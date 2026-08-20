import streamlit as st
import textwrap
import pandas as pd
from ui.components import recommendation_card, page_header, footer

def show_advisor(jobs, advisor_skills):
    page_header(
        "Career Advisor",
        "Select your technical skills to discover the AI career path that best matches your professional profile."
    )
    
    st.markdown('<div class="spacer-32"></div>', unsafe_allow_html=True)
    
    col_input, col_results = st.columns([1, 1.8])
    
    with col_input:
        st.markdown('<h3 style="margin-top: 0;">Skill Profile</h3>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 14px; margin-bottom: 16px;">Add the technical skills you currently possess or wish to acquire.</p>', unsafe_allow_html=True)
        
        # Curated list of skills a person actually holds (advisor_skills.csv), not
        # every raw token scraped into skills_required (junk domains, ".NET", etc.)
        all_skills = sorted(advisor_skills["Skill"].unique())

        experience = st.selectbox("Experience Level", sorted(jobs["experience_tier"].unique()))
        
        selected_skills = st.multiselect(
            "Select your technical skills",
            all_skills,
            placeholder="Choose one or more skills...",
            label_visibility="collapsed"
        )
        
        st.markdown('<div style="margin-top: 16px;"></div>', unsafe_allow_html=True)
        find_clicked = st.button("Find Matching Jobs", type="primary")
        
        st.markdown(
            textwrap.dedent("""
            <div class="why-rec-box" style="margin-top: 24px;">
                <div class="why-rec-title" style="font-size: 14px;">
                    <i class="bi bi-lightbulb-fill"></i> Pro-Tip for Better Matches
                </div>
                <p style="font-size: 13px; line-height: 1.5; margin: 0; color: var(--text-secondary);">
                Technology employers value a combination of programming languages (Python, Java, SQL), data skills, cloud technologies, and analytical tools. Selecting 3–5 relevant skills generally produces the most accurate job recommendations.
                </p>
            </div>
            """).strip(),
            unsafe_allow_html=True
        )

    with col_results:
        st.markdown('<h3 style="margin-top: 0;">Recommended Jobs</h3>', unsafe_allow_html=True)
        
        if find_clicked:
            if len(selected_skills) == 0:
                st.warning("Please select at least one technical skill.")
            else:
                # Case-insensitive comparison so a curated label like "Power BI"
                # still matches however it happens to be cased in the job data.
                selected_skills_lower = {skill.lower() for skill in selected_skills}

                recommendations = []
                filtered_jobs = jobs[jobs["experience_tier"] == experience]
                for _, job in filtered_jobs.iterrows():
                    job_skills = [skill.strip() for skill in job["skills_required"].split(",") if skill.strip() != ""]
                    job_skills_lower = {skill.lower() for skill in job_skills}

                    matched_skills = [skill for skill in selected_skills if skill.lower() in job_skills_lower]
                    match_score = (len(matched_skills) / len(selected_skills)) * 100
                    if match_score < 45:
                        continue

                    missing_skills = [skill for skill in job_skills if skill.lower() not in selected_skills_lower]
                    recommendations.append({

                        "job_title": job["job_title"],

                        "company": job["company_name"],

                        "city": job["primary_city"],

                        "experience": job["experience_tier"],

                        "score": round(match_score,1),

                        "gap": round(100-match_score,1),

                        "matched": matched_skills,

                        "missing": missing_skills[:5]})
                recommendations = sorted(recommendations,key=lambda x: x["score"],reverse=True)
                if len(recommendations) == 0:
                    st.warning(
                        """
                         No strong matches found.
                        Try selecting additional skills or a different experience level.
                        """)
                else:
                    for rec in recommendations[:5]:
                        with st.container(border=True):
                            st.subheader(rec["job_title"])
                            st.markdown(f"**Company:** {rec['company']}")
                            st.markdown(f"**City:** {rec['city']}")
                            st.markdown(f"**Experience:** {rec['experience']}")
                            st.markdown(f"**Match Score:** {rec['score']}%")
                            st.markdown(f"**Skill Gap:** {rec['gap']}%")
                            st.markdown(f"**Matched Skills:** {', '.join(rec['matched']) if rec['matched'] else '—'}")
                            st.markdown(f"**Missing Skills:** {', '.join(rec['missing']) if rec['missing'] else '—'}")
        else:
            # Default helper message before search is run
            st.markdown(
                textwrap.dedent("""
                <div style="border: 2px dashed var(--border); border-radius: var(--radius); padding: 48px; text-align: center; color: var(--text-secondary);" class="fade-in">
                    <i class="bi bi-bullseye" style="font-size: 40px; display: block; margin-bottom: 16px; color: var(--primary);"></i>
                    <h4 style="margin: 0 0 8px 0; color: var(--text); font-weight: 600;">No Search Run Yet</h4>
                    <p style="margin: 0; font-size: 15px;">Configure your technical skills in the left profile panel and click <strong>"Find Matching Careers"</strong> to view personalized career recommendations.</p>
                </div>
                """).strip(),
                unsafe_allow_html=True
            )
            
    footer()