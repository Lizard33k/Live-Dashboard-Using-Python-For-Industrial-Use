

import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import plotly.express as px
import plotly.graph_objects as go



#Loading the Dataset

df = pd.read_excel("/home/lizard/Downloads/Project_1/sample 2.xlsx")
df2 = df.iloc[:,[7,8,9]]

######Setting up the page in local webhost
st.set_page_config(page_title='Sales',layout='wide')
padding_top = 0

st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            padding-top: {padding_top}rem;
        }}
    </style>""",
    unsafe_allow_html=True,
)

######Creating the Dropdown Menu
option = st.sidebar.selectbox('LINE LEVEL',('STAMPER', 'BOSCH', 'CPM'))

#####Creating the Half Circle Chart for the Sidebar



#Creating two side by side elements in sidebar
col1, col2 = st.sidebar.columns(2)
with col1:
    st.header("Line OEE")
    # data
    label = ["A", "B", "C"]
    val = [2,2,2]

    # append data and assign color
    label.append("")
    val.append(sum(val))  # 50% blank
    colors = ['#3D6FC9','#579BDB','#F9C200','white']

     #plot
    fig = plt.figure(figsize=(8,6),dpi=100)
    fig.set_facecolor('#F0F2F6')
    ax = fig.add_subplot(1,1,1)
    ax.pie(val, labels=label, colors=colors)
    ax.add_artist(plt.Circle((0, 0), 0.6, color='white'))
    
    st.pyplot(fig)
  



with col2:
    st.header("Breakdown")
   

####Creating the Pie Chart for the sidebar
 # Creating dataset
    cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES']
 
    data = [23, 17, 35, 29, 12, 41]
    fig_pie_sidebar = plt.figure(figsize =(3,3),dpi=500,edgecolor='green')
    fig_pie_sidebar.tight_layout()
    fig_pie_sidebar.set_facecolor('#F0F2F6')
    colors = ['#3D6FC9','#579BDB','#F9C200','#A2A2A2','#F48138']
    plt.pie(data,colors=colors)
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='center right',prop={'size':5},labels=cars)
    st.sidebar.header("Machine Loss Contribution")
    st.sidebar.pyplot(fig_pie_sidebar)


#####Creating the Barchart for the side bar

data = {'C':20, 'C++':15, 'Java':30,
        'Python':35}
courses = list(data.keys())
values = list(data.values())
  
fig3 = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='#3D6FC9',
        width = 0.4)
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
st.sidebar.header("Hourly Production")
st.sidebar.pyplot(fig3)
 
# creating the bar plot

#########
with st.container():
    
    st.write("Machine Level")
###### Creating side by side pie chart and Table in a empty container

with st.container():
    col1, col2,col3 = st.columns(3)
    with col1:
        
        st.header("Stamper Loss Capturing")
        # Creating dataset
        cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES']
 
        data = [23, 17, 35, 29, 12, 41]
        fig9 = plt.figure(figsize =(3,3),dpi=1000)
        
        colors = ['#3D6FC9','#579BDB','#F9C200','#A2A2A2','#F48138']
        plt.pie(data,colors=colors)
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc=5,prop={'size':4},labels=cars)


        st.pyplot(fig9)

    with col2:
        stop_type= ['Manual Stop','machine Stop','Upload']
        rand_value1 = [5, 6,7]
        rand_value2 = [5, 6,7]
        figT= go.Figure(data= go.Table(header=dict(values=['Minor Stop Details', 'Frequency','Time Lost (Hr)']),cells=dict(values=[stop_type,rand_value1,rand_value2])))
        st.write(figT)
    with col3:
        
     
        pass
        

##########Creating Line Chart and Tabe in a empty Container
with st.container():
    col1, col2,col3 = st.columns(3)
    with col1:
        
            Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
            Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
            fig4 = plt.figure(figsize = (8, 5))
            plt.plot(Year,Unemployment_Rate)
            st.pyplot(fig4)
        
           

    with col2:
        stop_type= ['Manual Stop','machine Stop','Upload']
        rand_value1 = [5, 6,7]
        rand_value2 = [5, 6,7]
        figT= go.Figure(data= go.Table(header=dict(values=['Minor Stop Details', 'Frequency','Time Lost (Hr)']),cells=dict(values=[stop_type,rand_value1,rand_value2])))
        st.write(figT)
    with col3:
        pass
###### Creating a bar chart with very little space between two bars

###### Creating a bar chart with very little space between two bars
with st.empty():
    ata = {'C':20, 'C++':15, 'Java':30,
        'Python':35}
    courses1 = list(ata.keys())
    values1 = list(ata.values())
  
    fig8 = plt.figure(figsize = (9, 3))
 
# creating the bar plot
    plt.bar(courses1, values1, color ='#3D6FC9',width = 0.4)
 
    plt.xlabel("Courses offered")
    plt.ylabel("No. of students enrolled")
    plt.title("Students enrolled in different courses")
    
    st.pyplot(fig8)

# creating the bar plot
