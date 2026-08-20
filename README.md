# CareerLens

An end-to-end data science project that turns ~23,000 scraped Indian tech job postings into an interactive Streamlit app: match your skills to real openings, browse market-wide demand trends, and get a data-driven salary estimate.



---

## What it does

| Page | What it shows |
|---|---|
| **Home** | Landing page with headline stats |
| **Market Insights** | City, role, and skill-demand breakdowns across the full dataset |
| **Career Advisor** | Pick your skills + experience level, get matching job postings ranked by skill overlap |
| **Salary Predictor** | Estimate a salary range (in LPA) from role, city, experience, and company profile, via a trained regression model |
| **About** | Project background |

---

## Tech stack

`Python` · `pandas` · `scikit-learn` · `Streamlit` · `joblib`

---

## Project structure

```
CareerLens/
├── app.py                     # Entry point / page router
├── requirements.txt
├── ui/                        # One module per page
│   ├── home.py
│   ├── market.py
│   ├── advisor.py
│   ├── salary.py
│   ├── about.py
│   └── components.py          # Shared UI (cards, headers, footer)
├── notebooks/                 # The data pipeline, run in order 1 → 5
│   ├── 1_data_understanding.ipynb
│   ├── 2_data_cleaning.ipynb        # Skill canonicalization happens ONCE, here
│   ├── 3_eda.ipynb
│   ├── 4_feature_engineering.ipynb  # Curated skill allowlist for the Advisor
│   └── 5_salary_model.ipynb         # Trains + saves the salary model
├── data/
│   ├── raw/                   # Original scrape (gitignored — see below)
│   └── processed/             # Cleaned CSVs the app actually reads
├── models/
│   └── salary_model.pkl       # Trained GradientBoostingRegressor pipeline
└── assets/
    └── theme.css
```

---

## Running it locally

```bash
git clone <your-repo-url>
cd CareerLens
pip install -r requirements.txt
streamlit run app.py
```

App opens at `http://localhost:8501`.

---

## The data pipeline

Rather than build the app straight on scraped data, this project runs the raw scrape through five notebooks, each producing a specific, reused artifact:

1. **Data Understanding** — first pass over the raw scrape (23,201 rows, ~30 columns).
2. **Data Cleaning** — the core of the project. Free-text skills (`.Net` / `.NET` / `asp.net`) get normalized into one canonical spelling per skill, junk tokens and generic non-skill terms get dropped, and skills too rare to be useful get filtered out. **This is the only place skill cleaning happens** — everything downstream reuses `clean_skill_frequency.csv` instead of re-deriving it.
3. **EDA** — sanity-checks the cleaning and surfaces the KPIs used on the Market Insights page.
4. **Feature Engineering** — builds `advisor_skills.csv`, a curated allowlist (~90 skills) of things an individual actually holds — languages, cloud platforms, BI tools, frameworks — filtered out of the much noisier full skill list so the Career Advisor's picker doesn't show scraped junk.
5. **Salary Model** — only ~12% of postings (2,768 of 23,201) disclose a salary. Trains and compares Linear Regression, Random Forest, and Gradient Boosting via cross-validation; saves the winning pipeline (`models/salary_model.pkl`) and a metadata JSON that the app reads for dropdown options and ranges — nothing about the form is hardcoded.

## Regenerating the data

`data/raw/*.csv` is gitignored (it's ~14MB and not read directly by the app — only by the notebooks). To regenerate it and rebuild everything from scratch:

1. Get the source dataset and place it at `data/raw/indian_tech_jobs_2026.csv`.
2. Run notebooks `1` through `5` in order.
3. `streamlit run app.py`

`data/processed/careerlens_cleaned.csv` **is** committed, since the app reads it directly at runtime — no rebuild step needed to just run the app.

---

## A note on the salary model

The model explains roughly 38% of salary variance (R² ≈ 0.38, MAE ≈ ₹5.3 LPA) on held-out data. That's a modest number, and it's expected: features like role, city, experience, and company size only capture part of what actually determines someone's salary — negotiation, individual performance, and unlisted benefits aren't in the data. Rather than present a single falsely-precise number, the app shows a **range** (point estimate ± residual standard deviation) and states the model's fit directly in the UI.

---

## Known limitations / next steps

- `role_category` currently has only 6 broad buckets (bucketed from free-text `job_title` upstream) — more granular roles would likely improve the salary model's R².
- `primary_city` is bucketed to the top 15 cities + "Other" for the salary model, since the disclosed-salary subset (2,768 rows) is too small to support all 121 raw cities without heavy sparsity.
- Salary training data is a real but attenuated sample: only 12% of scraped postings disclose a salary.

---

## Project history

This is the third iteration of this project. Earlier versions used, respectively, a synthetically-generated dataset (caught via internal-consistency checks — e.g. near-zero correlation between experience and salary) and a real-but-disconnected pairing of two unrelated datasets (real job postings + an unrelated global salary survey). This version is built entirely on one real, scraped dataset, end to end.
