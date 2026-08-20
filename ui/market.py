import streamlit as st
import pandas as pd
import plotly.express as px
from ui.components import kpi_card, page_header, section_header, footer

def style_plotly_fig(fig):
    """
    Applies custom styling to a Plotly figure to make it look like a premium SaaS widget.
    Ensures title is cleared on the figure itself to avoid the 'undefined' label,
    since we render the title using custom HTML container headers.
    """
    fig.update_layout(
        font_family="Inter, sans-serif",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#FFFFFF", # White chart background
        font_color="#111827",
        title="", # Clear internal title using empty string to prevent "undefined" display
        title_text="",
        margin=dict(l=10, r=10, t=10, b=10),
    )
    fig.update_xaxes(
        showgrid=True,
        gridcolor="#E5E7EB", # Subtle grid lines
        zeroline=False,
        title_font=dict(size=12, color="#111827", family="Inter, sans-serif"),
        tickfont=dict(size=11, color="#111827", family="Inter, sans-serif")
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="#E5E7EB",
        zeroline=False,
        title_font=dict(size=12, color="#111827", family="Inter, sans-serif"),
        tickfont=dict(size=11, color="#111827", family="Inter, sans-serif")
    )
    return fig

def render_chart_card(title, description, fig):
    """
    Renders a Plotly figure enclosed in a styled container card.
    Uses st.container(border=True) targeted by CSS overrides.
    """
    with st.container(border=True):
        st.markdown(f"### {title}")
        st.markdown(f"<p class='stCaption' style='margin-top: -8px; margin-bottom: 12px;'>{description}</p>", unsafe_allow_html=True)
        st.plotly_chart(style_plotly_fig(fig), use_container_width=True)
def show_market(
    role_summary,
    city_summary,
    company_summary,
    skill_summary
):
    page_header(
        "Market Insights",
        "Explore hiring trends, skill demand, and company activity across India's technology job market."
    )
    
    st.markdown('<div class="spacer-32"></div>', unsafe_allow_html=True)
    
    section_header("Market Overview","A high-level overview of the Indian technology job market.")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        kpi_card("Job Roles",f"{len(role_summary):,}","briefcase","Unique technology roles")
    with col2:
        kpi_card("Companies",f"{len(company_summary):,}","building","Hiring companies")
    with col3:
        kpi_card("Cities",f"{len(city_summary):,}","globe","Hiring locations")
    with col4:
        kpi_card("Skills",f"{len(skill_summary):,}","activity","Unique technical skills")

    st.markdown('<div class="spacer-32"></div>', unsafe_allow_html=True)

    # ======================================================
    # HIRING TRENDS
    # ======================================================

    section_header("Hiring Landscape","Explore the most active technology roles, cities, and employer")
    
    # Palette colors requested: #1D4ED8, #2563EB, #3B82F6, #60A5FA, #93C5FD
    blue_scale = ["#93C5FD", "#60A5FA", "#3B82F6", "#2563EB", "#1D4ED8"]
    fig = px.bar(
        role_summary.sort_values("Number_of_Jobs",ascending=False).head(10),
        x="Number_of_Jobs",
        y="job_title",
        orientation="h",
        color="Number_of_Jobs",
        color_continuous_scale=blue_scale
        )

    fig.update_yaxes(autorange="reversed")
    render_chart_card("Top Job Roles","Most frequently advertised technology roles.",fig )

    fig = px.bar(
            city_summary.sort_values("Number_of_Jobs",ascending=False).head(10),
            x="Number_of_Jobs",
            y="primary_city",
            orientation="h",
            color="Number_of_Jobs",
            color_continuous_scale=blue_scale
        )
    fig.update_yaxes(autorange="reversed")
    render_chart_card(
        "Top Hiring Cities",
        "Cities with the highest number of job postings.",
        fig
    )
    st.markdown('<div class="spacer-32"></div>', unsafe_allow_html=True)

    fig = px.bar(
        company_summary.sort_values("Number_of_Jobs",ascending=False).head(10),
        x="Number_of_Jobs",
        y="company_name",
        orientation="h",
        color="Number_of_Jobs",
        color_continuous_scale=blue_scale
    )
    fig.update_yaxes(autorange="reversed")
    render_chart_card(
        "Top Hiring Companies",
        "Organizations with the largest number of technology job postings.",
        fig
    )

    st.markdown('<div class="spacer-32"></div>', unsafe_allow_html=True)

    section_header(
        "Skills Landscape",
        "The most requested technical skills across technology jobs."
    )

    fig = px.bar(
        skill_summary.sort_values("Frequency",ascending=False).head(20),
        x="Frequency",
        y="Skill",
        orientation="h",
        color="Frequency",
        color_continuous_scale=blue_scale
    )
    fig.update_yaxes(autorange="reversed")
    render_chart_card(
        "Top Technical Skills",
        "Most frequently requested skills in the Indian technology job market.",
        fig
    )
    st.markdown('<div class="spacer-32"></div>', unsafe_allow_html=True)

    section_header(
        "Market Summary",
        "Key highlights from the current technology job market."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Most In-Demand Role",
            role_summary.iloc[0]["job_title"]
        )

        st.metric(
            "Top Hiring Company",
            company_summary.iloc[0]["company_name"]
        )

    with col2:

        st.metric(
            "Top Hiring City",
            city_summary.iloc[0]["primary_city"]
        )

        st.metric(
            "Most Requested Skill",
            skill_summary.iloc[0]["Skill"]
        )

    footer()