
import streamlit as st
import pandas as pd
from datetime import datetime

def show():
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
