# LLM Engineering Interview Prep: Open Notes & Knowledge Base

> A structured, public knowledge base built while preparing for LLM engineering interviews at top AI companies (ByteDance, etc.).
> One daily check-in at a time — covering theory, implementation, and real interview experience.

This repo serves a dual purpose:

1. **Personal accountability** — daily practice logs, code implementations, and study notes
2. **Community resource** — clear, structured summaries of LLM interview topics for anyone preparing for similar roles

---

## Repository Structure

```
daily/           → Day-by-day notes (checklists + topic summaries)
templates/       → Daily check-in template
*.py             → Implementation scratch files
```

---

## Knowledge Areas

These are the core topics that appear repeatedly in LLM engineer interviews at ByteDance and similar companies. Each entry is updated as I study it.

### Transformer Architecture & Attention
- Scaled Dot-Product Attention — why divide by √d_k?
- Multi-Head Attention — what does each head learn?
- KV Cache — mechanism and memory cost
- FlashAttention — IO-aware exact attention
- Grouped-Query Attention (GQA) and Multi-Latent Attention (MLA)
- Causal / Sliding Window / Linear Attention variants

### Position Encoding
- Sinusoidal (original Transformer)
- RoPE (Rotary Position Embedding) — used in LLaMA, DeepSeek
- ALiBi — attention with linear biases

### Normalization
- LayerNorm vs BatchNorm vs RMSNorm
- Pre-norm vs Post-norm — which is more stable and why

### Fine-Tuning
- Full fine-tuning vs PEFT
- LoRA — low-rank decomposition, rank selection, math intuition
- QLoRA — quantization-aware fine-tuning

### Alignment & RLHF
- RLHF pipeline: reward model → PPO
- PPO in the LLM setting — what gets clipped and why
- DPO — how it simplifies RLHF, what it sacrifices

### Inference Optimization
- vLLM & PagedAttention — why fragmented KV caches hurt
- Quantization: INT8, GPTQ, AWQ, INT4
- Speculative decoding
- Continuous batching

### RAG (Retrieval-Augmented Generation)
- Basic pipeline: chunking → embedding → retrieval → generation
- Chunking strategies
- Reranking with cross-encoders

### Advanced Topics
- Mixture of Experts (MoE) — load balancing, sparse routing
- Long context: handling >128k tokens
- Hallucination — root causes and mitigation strategies
- Multimodal architectures (ViT block, cross-attention)
- MCTS in LLMs (tree search, reasoning)
- Diffusion models — DDIM, flow matching

---

## Learning Resources

| Resource | Description |
|----------|-------------|
| [大模型学习路线 (BV16dQTBUEim)](https://www.bilibili.com/video/BV16dQTBUEim/) | 5-stage LLM interview roadmap based on real ByteDance/Meituan experience |
| [大厂300道LLM面试题 (BV18gsdznEZX)](https://www.bilibili.com/video/BV18gsdznEZX/) | 46-episode series covering 300 top LLM interview questions |
| Real interview experience articles | Curated Q&A from candidates at top AI labs |
| [Pyre Code](https://github.com/whwangovo/pyre-code) | 68 implementation challenges — write LLM internals from scratch |
| LeetCode Hot 100 | Classical algorithms: required for any top-tier tech interview |

---

## Daily Progress

See the [`daily/`](./daily/) folder for day-by-day check-ins. Each note covers:
- What was studied that day (videos, articles, problems)
- Key knowledge summaries with Q&A
- Code implementations
- Tomorrow's schedule

---

## Implementation Index

| File | Topic |
|------|-------|
| `attention.py` | Scaled Dot-Product Self-Attention (from scratch) |

*More implementations added daily from the Pyre Code problem set.*

---

*Preparing for LLM engineering roles? Feel free to follow along, open an issue to discuss a topic, or share your own notes.*
