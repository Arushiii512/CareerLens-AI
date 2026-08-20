import streamlit as st
import textwrap
import streamlit as st

def render_html(html):
    lines = textwrap.dedent(html).strip().splitlines()
    cleaned = "\n".join(line.lstrip() for line in lines)
    st.markdown(cleaned, unsafe_allow_html=True)

def hero(title, subtitle, description, stats):

    stats_html = ""

    for label, value in stats:
        stats_html += f"""
        <div class="hero-stat">
            <div class="hero-stat-value">{value}</div>
            <div class="hero-stat-label">{label}</div>
        </div>
        """

    html = f"""
    <section class="hero-container fade-in">

        <div class="hero-tag">
            <i class="bi bi-stars"></i>
            AI Career Intelligence Platform
        </div>

        <h1 class="hero-title">{title}</h1>

        <div class="hero-subtitle">{subtitle}</div>

        <p class="hero-description">
            {description}
        </p>

        <div class="hero-divider"></div>

        <div class="hero-stats">

            {stats_html}

        </div>

    </section>
    """

    render_html(html)

def page_header(title, description):
    """
    Reusable top-of-page header: large title + secondary caption line.
    """
    html = f"""
    <div class="page-header fade-in">
        <h1>{title}</h1>
        <p class="stCaption">{description}</p>
    </div>
    """
    render_html(html)


def section_header(title, description=None):
    """
    Reusable section heading used to introduce a block of content on a page
    (e.g. "Salary Analysis", "Market Demand & Hiring").
    """
    desc_html = f'<p class="stCaption" style="margin-bottom: 16px;">{description}</p>' if description else ""
    html = f"""
    <div class="section-header">
        <h2>{title}</h2>
        {desc_html}
    </div>
    """
    render_html(html)


def kpi_card(title, value, icon, subtitle=""):

    icon_map = {
        "briefcase": "bi bi-briefcase-fill",
        "globe": "bi bi-globe2",
        "currency": "bi bi-cash-stack",
        "tools": "bi bi-tools",
        "chart": "bi bi-bar-chart-fill",
        "target": "bi bi-bullseye",
        "trending": "bi bi-graph-up-arrow",
        "activity": "bi bi-activity",
        "salary": "bi bi-currency-dollar",
        "info": "bi bi-info-circle-fill",
        "lightbulb": "bi bi-lightbulb-fill",
        "brain": "bi bi-cpu-fill",
        "home": "bi bi-house-door-fill",
        "fire": "bi bi-fire",
        "building": "bi bi-building-fill",
    }

    html = f"""
    <div class="kpi-card fade-in">

        <div class="kpi-header">

            <span class="kpi-title">{title}</span>

            <div class="kpi-icon">
                <i class="{icon_map.get(icon,'bi bi-circle-fill')}"></i>
            </div>

        </div>

        <div class="kpi-value">{value}</div>

        <div class="kpi-subtitle">{subtitle}</div>

    </div>
    """

    render_html(html)

def insight_card(title, value, text, icon):

    icon_map = {
        "briefcase": "bi bi-briefcase-fill",
        "activity": "bi bi-fire",
        "trending": "bi bi-graph-up-arrow",
        "globe": "bi bi-globe2",
        "currency": "bi bi-cash-stack",
        "target": "bi bi-bullseye",
        "chart": "bi bi-bar-chart-fill",
        "brain": "bi bi-cpu-fill",
        "salary": "bi bi-currency-dollar",
        "lightbulb": "bi bi-lightbulb-fill",
        "star": "bi bi-star-fill",
    }

    html = f"""
    <div class="insight-card fade-in">

        <div class="insight-icon-container">
            <i class="{icon_map.get(icon,'bi bi-circle-fill')}"></i>
        </div>

        <div class="insight-content">

            <div class="insight-label">
                {title}
            </div>

            <div class="insight-value">
                {value}
            </div>

            <div class="insight-desc">
                {text}
            </div>

        </div>

    </div>
    """

    render_html(html)

def feature_card(title, description, icon):

    icon_map = {
        "chart":"bi bi-bar-chart-line-fill",
        "target":"bi bi-bullseye",
        "salary":"bi bi-cash-stack",
        "info":"bi bi-info-circle-fill",
    }

    html=f"""
    <div class="feature-card fade-in">

        <div class="feature-icon-wrapper">

            <i class="{icon_map.get(icon,'bi bi-circle')}"></i>

        </div>

        <div class="feature-title">{title}</div>

        <div class="feature-desc">

            {description}

        </div>

    </div>
    """

    render_html(html)


def recommendation_card(career, score, salary, demand, growth, matched_skills,missing_skills,countries, explanation):
    """
    Renders a beautiful matching recommendation card on the Advisor page, including target countries.
    """
    formatted_salary = f"${salary:,.0f}" if isinstance(salary, (int, float)) else salary
    skills_html = "".join([f'<span class="skill-pill">{skill}</span>' for skill in matched_skills]) if matched_skills else '<span class="skill-pill" style="background-color: #FEE2E2; color: #EF4444; border-color: #FCA5A5;">No matching skills</span>'
    missing_skills_html = "".join([
        f'<span class="skill-pill missing-skill">{skill}</span>'
        for skill in missing_skills
    ]) if missing_skills else """
<span class="skill-pill learned-skill">
    All key skills covered
</span>
"""
    countries_str = ", ".join(countries) if isinstance(countries, list) else countries
    why_points = "".join([f'<li style="margin-bottom: 6px; font-size: 14px; color: var(--text-secondary);">{point}</li>' for point in explanation])
    
    html = f"""
    <div class="rec-card fade-in">
        <div class="rec-title-row">
            <span class="rec-title">{career}</span>
            <span class="rec-score-pill">Overall Match: {score:.1f}%</span>
        </div>
        <div class="rec-score-track">
            <div class="rec-score-fill" style="width: {min(max(score, 0), 100):.1f}%;"></div>
        </div>
        <div class="rec-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); gap: 12px; padding: 12px 0;">
            <div class="rec-grid-item">
                <div class="rec-grid-label">Average Salary</div>
                <div class="rec-grid-value" style="white-space: nowrap;">{formatted_salary}</div>
            </div>
            <div class="rec-grid-item">
                <div class="rec-grid-label">Demand Score</div>
                <div class="rec-grid-value" style="white-space: nowrap;">{demand:.1f}/100</div>
            </div>
            <div class="rec-grid-item">
                <div class="rec-grid-label">Projected Growth</div>
                <div class="rec-grid-value" style="white-space: nowrap;">{growth:.1f}%</div>
            </div>
            <div class="rec-grid-item">
                <div class="rec-grid-label">Top Countries</div>
                <div class="rec-grid-value" style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="{countries_str}">{countries_str}</div>
            </div>
        </div>
        <div style="margin-bottom:20px;">

            <div class="rec-grid-label" style="margin-bottom:8px;">
                ✓ Skills You Have
            </div>

            <div class="skills-container" style="margin-bottom:18px;">
                {skills_html}
            </div>

            <div class="rec-grid-label" style="margin-bottom:8px;">
                ⚠ Skills to Learn
            </div>

            <div class="skills-container">
                {missing_skills_html}
            </div>

        </div>
        </div>
        <div class="why-rec-box">
            <div class="why-rec-title">
                 <i class="bi bi-lightbulb-fill"></i> Why this recommendation?
            </div>
            <ul style="margin: 0; padding-left: 20px; color: var(--text-secondary);">
                {why_points}
            </ul>
        </div>
    </div>
    """
    render_html(html)

def footer():
    """
    Renders an empty spacing placeholder to satisfy the footer function call
    without rendering any visible footer text.
    """
    st.markdown('<div style="margin-top: 32px;"></div>', unsafe_allow_html=True)