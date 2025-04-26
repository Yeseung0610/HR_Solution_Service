
import streamlit as st
import plotly.express as px

def show():
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
