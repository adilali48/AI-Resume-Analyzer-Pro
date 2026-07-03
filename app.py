import streamlit as st

def load_css():

    with open("assets/style.css") as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True

        )

report = ""
job_report = ""
improved_resume = ""
letter = ""
questions = ""

from cover_letter import CoverLetterGenerator
from resume_rewriter import ResumeRewriter
from skill_gap import SkillGapAnalyzer
from resume_parser import ResumeParser
from ai_analyzer import AIAnalyzer
from ats_score import ATSScore
from dashboard import Dashboard
from job_match import JobMatcher
from interview import InterviewGenerator
from report_generator import PDFReport

# ------------------------------------------------
# Page Config
# ------------------------------------------------

st.markdown("""

<div class="card">

<h1>🚀 AI Resume Analyzer Pro</h1>

<p style="text-align:center;color:#CBD5E1;">

Your Personal AI Career Assistant

</p>

</div>

""", unsafe_allow_html=True)

load_css()

# ------------------------------------------------
# Objects
# ------------------------------------------------

parser = ResumeParser()
ai = AIAnalyzer()
ats = ATSScore()
dashboard = Dashboard()
matcher = JobMatcher()
gap = SkillGapAnalyzer()
rewriter = ResumeRewriter()
cover = CoverLetterGenerator()
interview = InterviewGenerator()
pdf_report = PDFReport()


# ------------------------------------------------
# Session State
# ------------------------------------------------

if "report" not in st.session_state:
    st.session_state.report = ""

if "job_report" not in st.session_state:
    st.session_state.job_report = ""

if "improved_resume" not in st.session_state:
    st.session_state.improved_resume = ""

if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""

if "interview_questions" not in st.session_state:
    st.session_state.interview_questions = ""

# ------------------------------------------------
# Sidebar
# ------------------------------------------------

st.sidebar.title("🚀 AI Resume Analyzer")

st.sidebar.markdown("---")

st.sidebar.success("📄 Resume Upload")
st.sidebar.success("🤖 AI Analysis")
st.sidebar.success("📊 ATS Score")
st.sidebar.success("🎯 Job Match")
st.sidebar.success("📈 Skill Gap")
st.sidebar.success("✨ Resume Rewriter")
st.sidebar.success("📄 Cover Letter")
st.sidebar.success("🎤 Interview Coach")
st.sidebar.success("📥 PDF Report")

st.sidebar.markdown("---")

st.sidebar.info("Powered by Groq AI")

# Resume Upload
uploaded_resume = st.sidebar.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx"]
)



# ------------------------------------------------
# Header
# ------------------------------------------------

st.title("🚀 AI Resume Analyzer Pro")

st.markdown("""
Analyze your resume using Artificial Intelligence.

### Features

- 📄 Resume Parsing
- 🤖 AI Resume Analysis
- 📊 ATS Score
- 💪 Strengths
- ⚠ Weaknesses
- 🎯 Missing Skills
- 💼 Recommended Job Roles
- 📈 Job Match Analysis
""")

st.divider()

# ------------------------------------------------
# Resume Upload
# ------------------------------------------------

uploaded_resume = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx"]
)

# ------------------------------------------------
# Job Description
# ------------------------------------------------

st.subheader("💼 Job Description (Optional)")

job_description = st.text_area(
    "Paste the Job Description",
    height=220,
    placeholder="Paste the complete Job Description here..."
)

# ------------------------------------------------
# Resume Processing
# ------------------------------------------------

if uploaded_resume:

    with st.spinner("📄 Reading Resume..."):

        resume_text = parser.extract_text(uploaded_resume)

    st.success("✅ Resume Loaded Successfully!")

    score = ats.calculate(resume_text)

    # ------------------------------------------------
    # Dashboard
    # ------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📊 ATS Score",
            f"{score}/100"
        )

    with col2:
        st.metric(
            "📄 Words",
            len(resume_text.split())
        )

    with col3:
        st.metric(
            "📝 Characters",
            len(resume_text)
       )

    with col4:
        st.metric(
            "🤖 AI Model",
            "Groq"
       )

    st.plotly_chart(
        dashboard.ats_gauge(score),
        use_container_width=True
    )
    st.divider()
    # ------------------------------------------------
    # Resume Preview
    # ------------------------------------------------

    with st.expander("📄 Resume Preview"):

        st.text_area(
            "Extracted Resume",
            resume_text,
            height=350
        )

    st.divider()

    # ------------------------------------------------
    # AI Resume Analysis
    # ------------------------------------------------

    if st.button(
        "🚀 Analyze Resume",
        use_container_width=True
    ):

        with st.spinner("🤖 AI is analyzing your resume..."):

           st.session_state.report = ai.analyze(resume_text)

        st.success("✅ Resume Analysis Complete")

        st.subheader("📋 AI Resume Report")

        st.markdown(st.session_state.report)

    # ------------------------------------------------
    # Job Match Analysis
    # ------------------------------------------------

    if job_description.strip():

        if st.button(
            "🎯 Calculate Job Match",
            use_container_width=True
        ):

            with st.spinner("🤖 Comparing Resume with Job Description..."):

                st.session_state.job_report = matcher.analyze(
                    resume_text,
                    job_description
               )

            st.success("✅ Job Match Analysis Completed")

            st.subheader("🎯 Job Match Report")

            st.markdown(st.session_state.job_report)

            # ----------------------------------------
            # Skill Gap Analysis
            # ----------------------------------------

            found, missing, percent = gap.analyze(
                resume_text,
                job_description
            )

            st.divider()

            st.subheader("📊 Skill Gap Analysis")

            st.progress(percent / 100)

            st.metric(
                "Skills Match",
                f"{percent}%"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.success("✅ Skills Found")

                if found:
                    for skill in found:
                        st.write(f"✔ {skill}")
                else:
                    st.write("No matching skills found.")

            with col2:

                st.error("❌ Missing Skills")

                if missing:
                    for skill in missing:
                        st.write(f"✘ {skill}")
                else:
                    st.write("No missing skills detected.")

    st.divider()

    # ------------------------------------------------
    # Resume Rewriter
    # ------------------------------------------------

    if st.button(
        "✨ Improve Resume",
        use_container_width=True
    ):

        with st.spinner("✍ AI is rewriting your resume..."):

            st.session_state.improved_resume = rewriter.rewrite(
                resume_text
            )

        st.success("✅ Resume Improved Successfully!")

        st.subheader("✨ ATS Optimized Resume")

        st.markdown(st.session_state.improved_resume)

        st.download_button(
            "📥 Download Improved Resume",
            st.session_state.improved_resume,
            file_name="Improved_Resume.md",
            mime="text/markdown"
        )

    st.divider()

    # ------------------------------------------------
    # Cover Letter Generator
    # ------------------------------------------------

    if job_description.strip():

        if st.button(
            "📄 Generate Cover Letter",
            use_container_width=True
        ):

            with st.spinner("📝 Writing Cover Letter..."):

                st.session_state.cover_letter = cover.generate(
                    resume_text,
                    job_description
                )

            st.success("✅ Cover Letter Generated!")

            st.subheader("📄 AI Cover Letter")

            st.markdown(st.session_state.cover_letter)

            st.download_button(
                "📥 Download Cover Letter",
                st.session_state.cover_letter,
                file_name="Cover_Letter.md",
                mime="text/markdown"
            )
    st.divider()

if st.button(
    "🎤 Generate Interview Questions",
    use_container_width=True
):

    with st.spinner("Preparing Interview Questions..."):

        st.session_state.interview_questions = interview.generate(
            resume_text,
            job_description
        )

    st.success("Interview Questions Generated!")

    st.subheader("🎤 AI Interview Preparation")

    st.markdown(st.session_state.interview_questions)

    st.download_button(
        "📥 Download Interview Questions",
        st.session_state.interview_questions,
        file_name="Interview_Questions.md",
        mime="text/markdown"
    )
            



# ------------------------------------------------
# PDF Report
# ------------------------------------------------

if st.button(
    "📥 Generate Full PDF Report",
    use_container_width=True
):

    sections = [

        ("ATS Score", str(score)),

        ("Resume Analysis", report),

        ("Job Match", job_report),

        ("Resume Improvement", improved_resume),

        ("Cover Letter", letter),

        ("Interview Questions", questions)

    ]

    pdf_report.generate(
        "Resume_Report.pdf",
        sections
    )

    with open(
        "Resume_Report.pdf",
        "rb"
    ) as f:

        st.download_button(
            "⬇ Download Report",
            f,
            file_name="Resume_Report.pdf",
            mime="application/pdf"
        )
    st.markdown("""
    ---
    <center>

    ### 🚀 AI Resume Analyzer Pro

    Built with ❤️ using

    **Streamlit • Groq • LangChain • Plotly**

    © 2026 Adil Ali

    </center>
    """, unsafe_allow_html=True)
