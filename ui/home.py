import streamlit as st
from ui.components import hero, insight_card, feature_card, section_header, footer

def show_home(
    dashboard_kpis,
    role_summary,
    city_summary,
    company_summary,
    skill_summary
):
    
    kpis = dict(zip(dashboard_kpis["Metric"], dashboard_kpis["Value"]))

    top_role = role_summary.iloc[0]["job_title"]
    top_city = city_summary.iloc[0]["primary_city"]
    top_company = company_summary.iloc[0]["company_name"]
    top_skill = skill_summary.iloc[0]["Skill"]

    # =====================
    # Hero
    # =====================
    hero(
        "CareerLens AI",
        "Technology Job Market Intelligence",
        "Explore India's technology job market through hiring trends, in-demand skills, company insights, and personalized career recommendations.",
        [
            ("Jobs", f"{int(kpis['Total Jobs']):,}"),
            ("Companies", f"{int(kpis['Companies']):,}"),
            ("Cities", f"{int(kpis['Cities'])}"),
            ("Skill Domains", f"{int(kpis['Skill Domains'])}")
        ]
    )

    st.markdown("<div class='spacer-64'></div>", unsafe_allow_html=True)
    st.markdown("<div class='spacer-64'></div>", unsafe_allow_html=True)

    # ==================================================
    # Market Snapshot
    # ==================================================
    section_header(
        "Market Snapshot",
        " quick overview of the Indian technology job market."
    )

    row1 = st.columns(2)

    with row1[0]:
        insight_card(
            "Most In-Demand Role",
            top_role,
            "Role with the highest number of job postings",
            "briefcase"
        )

    with row1[1]:
        insight_card(
            "Top Hiring City",
            top_city,
            "City with the highest number of technology jobs",
            "globe"
        )

    row2 = st.columns(2)

    with row2[0]:
        insight_card(
            "Top Hiring Company",
            top_company,
            "Company with the most job postings",
            "activity"
        )

    with row2[1]:
        insight_card(
            "Most Requested Skill",
            top_skill,
            "Most frequently requested technical skill",
            "trending"
        )

    st.markdown("<div class='spacer-64'></div>", unsafe_allow_html=True)

    # ==================================================
    # Explore CareerLens
    # ==================================================
    section_header(
        "Explore CareerLens",
        "Jump into any module to dig deeper into the data, your fit, and your earning potential."
    )

    row1 = st.columns(2)

    with row1[0]:
        feature_card(
            "Market Insights",
            "Explore hiring trends, in-demand skills, top companies, and technology job opportunities across India.",
            "chart"
        )

    with row1[1]:
        feature_card(
            "Career Advisor",
            "Discover technology roles that match your skills and experience.",
            "target"
        )

    row2 = st.columns(2)

    with row2[0]:
        feature_card(
            "Salary Predictor",
            "Explore salary trends across different technology roles, locations, and experience levels.",
            "salary"
        )

    with row2[1]:
        feature_card(
            "About",
            "Learn about CareerLens AI, the technologies used, and the developer.",
            "info"
        )

    st.markdown("<div class='spacer-48'></div>", unsafe_allow_html=True)

    footer()