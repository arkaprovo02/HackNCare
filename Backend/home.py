import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import json
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def app():
    st.markdown("<h1 style='text-align: center; color: white;'>WE CARE</h1>", unsafe_allow_html=True)
    lottie_home = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_x1gjdldd.json")
    st_lottie(lottie_home)
    st.subheader("About the project.")
    st.text("The app is a Healthcare app and it's purpose is to detect dieseases according to test results as early as possible. This app also contains an exercise section where the user can do exercise and take a look at the calories burnt displayed on the screen along with the count of the exercise.")
    st.subheader("Name of Contributers.")
    st.text("1. AYUSH ROY")
    st.text("1. RITWIK HALDER")
    st.text("1. ARKAPROVO ACHARYA")
    st.snow()