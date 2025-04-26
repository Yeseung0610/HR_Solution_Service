import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from pages import (
    evaluation as page_evaluation,
    analysis as page_analysis,
    dashboard as page_dashboard
)

# Page configuration
st.set_page_config(page_title="HR 평가자 분석 시스템", layout="wide")

# Initialize session state
if 'evaluations' not in st.session_state:
    st.session_state.evaluations = pd.DataFrame(columns=['평가자ID', '평가일시', '평가점수', '코멘트'])

def analyze_evaluator(scores):
    mean_score = scores.mean()
    if mean_score > 4.0:
        return "관대화 경향", "평가 점수가 전반적으로 높은 편입니다. 더 객관적인 평가를 위해 평가 기준을 재검토해보세요."
    elif mean_score < 2.0:
        return "가혹화 경향", "평가 점수가 전반적으로 낮은 편입니다. 피평가자의 긍정적인 면도 함께 고려해보세요."
    else:
        return "균형적 평가", "비교적 균형잡힌 평가를 하고 있습니다. 지금의 객관성을 유지하세요."

# Sidebar navigation
st.sidebar.title("HR 평가 지원 시스템")
page = st.sidebar.radio("메뉴", ["모의 평가", "평가자 분석", "관리자 대시보드"])

if page == "모의 평가":
    page_evaluation.show()
elif page == "평가자 분석":
    page_analysis.show()
else:
    page_dashboard.show()