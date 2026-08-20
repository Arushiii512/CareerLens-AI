import streamlit as st
import textwrap
from ui.components import page_header, footer

def show_about(dashboard_kpis):
    page_header(
        "About CareerLens AI",
        "An AI-powered career intelligence platform that analyzes the Indian technology job market through data analytics, interactive dashboards, and personalized career recommendations."
    )
    
    st.markdown('<div class="spacer-32"></div>', unsafe_allow_html=True)
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown('<h3 style="margin-top: 0; color: var(--primary);">What is CareerLens AI?</h3>', unsafe_allow_html=True)
        st.markdown(
            textwrap.dedent("""
            <p style="font-size: 15px; line-height: 1.65; margin: 0 0 12px 0;">
                CareerLens is an application built to help students and professionals explore the Indian technology job market.
            <p style="font-size: 15px; line-height: 1.65; margin: 0;">
                The platform analyzes thousands of technology job postings to identify hiring trends, in-demand skills, top companies, and career opportunities. It also provides personalized job recommendations based on a user's technical skills and experience level, enabling informed career planning through data-driven insights.
            """).strip(),
            unsafe_allow_html=True
        )
        
    with col_right:
        st.markdown('<h3 style="margin-top: 0;">Key Platform Capabilities</h3>', unsafe_allow_html=True)
        st.markdown(
            textwrap.dedent("""
            <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 4px;">
                <div style="display: flex; gap: 10px; align-items: flex-start;">
                    <i class="bi bi-bar-chart-line-fill" style="font-size: 18px; color: var(--primary);"></i>
                    <div>
                        <strong style="color: var(--text);">Market Insights</strong>
                        <div style="font-size: 13px; color: var(--text-secondary);">Explore hiring trends, leading companies, top hiring cities, and the most requested technical skills.</div>
                    </div>
                </div>
                <div style="display: flex; gap: 10px; align-items: flex-start;">
                    <i class="bi bi-bullseye" style="font-size: 18px; color: var(--primary);"></i>
                    <div>
                        <strong style="color: var(--text);">Career Advisor</strong>
                        <div style="font-size: 13px; color: var(--text-secondary);">Receive personalized job recommendations based on your technical skills and experience level.</div>
                    </div>
                </div>
                <div style="display: flex; gap: 10px; align-items: flex-start;">
                    <i class="bi bi-cash-stack" style="font-size: 18px; color: var(--primary);"></i>
                    <div>
                        <strong style="color: var(--text);">Career Report</strong>
                        <div style="font-size: 13px; color: var(--text-secondary);">Generate a downloadable report summarizing job matches, skill gaps, and market insights.</div>
                    </div>
                </div>
            </div>
            """).strip(),
            unsafe_allow_html=True
        )
        
    st.markdown('<hr>', unsafe_allow_html=True)
    kpis = dict(zip(dashboard_kpis["Metric"], dashboard_kpis["Value"]))
    st.markdown("### Project Statistics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Jobs", f"{int(kpis['Total Jobs']):,}")
    with col2:
        st.metric("Companies", f"{int(kpis['Companies']):,}")
    with col3:
        st.metric("Cities", f"{int(kpis['Cities'])}")
    with col4:
        st.metric("Skill Domains", f"{int(kpis['Skill Domains'])}")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<h3 style="margin-top: 0; margin-bottom: 12px;">Technology Stack</h3>', unsafe_allow_html=True)
    
    tech_stack = [ "Python","Pandas","NumPy","Plotly","Matplotlib","Streamlit","Scikit-learn","ReportLab"]
    
    tech_html = "".join([f'<span class="skill-pill" style="font-size: 14px; padding: 6px 16px; margin: 4px; display: inline-block;">{tech}</span>' for tech in tech_stack])
    st.markdown(f'<div style="margin-bottom: 8px;">{tech_html}</div>', unsafe_allow_html=True)
    
    st.markdown('<hr>', unsafe_allow_html=True)
    
    st.markdown('<h3 style="margin-top: 0; margin-bottom: 8px;">Developer Profile</h3>', unsafe_allow_html=True)
    
    st.markdown(
        textwrap.dedent("""
        <div class="dev-card fade-in">
            <div class="dev-avatar">AR</div>
            <div class="dev-info">
                <div class="dev-name">Arushi Ramesh</div>
                <div class="dev-title">B.Tech Computer Science & Engineering</div>
                <div style="font-size: 14px; color: var(--text-secondary); margin-bottom: 8px;">
                    Indian Institute of Information Technology Pune (IIIT Pune)
                </div>
                <div class="dev-links">
                    <a href="https://github.com" target="_blank" class="btn-primary" style="padding: 10px 20px; font-size: 13px; display: inline-flex; align-items: center; gap: 8px; text-decoration: none;">
                        <i class="bi bi-github"></i> GitHub Profile
                    </a>
                    <a href="https://linkedin.com" target="_blank" class="btn-secondary" style="padding: 10px 20px; font-size: 13px; display: inline-flex; align-items: center; gap: 8px; text-decoration: none;">
                        <i class="bi bi-linkedin"></i> LinkedIn Profile
                    </a>
                </div>
            </div>
        </div>
        """).strip(),
        unsafe_allow_html=True
    )
    
    footer()
