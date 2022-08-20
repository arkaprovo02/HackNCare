import streamlit as stream
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import json
import requests
import datetime
import pandas as pd

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def df_to_csv():
    
    fd = open("med_record.json",'r')
    txt = fd.read()
    fd.close()
    rec = json.loads(txt)
    zer = 0
    if '0' in rec:
        del rec['0']
    df = pd.DataFrame(rec).transpose()
    df1 = df.astype(str)
    nan_value = float("NaN")
    df1.replace("", nan_value, inplace=True)
    df1.dropna(inplace=True)

    df1.to_csv('file1.csv') # dataframe to CSV file 


def app():

    fd = open("med_record.json",'r')
    sl = fd.read()
    fd.close()
    info = json.loads(sl)

    stream.markdown("<h1 style='text-align: center; color: white;'>MEDICINE NOTIFICATION</h1>", unsafe_allow_html=True)
    lottie_med = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_tutvdkg0.json")
    st_lottie(lottie_med)

    with stream.form(key = 'forml'):
        pid = len(info) + 1
        email = stream.text_input("Enter EMAIL ID")
        medicine = stream.text_input("Write the name of medicines prescribed by the doctor")
        time  = stream.time_input("Specify the timing of taking the medicine", datetime.time(00, 00)) 
        time = str(time)
        #time = time[:len(time)-3]
        submit_button = stream.form_submit_button(label = 'Confirm')

    if submit_button:
        stream.success("Info added")

    info[pid] = {'Medicine' : medicine, 'time': time, 'Email' : email}

    js = json.dumps(info)
    fd = open("med_record.json",'w')
    fd.write(js)
    fd.close()

    df_to_csv()
