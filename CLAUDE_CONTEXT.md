# Claude Context — Interview Prep System

> This file is for Claude to read when the user says "create today's note", "push today's RM", or asks for tomorrow's schedule.

## About This Repo

Interview prep for ByteDance LLM engineer roles (3 technical rounds).  
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

- **Hanzi-browser** (`Project/hanzi-browse`) — fit in when possible (17:00–18:00)
- **Research project** — paper due **2026-06-06**, experiments + slides + write-up
- **IELTS** — exam **2026-06-13**, practice full exams on **weekends**

## Pyre Code Problem List (for tracking)

P1 ReLU → P2 Softmax → P3 Linear → P4 LayerNorm → P5 Attention → P6 MHA → P7 BatchNorm → P8 RMSNorm → P9 Causal Attention → P10 GQA → P11 Sliding Window → P12 Linear Attention → P13 GPT2 Block → P14 KV Cache → P15 MLP → P16 Cross-entropy → P17 Dropout → P18 Embedding → P19 GELU → P20 Weight Init → ... → P68 Noise Schedule

## Default Weekday Schedule Template

| Time | Task |
|------|------|
| 9:00–9:30 | LeetCode Hot 100 |
| 9:30–10:30 | Pyre Code |
| 10:30–11:30 | BV18g: 1 episode + notes |
| 11:30–12:00 | Interview Experience (user pastes article) |
| 14:00–16:00 | Research work |
| 16:00–17:00 | BV16d: Roadmap segment |
| 17:00–18:00 | Hanzi-browser |
| 20:00–20:30 | Write daily note → commit & push |

## Weekend Schedule (adjust for IELTS practice)

| Time | Task |
|------|------|
| 9:00–11:00 | IELTS practice exam (full paper) |
| 11:00–12:00 | Review weekly notes / weak areas |
| 14:00–16:00 | Research work |
| 16:00–17:00 | LeetCode (1–2 problems) |
| 17:00–18:00 | Pyre Code (1 problem) |
| 20:00–20:30 | Write daily note → commit & push |

## When the User Asks to "Push Today's RM" (Daily Note Workflow)

1. **Ask what was studied today** (or have the user paste video notes, zsxq article content)
2. **Help summarize** the knowledge from each item into clear, interview-ready Q&A format
3. **Fill in the daily template** (see `templates/daily_template.md`)
4. **Name the file** `daily/YYYY-MM-DD.md`
5. **Generate tomorrow's schedule** based on the default template + current progress counters
6. After writing the file: `git add . && git commit -m "日志: YYYY-MM-DD" && git push`

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
