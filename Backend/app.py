import heart
import kidney
import exercise
import diabetes
import medicine
import home
import streamlit as st


PAGES = {
    "Home": home,
    "Heart Diesease Detection": heart,
    "Kidney Diesease Detection": kidney,
    "Diabetes Diesease Detection": diabetes,
    "Exercise": exercise,
    "Medicine Notification": medicine
}
st.sidebar.title('NAVIGATION')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()