import json
import joblib
import pandas as pd
import streamlit as st
from ui.components import page_header, section_header, kpi_card, footer


@st.cache_resource
def load_model():
    return joblib.load("models/salary_model.pkl")


@st.cache_data
def load_meta():
    with open("data/processed/salary_model_meta.json") as f:
        return json.load(f)


def show_salary():
    page_header(
        "Salary Predictor",
        "Estimate a market-competitive salary range for an Indian tech role using a model trained on real, disclosed job postings."
    )

    st.markdown('<div class="spacer-32"></div>', unsafe_allow_html=True)

    model = load_model()
    meta = load_meta()

    col_input, col_result = st.columns([1, 1.8])

    with col_input:
        st.markdown('<h3 style="margin-top: 0;">Your Profile</h3>', unsafe_allow_html=True)

        role_category = st.selectbox("Role", meta["role_categories"])
        skill_domain = st.selectbox("Primary Skill Domain", meta["skill_domains"])
        city = st.selectbox("City", meta["cities"])
        work_mode = st.selectbox("Work Mode", meta["work_modes"])
        company_size = st.selectbox("Company Size", meta["company_size_buckets"])

        exp_min_lo, exp_min_hi = meta["experience_min_range"]
        experience_min = st.slider(
            "Years of Experience (min)", int(exp_min_lo), int(exp_min_hi), min(3, int(exp_min_hi))
        )
        exp_max_lo, exp_max_hi = meta["experience_max_range"]
        experience_max = st.slider(
            "Years of Experience (max)", int(exp_max_lo), int(exp_max_hi), max(experience_min + 1, min(5, int(exp_max_hi)))
        )

        rating_lo, rating_hi = meta["company_rating_range"]
        company_rating = st.slider("Company Rating", rating_lo, rating_hi, 4.0, step=0.1)

        skills_lo, skills_hi = meta["skills_count_range"]
        skills_count = st.slider("Number of Skills Listed", int(skills_lo), int(skills_hi), min(4, int(skills_hi)))

        st.markdown('<div style="margin-top: 16px;"></div>', unsafe_allow_html=True)
        predict_clicked = st.button("Estimate Salary", type="primary")

    with col_result:
        st.markdown('<h3 style="margin-top: 0;">Estimated Salary</h3>', unsafe_allow_html=True)

        if predict_clicked:
            row = pd.DataFrame([{
                "experience_min_yrs": experience_min,
                "experience_max_yrs": experience_max,
                "company_rating": company_rating,
                "skills_count": skills_count,
                "role_category": role_category,
                "skill_domain": skill_domain,
                "work_mode": work_mode,
                "company_size_bucket": company_size,
                "city_bucketed": city,
            }])

            point_estimate = model.predict(row)[0]
            residual = meta["metrics"]["residual_std_lpa"]
            low = max(0, point_estimate - residual)
            high = point_estimate + residual

            kpi_row = st.columns(2)
            with kpi_row[0]:
                kpi_card("Estimate", f"₹{point_estimate:.1f} LPA", "currency")
            with kpi_row[1]:
                kpi_card("Range", f"₹{low:.1f} – {high:.1f} LPA", "chart")

            st.markdown('<div class="spacer-32"></div>', unsafe_allow_html=True)
            st.info(
                f"This model explains roughly {meta['metrics']['R2']*100:.0f}% of salary variance in the training "
                f"data (MAE ≈ ₹{meta['metrics']['MAE_lpa']} LPA) — enough to sanity-check where you land in the "
                f"market, not a guarantee. Treat the range as more reliable than the single number."
            )
        else:
            st.markdown(
                """
                <div style="border: 2px dashed var(--border); border-radius: var(--radius); padding: 48px; text-align: center; color: var(--text-secondary);" class="fade-in">
                    <i class="bi bi-cash-stack" style="font-size: 40px; display: block; margin-bottom: 16px; color: var(--primary);"></i>
                    <h4 style="margin: 0 0 8px 0; color: var(--text); font-weight: 600;">No Estimate Yet</h4>
                    <p style="margin: 0; font-size: 15px;">Fill in your profile on the left and click <strong>"Estimate Salary"</strong> to see a predicted range.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    footer()