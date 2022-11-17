import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 


# read csv from a github repo



st.set_page_config(
    page_title = 'Real-Time Data Science Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Real-Time / Live Data Science Dashboard")

# top-level filters 
st.write("Hello")
option = st.selectbox('LINE LEVEL',('STAMPER', 'BOSCH', 'CPM'))


# creating a single-element container.
placeholder = st.empty()

for seconds in range(200):
#while True: 
    
 
    

    with placeholder.container():
        if option== "STAMPER":
            st.write("stamper")
        if option== "BOSCH":
            st.write("working")
        
        # create three columns
        
        
        time.sleep(1)
    #placeholder.empty()

# dataframe filter 



# near real-time / live feed simulation 
