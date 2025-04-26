
import streamlit as st
import plotly.express as px
from utils.analysis import analyze_evaluator

def show():
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
            
            fig = px.line(evaluator_data, x='평가일시', y='평가점수', 
                         title='평가 점수 추이')
            st.plotly_chart(fig)
    else:
        st.info("아직 평가 데이터가 없습니다.")
