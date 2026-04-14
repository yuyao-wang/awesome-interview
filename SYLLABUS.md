# LLM Engineering Interview Syllabus

> Target: ByteDance LLM engineer (3 technical rounds)  
> Timeline: 7 weeks (Apr 14 – Jun 1)  
> Priority: ★★★ must know · ★★ should know · ★ good to know

For every topic, be able to answer four questions:
1. **What** is it?
2. **Why** was it designed this way?
3. **What tradeoffs** does it make?
4. **How does it compare** to alternatives?

---

## Part 1 — Foundations
*Week 1 · Prerequisite check — move fast if solid, slow down where gaps appear*

### 1.1 Linear Algebra ★★
- Matrix multiplication, transpose, inverse
- Eigenvalues / eigenvectors (used in PCA, understanding attention)
- SVD — intuition (used in LoRA derivation)

### 1.2 Probability & Statistics ★★
- Probability distributions: Gaussian, Categorical, KL divergence
- MLE vs MAP — what loss functions are really optimizing
- Cross-entropy loss: derivation from MLE

### 1.3 Neural Network Basics ★★★
- Forward pass / backward pass
- Computational graph and autograd
- Vanishing / exploding gradients — why they happen, how to fix
- Activation functions: sigmoid, tanh, ReLU, GELU, SwiGLU — tradeoffs

### 1.4 Optimization ★★★
- SGD → Momentum → Adam: what each adds and why
- Learning rate schedules: warmup, cosine decay
- Gradient clipping — when and why
- Weight initialization: Xavier, Kaiming — which to use and why

---

## Part 2 — Transformer Architecture
*Week 1–2 · Highest interview priority — expect deep probing on every component*

### 2.1 Scaled Dot-Product Attention ★★★
- Formula: `Attention(Q,K,V) = softmax(QKᵀ/√d_k)V`
- Why divide by √d_k? What happens without it?
- Computational complexity: O(T²d) — why this matters
- Masking: padding mask vs causal mask

### 2.2 Multi-Head Attention ★★★
- Architecture: split into h heads, attend independently, concat + project
- Why multiple heads? What does each head learn?
- Parameter count: 4 × d_model × d_model (Wq, Wk, Wv, Wo)
- MHA vs single-head: expressiveness tradeoff

### 2.3 Attention Variants ★★★
| Variant | Key idea | Where used |
|---------|----------|------------|
| MHA | h independent heads | original Transformer |
| MQA (Multi-Query) | 1 shared KV, multiple Q | Falcon, early Gemini |
| GQA (Grouped-Query) | g shared KV groups | LLaMA 2/3, Mistral |
| MLA (Multi-Latent) | compressed KV latent | DeepSeek-V2/V3 |

Interview question: *Why did we move from MHA → MQA → GQA? What problem does each solve?*

### 2.4 Feed-Forward Network (FFN) ★★★
- Standard: two linear layers with ReLU in between
- SwiGLU (used in LLaMA): `SwiGLU(x) = (xW₁) ⊙ SiLU(xWgate)` — why gating helps
- Hidden dim is typically 4× or 8/3× d_model — why?

### 2.5 Residual Connections ★★★
- Why residuals? Gradient highway — prevents vanishing gradients in deep nets
- Pre-LN vs Post-LN: original Transformer uses Post-LN; modern LLMs use Pre-LN
- Why Pre-LN? Training stability — gradients don't explode in early layers

### 2.6 Normalization ★★★
| Type | Normalizes over | Used in |
|------|----------------|---------|
| BatchNorm | batch dimension | CNNs |
| LayerNorm | feature dimension | original Transformer |
| RMSNorm | feature dim, no mean | LLaMA, Mistral (faster) |

Interview question: *Why can't we use BatchNorm in Transformers? Why is RMSNorm preferred over LayerNorm in LLMs?*

---

## Part 3 — Position Encoding
*Week 2 · Frequently asked standalone topic*

### 3.1 Sinusoidal (Original) ★★
- Formula: `PE(pos, 2i) = sin(pos/10000^(2i/d_model))`
- Fixed, not learned; allows length extrapolation in theory
- Why does this work? Each position gets a unique fingerprint

### 3.2 Learned Absolute PE ★★
- Simple: add a learned vector per position
- Problem: fixed max sequence length; poor extrapolation

### 3.3 RoPE (Rotary Position Embedding) ★★★
- Key idea: encode position as a rotation in 2D subspaces of Q and K
- Property: `q_m · k_n` depends only on relative position `m-n`
- Why better? Relative position awareness + good extrapolation
- Used in: LLaMA, Mistral, Qwen, DeepSeek
- Extension: NTK-aware scaled RoPE for longer contexts

### 3.4 ALiBi ★★
- Add a linear bias to attention scores based on distance: `score - m × |i-j|`
- No position vectors; extrapolates well beyond training length
- Used in: BLOOM, MPT

Interview question: *Compare RoPE vs ALiBi. When would you choose one over the other?*

---

## Part 4 — LLM Architecture & Training
*Week 3 · Understand how GPT/LLaMA actually works end-to-end*

### 4.1 GPT Architecture (Decoder-only) ★★★
- Token embedding + position encoding → N × (MHA + FFN) → LM head
- Causal attention (lower triangular mask)
- Autoregressive generation: next-token prediction

### 4.2 LLaMA / Modern LLM Differences vs Original GPT ★★★
| Component | GPT-2 | LLaMA |
|-----------|-------|-------|
| Norm | Post-LN | Pre-LN (RMSNorm) |
| Activation | GELU | SwiGLU |
| Position | Learned absolute | RoPE |
| Attention | MHA | GQA |

### 4.3 Tokenization ★★
- BPE (Byte Pair Encoding): merge most frequent pairs iteratively
- WordPiece, SentencePiece — differences
- Why subword tokenization? Balance between OOV and vocab size

### 4.4 Scaling Laws ★★
- Chinchilla: optimal tokens ≈ 20× parameters
- What happens when you over/under-train?
- Emergent abilities — threshold behavior at scale

### 4.5 Training Stability ★★
- Loss spikes: causes (bad data, LR too high) and mitigation
- Gradient clipping necessity at large scale
- Mixed precision (FP16/BF16) — why BF16 is preferred

---

## Part 5 — Fine-Tuning & Alignment
*Week 4 · Highest practical interview weight at ByteDance*

### 5.1 Full Fine-Tuning ★★
- Update all parameters; expensive but best quality
- Catastrophic forgetting — what it is, how to mitigate

### 5.2 LoRA ★★★
- Freeze W, add low-rank decomposition: `ΔW = BA` where B ∈ ℝ^(d×r), A ∈ ℝ^(r×k)
- Why does this work? Hypothesis: weight updates have low intrinsic rank
- Hyperparameters: rank r, alpha α (scaling), which layers to apply to
- Merge at inference: `W' = W + (α/r)BA` — zero extra latency

### 5.3 QLoRA ★★★
- 4-bit quantize the base model, add LoRA adapters in BF16
- NF4 (Normal Float 4) quantization — why NF4 not INT4?
- Double quantization to save even more memory
- When to use: fine-tune 70B on a single A100

### 5.4 RLHF Pipeline ★★★
1. Supervised Fine-Tuning (SFT) on demonstrations
2. Train Reward Model (RM) on preference pairs
3. Optimize policy with PPO against RM

### 5.5 PPO in LLMs ★★★
- Clipped objective: `L = min(r_t A_t, clip(r_t, 1-ε, 1+ε) A_t)`
- KL penalty: keep policy close to SFT reference
- Why clip? Prevent too-large policy updates
- Problems: reward hacking, complexity of 4 models in memory

### 5.6 DPO ★★★
- Skip RM training; directly optimize on preference pairs
- Loss: `L = -log σ(β log(π/π_ref on chosen) - β log(π/π_ref on rejected))`
- Why simpler? Implicit reward is the log ratio of policy to reference
- Tradeoff vs PPO: simpler but less flexible; can't do online learning

### 5.7 GRPO ★★
- Group Relative Policy Optimization (used in DeepSeek-R1)
- Remove value network; normalize advantages within a group of responses
- Used for reasoning tasks with verifiable rewards

---

## Part 6 — Inference Optimization
*Week 5 · Critical for engineering roles — expect implementation questions*

### 6.1 KV Cache ★★★
- Cache K and V from all previous tokens; only compute new token's Q
- Memory cost: `2 × num_layers × seq_len × d_model × precision_bytes`
- Problem at scale: KV cache can be larger than model weights

### 6.2 FlashAttention ★★★
- Problem: standard attention materializes the O(T²) attention matrix in HBM
- Solution: tile Q, K, V into SRAM blocks; compute attention without materializing full matrix
- Result: IO complexity O(T²/B) instead of O(T²); 2-4× faster, exact same output
- V2 improvements: better parallelism across heads and sequence

### 6.3 vLLM & PagedAttention ★★★
- Problem: KV cache has internal/external fragmentation (like malloc)
- Solution: non-contiguous physical memory pages, mapped via block table
- Enables: higher batch sizes, efficient parallel sampling, beam search

### 6.4 Quantization ★★★
| Method | Precision | Approach |
|--------|-----------|----------|
| INT8 / W8A8 | 8-bit | scale + zero-point per tensor/channel |
| GPTQ | 4-bit | layer-wise second-order quantization |
| AWQ | 4-bit | protect salient weights (based on activation magnitude) |
| NF4 | 4-bit | non-uniform; optimal for normally distributed weights |

Interview: *Why does AWQ outperform GPTQ on some benchmarks? What does "activation-aware" mean?*

### 6.5 Speculative Decoding ★★
- Small draft model generates k tokens; large target model verifies all in one forward pass
- Acceptance: keep draft token if target probability is high enough
- Speedup: ~2-3× with well-matched draft model

### 6.6 Continuous Batching ★★
- Problem: static batching wastes GPU when sequences finish at different times
- Solution: insert new requests mid-batch as slots free up
- Used by: vLLM, TGI

---

## Part 7 — Applications
*Week 6 · Increasingly asked; expect system design questions*

### 7.1 RAG (Retrieval-Augmented Generation) ★★★
- Pipeline: query → embed → retrieve from vector DB → rerank → generate
- Chunking strategies: fixed-size, sentence, semantic — tradeoffs
- Retrieval: dense (embedding similarity) vs sparse (BM25) vs hybrid
- Reranking: cross-encoder scores (query, doc) pairs — expensive but accurate
- Common failure modes: retrieval miss, context overflow, hallucination despite retrieval

### 7.2 LLM Agents ★★★
- ReAct: interleave reasoning (Thought) and acting (Action/Observation)
- Tool use: function calling, how to define tool schemas
- Multi-agent: planner + executor pattern
- Memory: in-context (limited), external (vector DB), episodic

### 7.3 Hallucination ★★★
- Causes: training data gaps, overconfident generation, exposure bias
- Mitigation: RAG, RLHF on factuality, self-consistency sampling, citations

### 7.4 Long Context ★★
- Challenges: quadratic attention cost, position encoding extrapolation, lost-in-the-middle
- Solutions: RoPE scaling (linear, NTK, YaRN), sliding window attention, sparse attention

### 7.5 Prompt Engineering ★★
- Zero-shot, few-shot, chain-of-thought (CoT), self-consistency
- System prompt design; jailbreak resistance

---

## Part 8 — Systems & Distributed Training
*Week 7 · More likely in senior roles; cover basics for any role*

### 8.1 Data Parallelism ★★
- Replicate model on each GPU; split batch; average gradients
- DDP (PyTorch): all-reduce after backward
- FSDP: shard parameters + gradients + optimizer states across GPUs

### 8.2 Model Parallelism ★★
- **Tensor Parallelism:** split weight matrices across GPUs (Megatron-LM style)
- **Pipeline Parallelism:** assign layers to different GPUs; micro-batching to hide bubbles
- **Sequence Parallelism:** split sequence dimension (ring attention)

### 8.3 Mixed Precision Training ★★
- FP16: dynamic range issues (overflow); needs loss scaling
- BF16: same exponent bits as FP32; preferred for LLMs
- AMP (Automatic Mixed Precision): keep master weights in FP32

### 8.4 Gradient Checkpointing (Activation Checkpointing) ★★
- Recompute activations during backward instead of storing them
- Memory: O(√N) instead of O(N) layers; ~33% compute overhead

### 8.5 MoE (Mixture of Experts) ★★★
- Replace FFN with E expert FFNs; router selects top-k per token
- Load balancing loss: penalize router imbalance
- Used in: Mixtral, DeepSeek-MoE, GPT-4 (rumored)
- Tradeoff: more parameters, same FLOPs per token; requires expert parallelism

---

## Week-by-Week Map

| Week | Focus | Pyre Code range | BV18g range |
|------|-------|----------------|-------------|
| 1 (Apr 14–20) | Foundations + Attention core | P1–P7 | Ep 1–7 |
| 2 (Apr 21–27) | Attention variants + Position encoding | P8–P14 | Ep 8–14 |
| 3 (Apr 28–May 4) | LLM architecture + Tokenization | P15–P21 | Ep 15–21 |
| 4 (May 5–11) | Fine-tuning + Alignment | P22–P30 | Ep 22–30 |
| 5 (May 12–18) | Inference optimization | P31–P40 | Ep 31–38 |
| 6 (May 19–25) | RAG + Agents + Applications | P41–P50 | Ep 39–46 |
| 7 (May 26–Jun 1) | Systems + MoE + Review | P51–P60 | Review weak spots |
| 8 (Jun 2–8) | Mock interviews + Buffer | P61–P68 | — |

---

## Top 20 Questions ByteDance Will Ask

These come up in almost every LLM interview round. Practice explaining each in under 2 minutes.

1. Explain attention. Why scale by √d_k?
2. MHA vs GQA vs MLA — why did we evolve from one to the next?
3. Why Pre-LN instead of Post-LN in modern LLMs?
4. Why RMSNorm instead of LayerNorm?
5. RoPE — how does it encode relative position? How does it extrapolate?
6. LoRA — why does low-rank work? How do you choose rank?
7. QLoRA — what is NF4 and why is it better than INT4 for LLMs?
8. RLHF pipeline — walk through all 3 stages.
9. PPO vs DPO — when would you use each? What does DPO sacrifice?
10. KV Cache — memory formula, why it's the bottleneck at scale.
11. FlashAttention — what memory problem does it solve and how?
12. PagedAttention — what is KV cache fragmentation and how does it fix it?
13. Quantization — GPTQ vs AWQ. What does "activation-aware" mean?
14. Speculative decoding — how does acceptance sampling work?
15. MoE — what is load balancing loss and why is it needed?
16. RAG — dense vs sparse retrieval. When does reranking help?
17. Hallucination — three causes and three mitigations.
18. Catastrophic forgetting — what causes it, how do you avoid it?
19. BF16 vs FP16 — why does BF16 dominate LLM training?
20. FSDP vs DDP — when does sharding help?
