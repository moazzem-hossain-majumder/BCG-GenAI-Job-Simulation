# BCG GenAI Job Simulation — Forage

Completed the Boston Consulting Group (BCGX) GenAI Job Simulation on Forage,
covering financial data extraction/analysis and a prototype AI-powered
financial chatbot.

> **Note:** Per Forage's program policy, this is a self-paced virtual job
> simulation, not employment or internship experience with BCG.

## Scenario

Acting as a junior data scientist on BCG's GenAI consulting team, tasked with
extracting and analyzing company financial data, then prototyping a chatbot
that answers questions about it.

## Repo contents

| File | What it is |
|---|---|
| `BCG_GenAI_Financial_Data_Extraction_Example.xlsx` | Extracted financial data for Microsoft, Tesla, and Apple (FY2023–2025) |
| `BCG_Task1.ipynb` | Pandas analysis of the extracted data |
| `task2_financial_chatbot.py` | Rule-based financial Q&A chatbot |
| `Task2_Documentation.pdf` | Design notes, limitations, and future improvements for the chatbot |
| `task2_test_results.txt` | Manual test cases and results |
| `BCG_GenAI_Job_Simulation.pdf` | Forage certificate of completion |

## Task 1 — Financial data extraction and analysis

Extracted and analyzed three years (FY2023–2025) of financial data for
**Microsoft, Tesla, and Apple**, sourced from company investor reports and
SEC filings. Using Pandas:

- Loaded the extracted dataset (revenue, net income, total assets,
  liabilities, operating cash flow) from Excel
- Calculated year-over-year growth rates for revenue and net income using
  `pct_change()`
- Computed a company-level summary of average growth rates for comparison

**Finding:** Microsoft showed the strongest average growth (~15% revenue,
~19% net income), while Tesla's net income declined sharply over the period
(~-49% average).

## Task 2 — AI-powered financial chatbot (prototype)

A rule-based chatbot that answers a fixed set of financial questions by
dictionary lookup — the user's question is matched (case-insensitive)
against predefined queries, and the corresponding answer is returned.

**Supported queries:**
- What is the total revenue?
- What is the net income?
- How has net income changed over the last year?
- What is the revenue growth?
- What are the total assets?

Any question outside this set returns a fallback message rather than
guessing. Manually tested against 5 cases (4 supported queries + 1
unsupported), all passing as documented in `task2_test_results.txt`.

**Honest scope note:** this is a rule-based dictionary lookup, not an LLM or
NLP model — it matches exact predefined questions and uses hardcoded values,
as documented in `Task2_Documentation.pdf`. Documented next steps for a
production version: reading live data via Pandas instead of hardcoded
values, real NLP (NLTK/spaCy) to handle natural-language variation, a Flask
web interface, and a connection to live financial APIs.

## Skills practiced

Python, Pandas, Excel, financial statement analysis, growth-rate
calculation, rule-based chatbot design, documentation

## Certificate

Completed June 2026 — see `BCG_GenAI_Job_Simulation.pdf`
