import streamlit as st
import textwrap
import pandas as pd

from pathlib import Path

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CareerLens AI",
    page_icon=None,
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
dashboard_kpis = pd.read_csv("data/processed/dashboard_kpis.csv")

role_summary = pd.read_csv("data/processed/role_summary.csv")

city_summary = pd.read_csv("data/processed/city_summary.csv")

company_summary = pd.read_csv("data/processed/company_summary.csv")

skill_summary = pd.read_csv("data/processed/skill_summary.csv")

advisor_skills = pd.read_csv("data/processed/advisor_skills.csv")

jobs = pd.read_csv("data/processed/careerlens_cleaned.csv",
    keep_default_na=False
)



# -----------------------------
# Load Custom CSS
# -----------------------------
def load_css():
    css = Path(__file__).parent / "assets" / "theme.css"
    with open(css, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
st.markdown("""
<link rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
""", unsafe_allow_html=True)


# -----------------------------
# Sidebar Header
# -----------------------------
st.sidebar.markdown(
    textwrap.dedent("""
    <div class="sidebar-header">
        <div class="sidebar-title">CareerLens AI</div>
        <p class="sidebar-subtitle">AI Career Intelligence</p>
    </div>
    """).strip(),
    unsafe_allow_html=True
)

# -----------------------------
# Navigation
# -----------------------------
navigation_options = [
    "Home",
    "Market Insights",
    "Career Advisor",
    "Salary Predictor",
    "About"
]

if "navigation_selection" not in st.session_state:
    st.session_state.navigation_selection = "Home"

selected_page = st.sidebar.radio(
    "Navigation",
    navigation_options,
    key="navigation_selection"
)

page = selected_page


# -----------------------------
# Page Routing
# -----------------------------
if page == "Home":
    from ui.home import show_home
    show_home(
        dashboard_kpis,
        role_summary,
        city_summary,
        company_summary,
        skill_summary
    )

elif page == "Market Insights":
    from ui.market import show_market

    show_market(
        role_summary,
        city_summary,
        company_summary,
        skill_summary
    )

elif page == "Career Advisor":
    from ui.advisor import show_advisor

    show_advisor(jobs, advisor_skills)

elif page == "Salary Predictor":
    from ui.salary import show_salary

    show_salary()

elif page == "About":
    from ui.about import show_about

    show_about(dashboard_kpis)