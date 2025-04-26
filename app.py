
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

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
    st.title("모의 평가")
    
    evaluator_id = st.text_input("평가자 ID")
    st.write("다음 항목들에 대해 평가를 진행해주세요. (1: 매우 미흡, 5: 매우 우수)")
    
    score1 = st.slider("업무 수행 능력", 1, 5, 3)
    score2 = st.slider("의사소통 능력", 1, 5, 3)
    score3 = st.slider("팀워크", 1, 5, 3)
    score4 = st.slider("리더십", 1, 5, 3)
    
    comments = st.text_area("종합 의견")
    
    if st.button("평가 제출"):
        if evaluator_id:
            new_evaluation = pd.DataFrame({
                '평가자ID': [evaluator_id],
                '평가일시': [datetime.now()],
                '평가점수': [(score1 + score2 + score3 + score4) / 4],
                '코멘트': [comments]
            })
            st.session_state.evaluations = pd.concat([st.session_state.evaluations, new_evaluation], ignore_index=True)
            st.success("평가가 제출되었습니다!")
        else:
            st.error("평가자 ID를 입력해주세요.")

elif page == "평가자 분석":
    st.title("평가자 분석")
    
    if not st.session_state.evaluations.empty:
        evaluator_id = st.selectbox(
            "평가자 선택",
            options=st.session_state.evaluations['평가자ID'].unique()
        )
        
        evaluator_data = st.session_state.evaluations[
            st.session_state.evaluations['평가자ID'] == evaluator_id
        ]
        
        if not evaluator_data.empty:
            tendency, feedback = analyze_evaluator(evaluator_data['평가점수'])
            
            st.subheader("평가 성향 분석")
            st.write(f"**평가 경향:** {tendency}")
            st.write(f"**피드백:** {feedback}")
            
            # 평가 점수 추이 그래프
            fig = px.line(evaluator_data, x='평가일시', y='평가점수', 
                         title='평가 점수 추이')
            st.plotly_chart(fig)
    else:
        st.info("아직 평가 데이터가 없습니다.")

else:  # 관리자 대시보드
    st.title("관리자 대시보드")
    
    if not st.session_state.evaluations.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("평가자별 평균 점수")
            avg_scores = st.session_state.evaluations.groupby('평가자ID')['평가점수'].mean()
            fig1 = px.bar(avg_scores, title='평가자별 평균 점수')
            st.plotly_chart(fig1)
        
        with col2:
            st.subheader("전체 평가 분포")
            fig2 = px.histogram(st.session_state.evaluations, x='평가점수', 
                              title='평가 점수 분포')
            st.plotly_chart(fig2)
        
        st.subheader("최근 평가 기록")
        st.dataframe(st.session_state.evaluations.sort_values('평가일시', ascending=False))
    else:
        st.info("아직 평가 데이터가 없습니다.")
