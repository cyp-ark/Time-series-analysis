import streamlit as st
import EDA
import reg
import stock

def sidebar_nagivation():
    st.sidebar.title('Navigation')
    if st.sidebar.button('EDA'):
        st.session_state["session"]="EDA"
    if st.sidebar.button('Stock'):
        st.session_state["session"]="Stock"
    if st.sidebar.button('Regression'):
        st.session_state["session"]="Regression"
        
    
    st.sidebar.title('Options')

def run():
    st.set_page_config(layout='wide')
    
    # 사이드바 네비게이션
    sidebar_nagivation()
    
    if st.session_state.get("session","Stock") == "Stock":
        stock.main()
    elif st.session_state["session"] == "EDA":
        EDA.main()
    elif st.session_state["session"] == "Regression":
        reg.main()
    
if __name__ == "__main__":
    run()