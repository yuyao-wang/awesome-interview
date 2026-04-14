# Claude Context — Interview Prep System

> This file is for Claude to read when the user says "create today's note", "push today's RM", or asks for tomorrow's schedule.

## About This Repo

Start date: 2026-04-13. Paper deadline: 2026-06-06. IELTS: 2026-06-13.  
Repo is public — daily notes double as a knowledge-sharing resource.

## The 5 Daily Tasks (in order)

| # | Task | Source | Pace |
|---|------|---------|------|
| 1 | BV16d Roadmap video | https://www.bilibili.com/video/BV16dQTBUEim/ | 1 segment/day |
| 2 | BV18g 300 Q video | https://www.bilibili.com/video/BV18gsdznEZX/ | 1 episode/day (46 total) |
| 3 | zsxq interview experience | https://articles.zsxq.com/id_7mbpnbe4w2w0.html | 1 article/day — **user must paste content, Claude cannot access** |
| 4 | Pyre Code | localhost:3000 (Project/pyre-code) | 1 problem/day, starting P1 |
| 5 | LeetCode Hot 100 | — | 1–2 problems/day |

## Additional Ongoing Projects

- **Personal project** (`Project/hanzi-browse`) — fit in when possible
- **Research project** — paper due **2026-06-06**, experiments + slides + write-up
- **IELTS** — exam **2026-06-13**, on **weekends**

## Pyre Code Problem List (for tracking)

P1 ReLU → P2 Softmax → P3 Linear → P4 LayerNorm → P5 Attention → P6 MHA → P7 BatchNorm → P8 RMSNorm → P9 Causal Attention → P10 GQA → P11 Sliding Window → P12 Linear Attention → P13 GPT2 Block → P14 KV Cache → P15 MLP → P16 Cross-entropy → P17 Dropout → P18 Embedding → P19 GELU → P20 Weight Init → ... → P68 Noise Schedule

## When the User Asks to "Push Today's RM" (Daily Note Workflow)

1. **Ask what was studied today** (or have the user paste video notes, zsxq article content)
2. **Help summarize** the knowledge from each item into clear, interview-ready Q&A format
3. **Fill in the daily template** (see `templates/daily_template.md`)
4. **Name the file** `daily/YYYY-MM-DD.md`
5. **Generate tomorrow's schedule** based on the default template + current progress counters
6. After writing the file: `git add . && git commit -m "Log: YYYY-MM-DD" && git push`

## How to Help the User Learn Each Topic

User's current level: knows terms, rough concepts, but lacks depth and cannot explain details in interviews.  
**Best approach: always quiz first, explain second.**  
After each topic, generate 3–5 questions and ask the user to answer them before giving the model answer.

## Key Interview Mindset (from BV16d)

For every topic, be able to answer:
1. What is it?
2. Why was it designed this way?
3. What are the tradeoffs?
4. How does it compare to alternatives?
