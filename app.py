import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Keşfet Ya Da Tahminde Bulun" , ("Maaş Tahmini" , "Keşfet"))    # kenar çubuğu oluşturduk

if page == "Maaş Tahmini":
    show_predict_page()
else:
    show_explore_page()




# conda activate ml
# streamlit run app.py