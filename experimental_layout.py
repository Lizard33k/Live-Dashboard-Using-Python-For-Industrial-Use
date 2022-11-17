from enum import unique
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import plotly.express as px
import plotly.graph_objects as go
import time # to simulate a real time data, time loop
st.set_page_config(page_title='Live Machine Performance Dashboard',layout='wide')
a= st.number_input("SKU", min_value=100, max_value=125, value= 125)
if a==100:
    SKU= 90;
    ton1=101;
if a== 125:
    SKU= 84;
    ton1=95.25;
    
    
option = st.selectbox('MACHINE LEVEL',('L4- STAMPER', 'L4- BOSCH1','L4- BOSCH2', 'L4- CPM1','L4- CPM2','Line 6'))

##SKU= st.sidebar.selectbox('SKU', ('Wheel 125g', 'Wheel 100g'))
from datetime import datetime



placeholder_container1 = st.empty()


for seconds in range(200):
#while True: 

    with placeholder_container1.container():
        df_stamper= pd.read_csv("L4Stamper.csv")
        df_stamper_without_dash = df_stamper.iloc[1:]
               
        df_CPM1= pd.read_csv("L4CPM1.csv")
        df_CPM1_without_dash = df_CPM1.iloc[1:]
        
        df_CPM2= pd.read_csv("L4CPM2.csv")
        df_CPM2_without_dash = df_CPM2.iloc[1:]

        df_BOSCH1= pd.read_csv("L4BOSCH1.csv")
        df_BOSCH1_without_dash = df_BOSCH1.iloc[1:]
        
        df_BOSCH2= pd.read_csv("L4BOSCH2.csv")
        df_BOSCH2_without_dash = df_BOSCH2.iloc[1:]
        
        
      

        # create two columns for charts 

        fig_col1, fig_col2, fig_col3 = st.columns([0.75,1,2],gap="small")
        
        
        
        
        with fig_col1:
           ############TOTAL FBC LINE 6 
#             if option =="Line 6":  
#                 df_LINE_CSV = pd.read_csv("Line.csv")
#                 df_line_csv_without_dash_for_machine_status_6 = df_LINE_CSV.iloc[1,:]
#                 line_tot = pd.to_numeric(df_line_csv_without_dash_for_machine_status_6["TOTAL_FBC               "])
#                 line_tot= line_tot.astype(int)
#                 ton6= line_tot/101
#                 ton= round(ton,2)
#                 line_tot= line_tot.astype(str)
#                 ton= ton.astype(str)
#                 st.markdown(f'<h2 style="color: "darkslategrey"; font-size:20px;" align="center">{"FBC:    " +line_tot}</h2>', unsafe_allow_html=True)
#                 st.markdown(f'<h2 style="color: "darkslategrey"; font-size:20px;" align="center">{"Ton:    " +ton6}</h2>', unsafe_allow_html=True)
                
            if option=="Line 6":
                ####################FOR TOTAL FBC 
                df_LINE6_CSV = pd.read_csv("Line6.csv")
                df_line6_csv_without_dash_for_machine_status = df_LINE6_CSV.iloc[1,:]
                line6_tot = pd.to_numeric(df_line6_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                line6_tot= line6_tot.astype(int)
                ton6= line6_tot/101
                ton6= round(ton6,2)
                line6_tot= line6_tot.astype(str)
                ton6= ton6.astype(str)
                #st.markdown(f'<h1 style="color: "#D9911A"; font-size:20px;" align="center">{"FBC"}</h1>', unsafe_allow_html=True)
                st.markdown(f'<h2 style="color: "darkslategrey"; font-size:20px;" align="center">{"FBC:    " +line6_tot}</h2>', unsafe_allow_html=True)
                st.markdown(f'<h2 style="color: "darkslategrey"; font-size:20px;" align="center">{"Ton:    " +ton6}</h2>', unsafe_allow_html=True)
                
                def line_oee(oee):
                    lizard_007 = go.Figure(go.Indicator(
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    value = oee*100, #put line OEE here. 
                    mode = "gauge+number+delta",
                    title = {'text': "LINE OEE"},
                    delta = {'reference': 70},
                    gauge = {'axis': {'range': [0, 100]},

                             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 70}}))
                    lizard_007.update_layout(
                    autosize=False,

                    width=290,
                    height=320,
                    margin_l=0,
                    margin_b=0,
                    margin_t=0
                )

                    st.write(lizard_007)
                line_csv = pd.read_csv("Line6.csv")
                line_csv_without_dash = line_csv.iloc[1:,:]
                dt3 = datetime.strptime('2021-10-20 06:00:48.00000', "%Y-%m-%d %H:%M:%S.%f")
                dt_line =line_csv_without_dash._get_value(1,0, takeable = True)
                line_time = datetime.strptime(dt_line, "%Y-%m-%d %H:%M:%S.%f")

                line_time_diff=round(((line_time-dt3).seconds)/60)
                if line_time_diff<480:
                    fbc= line_csv_without_dash._get_value(1,3, takeable = True)
                    fbc = float(fbc)
                    oee=(fbc*72)/(458*line_time_diff)
                    line_oee(oee)

                if line_time_diff>480 and line_time_diff<960:
                    fbc= line_csv_without_dash._get_value(1,3, takeable = True)
                    fbc = float(fbc)
                    oee=(fbc*72)/(458*(line_time_diff-480))
                    line_oee(oee)



                if line_time_diff>960:
                    fbc= line_csv_without_dash._get_value(1,3, takeable = True)
                    fbc = float(fbc)
                    oee=(fbc*72)/(458*(line_time_diff-960))
                    line_oee(oee)

                

                
        ############################################################################################################### ALL LINES START

            if option=="L4- CPM1" or option=="L4- CPM2" or option== "L4- BOSCH1" or option=="L4- BOSCH2" or option=="L4- STAMPER":
        ####################FOR TOTAL FBC 
                df_LINE_CSV = pd.read_csv("Line.csv")
                df_line_csv_without_dash_for_machine_status = df_LINE_CSV.iloc[1,:]
                line_tot = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                line_tot= line_tot.astype(int)
                ton= line_tot/ton1
                ton= round(ton,2)
                line_tot= line_tot.astype(str)
                ton= ton.astype(str)


                #st.markdown(f'<h1 style="color: "#D9911A"; font-size:20px;" align="center">{"FBC"}</h1>', unsafe_allow_html=True)
                st.markdown(f'<h2 style="color: "darkslategrey"; font-size:20px;" align="center">{"FBC:    " +line_tot}</h2>', unsafe_allow_html=True)
                st.markdown(f'<h2 style="color: "darkslategrey"; font-size:20px;" align="center">{"Ton:    " +ton}</h2>', unsafe_allow_html=True)
#################################### FUNCTION FOR LINE OEE
                def line_oee(oee):
                    lizard_007 = go.Figure(go.Indicator(
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    value = oee*100, #put line OEE here. 
                    mode = "gauge+number+delta",
                    title = {'text': "LINE OEE"},
                    delta = {'reference': 70},
                    gauge = {'axis': {'range': [0, 100]},

                             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 70}}))
                    lizard_007.update_layout(
                    autosize=False,

                    width=290,
                    height=320,
                    margin_l=0,
                    margin_b=0,
                    margin_t=0
                )

                    st.write(lizard_007)
                line_csv = pd.read_csv("Line.csv")
                line_csv_without_dash = line_csv.iloc[1:,:]
                dt3 = datetime.strptime('2021-10-20 06:00:48.00000', "%Y-%m-%d %H:%M:%S.%f")
                dt_line =line_csv_without_dash._get_value(1,0, takeable = True)
                line_time = datetime.strptime(dt_line, "%Y-%m-%d %H:%M:%S.%f")

                line_time_diff=round(((line_time-dt3).seconds)/60)
                if line_time_diff<480:
                    fbc= line_csv_without_dash._get_value(1,3, takeable = True)
                    fbc = float(fbc)
                    oee=(fbc*SKU)/(440*line_time_diff)
                    line_oee(oee)

                if line_time_diff>480 and line_time_diff<960:
                    fbc= line_csv_without_dash._get_value(1,3, takeable = True)
                    fbc = float(fbc)
                    oee=(fbc*SKU)/(440*(line_time_diff-480))
                    line_oee(oee)



                if line_time_diff>960:
                    fbc= line_csv_without_dash._get_value(1,3, takeable = True)
                    fbc = float(fbc)
                    oee=(fbc*SKU)/(440*(line_time_diff-960))
                    line_oee(oee)


            

            
            
            
#################################################################################################################################################################################################################################################
            #fig_bar = go.Figure([go.Bar(x=oee, y=[20, 14, 23])])
            def fault_time(file_name):
                    cpm1_fault = pd.read_csv(file_name)
                    
                    top5_fault = cpm1_fault.iloc[1:10,3:4]
                    fault_freq = cpm1_fault.iloc[1:10,4:5]
                    
  
                    figT= go.Figure(data= go.Table(header=dict(values=['Minor Stop Details', 'Duration (sec)'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[top5_fault,fault_freq], fill_color='lavender',font=dict(color='black', size=12))))
                    figT.update_layout(title= "Machine faults (Updated hourly in the last hour)", margin_l=5, margin_b=0, margin_t=25, width=500)
                    
                    
                    
                    st.write(figT)
            if option == "L4- CPM1":
                fault_time("CPM1faulttime2.csv")
            if option == "L4- CPM2":
                fault_time("CPM2faulttime2.csv")   
            if option == "L4- STAMPER":
                fault_time("stamperfaulttime.csv")    
            if option == "L4- BOSCH1":
                fault_time("bosch1faulttime.csv")         
            if option == "L4- BOSCH2":
                fault_time("bosch2faulttime.csv")       
            
            
            
            ############### Machine Running Mode
  
            if option =="L4- STAMPER":
                    df_stamper_without_dash_for_machine_status = df_stamper.iloc[1:480,:]
                    stamper_runmode = pd.to_numeric(df_stamper_without_dash_for_machine_status["Stamper_In_Run_mode     "])
                    stopped= 480- stamper_runmode.sum()
                    stopped= stopped.astype(str)
                    stamper_runmode.replace(to_replace={1:0, 0:1}, inplace= True)

                    fig_stamper_runmode = go.Figure()
                    fig_stamper_runmode.add_trace(go.Bar(
                        x=df_stamper_without_dash_for_machine_status['DateAndTime            '],
                        y=stamper_runmode,
                        name='Primary Product', 
                        marker_color='red'
                       ))
                    
                    fig_stamper_runmode.update_layout( bargap=0,plot_bgcolor= 'black', title= "Stamper Run Mode", height=250, margin_b=0)
                    st.write(fig_stamper_runmode)
                    st.write("Stamper has been stopped for " +stopped +" minutes in the last 8 hours")
                    

                    
                    
            if option =="L4- BOSCH1":
                df_stamper_without_dash_for_machine_status = df_BOSCH1.iloc[1:480,:]
                stamper_runmode = pd.to_numeric(df_stamper_without_dash_for_machine_status["BOSCH_1_Running         "])
                stopped= 480- stamper_runmode.sum()
                stopped= stopped.astype(str)
                stamper_runmode.replace(to_replace={1:0, 0:1}, inplace= True)


                fig_stamper_runmode = go.Figure()

                fig_stamper_runmode.add_trace(go.Bar(
                    x=df_stamper_without_dash_for_machine_status['DateAndTime            '],
                    y=stamper_runmode,
                    name='Primary Product',
                    marker_color='red'

                    ))
                fig_stamper_runmode.update_layout( bargap=0,title= "BOSCH1 Run Mode", height=250)
                st.write(fig_stamper_runmode)
                st.write("BOSCH 1 has been stopped for " +stopped +" minutes in the last 8 hours")
            if option =="L4- BOSCH2":
                df_stamper_without_dash_for_machine_status = df_BOSCH2.iloc[1:480,:]
                stamper_runmode = pd.to_numeric(df_stamper_without_dash_for_machine_status["BOSCH_2_Running         "])
                stopped= 480- stamper_runmode.sum()
                stopped= stopped.astype(str)
                stamper_runmode.replace(to_replace={1:0, 0:1}, inplace= True)


                fig_stamper_runmode = go.Figure()

                fig_stamper_runmode.add_trace(go.Bar(
                    x=df_stamper_without_dash_for_machine_status['DateAndTime            '],
                    y=stamper_runmode,
                    name='Primary Product',
                    marker_color='red'

                    ))
                fig_stamper_runmode.update_layout( bargap=0,title= "BOSCH2 Run Mode", height=250)
                st.write(fig_stamper_runmode)
                st.write("BOSCH 2 has been stopped for " +stopped +" minutes in the last 8 hours")
            if option =="L4- CPM1":
                df_stamper_without_dash_for_machine_status = df_CPM1.iloc[1:480,:]
                stamper_runmode = pd.to_numeric(df_stamper_without_dash_for_machine_status["CPM_1_Running           "])
                stopped= 480- stamper_runmode.sum()
                stopped= stopped.astype(str)
                stamper_runmode.replace(to_replace={1:0, 0:1}, inplace= True)


                fig_stamper_runmode = go.Figure()

                fig_stamper_runmode.add_trace(go.Bar(
                    x=df_stamper_without_dash_for_machine_status['DateAndTime            '],
                    y=stamper_runmode,
                    name='Primary Product',
                    marker_color='red'

                    ))
                fig_stamper_runmode.update_layout( bargap=0,title= "CPM1 Run Mode", height=250, margin_t=0)
                st.write(fig_stamper_runmode)
                st.write("CPM 1 has been stopped for " +stopped +" minutes in the last 8 hours")
            if option =="L4- CPM2":
                df_stamper_without_dash_for_machine_status = df_CPM2.iloc[1:480,:]
                stamper_runmode = pd.to_numeric(df_stamper_without_dash_for_machine_status["CPM_1_Running           "])
                stopped= 480- stamper_runmode.sum()
                stopped= stopped.astype(str)
                stamper_runmode.replace(to_replace={1:0, 0:1}, inplace= True)


                fig_stamper_runmode = go.Figure()

                fig_stamper_runmode.add_trace(go.Bar(
                    x=df_stamper_without_dash_for_machine_status['DateAndTime            '],
                    y=stamper_runmode,
                    name='Primary Product',
                    marker_color='red'

                    ))
                fig_stamper_runmode.update_layout( bargap=0,title= "CPM2 Run Mode", height=250)
                st.write(fig_stamper_runmode)
                st.write("CPM 2 has been stopped for " +stopped +" minutes in the last 8 hours")    
            
             
                
          
                    
#                             ## This is the table for the Downstream and upstream block
#             if option =="BOSCH1":
#                 df_bosch_without_dash_for_block = df_BOSCH1.iloc[1:480,:]
#                 bosch1_upstream_block_count=df_bosch_without_dash_for_block['Bosch_01_Waiting_For_Upstream'].value_counts()[1]
#                 stop_type= ['Blocked by CPM 1', 'Waiting from Stamper']

#                 bosch1_downstream_block_count=df_bosch_without_dash_for_block['Bosch_01_Downstream_Not_Ready'].value_counts()[1]

#                 figT2= go.Figure(data= go.Table(header=dict(values=['', 'Block in minutes'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[stop_type,[bosch1_downstream_block_count,bosch1_upstream_block_count]], fill_color='lavender',font=dict(color='black', size=12))))

#                 figT2.update_layout(title= "Downstream/upstream Block", margin_t=0, margin_l=0, width=500)

#                 st.write(figT2)




#             if option=="STAMPER":

#                 df_bosch_without_dash_for_block = df_stamper.iloc[1:480,:]
#                 bosch1_upstream_block_count=df_bosch_without_dash_for_block['Stamper_Waiting_For_Upstream'].value_counts()[1]
#                 stop_type= ['Upstream waiting','A side blocked by BOSCH','B side blocked by BOSCH',]

#                 bosch1_downstream_block_count=df_bosch_without_dash_for_block['Stamper_Downstream_01_Stop'].value_counts()[1]

#                 bosch2_downstream_block_count=df_bosch_without_dash_for_block['Stamper_Downstream_02_Stop'].value_counts()[1]


#                 figT2= go.Figure(data= go.Table(header=dict(values=['', 'Block in minutes'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[stop_type,[bosch1_upstream_block_count,bosch1_downstream_block_count,bosch2_downstream_block_count]], fill_color='lavender',font=dict(color='black', size=12))))
#                 figT2.update_layout(title= "Downstream/upstream Block", margin_l=0, margin_t=0, width=500)

#                 st.write(figT2)




#             if option =="BOSCH2":

#                 df_bosch_without_dash_for_block = df_BOSCH2.iloc[1:480,:]
#                 bosch1_upstream_block_count=df_bosch_without_dash_for_block['BOSCH_2_Waiting_Upstream'].value_counts()[1]
#                 stop_type= ['Blocked by CPM 2', 'Waiting from Stamper']

#                 bosch1_downstream_block_count=df_bosch_without_dash_for_block['BOSCH_2_Downstream_Waiting'].value_counts()[1]

#                 figT2= go.Figure(data= go.Table(header=dict(values=['', 'Block in minutes'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[stop_type,[bosch1_downstream_block_count,bosch1_upstream_block_count]],fill_color='lavender',font=dict(color='black', size=12))))
#                 figT2.update_layout(title= "Downstream/upstream Block",  margin_l=0,width=500)

#                 st.write(figT2)


#                 if option =="CPM1":


#                 df_bosch_without_dash_for_block2 = df_CPM1.iloc[1:480,:]
#                 bosch1_upstream_block_count2=479-(df_bosch_without_dash_for_block2['CPM_1_Under_Fault       ']==1).value_counts()[0]
#                 stop_type= ['Waiting for BOSCH 1']

#                 bosch1_downstream_block_count2=479-(df_bosch_without_dash_for_block2['CPM_1_Blocked_Downstream']==1).value_counts()[0]

#                 figT2= go.Figure(data= go.Table(header=dict(values=['', 'Block in minutes'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[stop_type,[bosch1_upstream_block_count2]], fill_color='lavender',font=dict(color='black', size=12))))
#                 figT2.update_layout(title= "Downstream/upstream Block", margin_l=0, width=500)

#                 st.write(figT2)
#             if option == "CPM2":

#                 df_bosch_without_dash_for_block = df_CPM2.iloc[1:480,:]
#                 bosch1_upstream_block_count=479-(df_bosch_without_dash_for_block['CPM_1_Waiting_Upstream  ']).value_counts()[0]
#                 stop_type= ['Downstream Block','Waiting for BOSCH 2']

#                 bosch1_downstream_block_count=479-(df_bosch_without_dash_for_block['CPM_1_Blocked_Downstream']).value_counts()[0]

#                 figT2= go.Figure(data= go.Table(header=dict(values=['', 'Block in minutes'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[stop_type,[bosch1_downstream_block_count,bosch1_upstream_block_count]], fill_color='lavender',font=dict(color='black', size=12))))
#                 figT2.update_layout(title= "Downstream/upstream Block", margin_l=0, width=500)

#                 st.write(figT2)       


        
        
        
        

            
        with fig_col2:
           
                    
###### FUNCTION FOR BREAKDOWN TIME
                def breakdown_time_and_minor_stop_time(file_name,run_col):
                    
                        line_csv = pd.read_csv(file_name)
                        line_csv = line_csv.fillna(0)
                        line_csv_without_dash = line_csv.iloc[1:,:]
                        dt3 = datetime.strptime('2021-10-20 06:00:48.00000', "%Y-%m-%d %H:%M:%S.%f")
                        dt_line =line_csv_without_dash._get_value(1,0, takeable = True)
                        line_time = datetime.strptime(dt_line, "%Y-%m-%d %H:%M:%S.%f")

                        line_time_diff=round(((line_time-dt3).seconds)/60)
                        k = line_time_diff
                        k= int(k)

                        if k<480:
                            count =0
                            minor_stop = 0
                            breakdown = 0
                            minor_stop_time = 0
                            breakdown_time =0
                            for total in range(0,k):
                                if float(line_csv_without_dash._get_value(total+1,run_col, takeable = True))==0.0:
                                    count=  count+1


                                if float(line_csv_without_dash._get_value(total+1,run_col, takeable = True))==1.0:
                                    if count < 10 and count>0:
                                        minor_stop = minor_stop +1
                                        minor_stop_time = minor_stop_time + count

                                        count = 0
                                    if count > 10:
                                        breakdown = breakdown+1
                                        breakdown_time = breakdown_time + count

                                        count= 0
                                if (k-total)==1:
                                    if count < 10 and count>0:
                                        minor_stop = minor_stop +1
                                        minor_stop_time = minor_stop_time + count
                                        count = 0
                                    if count > 10:
                                        breakdown = breakdown+1
                                        breakdown_time = breakdown_time + count

                                        count= 0

                        if k>480 and k<960:
                            count =0
                            minor_stop = 0
                            breakdown = 0
                            minor_stop_time = 0
                            breakdown_time =0
                            for total in range(0,k-480):
                                if float(line_csv_without_dash._get_value(total+1,run_col, takeable = True))==0.0:
                                    count=  count+1


                                if float(line_csv_without_dash._get_value(total+1,run_col, takeable = True))==1.0:
                                    if count < 10 and count>0:
                                        minor_stop = minor_stop +1
                                        minor_stop_time = minor_stop_time + count
                                        count = 0
                                    if count > 10:
                                        breakdown = breakdown+1
                                        breakdown_time = breakdown_time + count

                                        count= 0
                                if (k-total)==481:
                                    if count < 10 and count>0:
                                        minor_stop = minor_stop +1
                                        minor_stop_time = minor_stop_time + count
                                        count = 0
                                    if count > 10:
                                        breakdown = breakdown+1
                                        breakdown_time = breakdown_time + count

                                        count= 0



                        if k>960:

                            count =0
                            minor_stop = 0
                            breakdown = 0
                            minor_stop_time = 0
                            breakdown_time =0
                            for total in range(0,k-960):
                                if float(line_csv_without_dash._get_value(total+1,run_col, takeable = True))==0.0:
                                    count=  count+1



                                if float(line_csv_without_dash._get_value(total+1,run_col, takeable = True))==1.0:
                                    if count < 10 and count>0:
                                        minor_stop = minor_stop +1
                                        minor_stop_time = minor_stop_time + count
                                        count = 0

                                    if count > 10:
                                        breakdown = breakdown+1
                                        breakdown_time = breakdown_time + count

                                        count= 0
                                        
                                if (k-total)==961:
                                    if count < 10 and count>0:
                                        minor_stop = minor_stop +1
                                        minor_stop_time = minor_stop_time + count
                                        count = 0
                                    if count > 10:
                                        breakdown = breakdown+1
                                        breakdown_time = breakdown_time + count

                                        count= 0


                        return(breakdown_time,minor_stop_time)
                    
                    
                    
############ fUNCCTION fOR sPEED lOSS                        
                def speed_loss_and_oee(file_name,output_count1,speed):
                        line_csv = pd.read_csv(file_name)
                        line_csv.replace(np.nan,0)
                        line_csv_without_dash = line_csv.iloc[1:,:]
                        dt3 = datetime.strptime('2021-10-20 06:00:48.00000', "%Y-%m-%d %H:%M:%S.%f")
                        dt_line =line_csv_without_dash._get_value(1,0, takeable = True)
                        line_time = datetime.strptime(dt_line, "%Y-%m-%d %H:%M:%S.%f")

                        line_time_diff=round(((line_time-dt3).seconds)/60)
                        output_count = float(line_csv_without_dash._get_value(1,output_count1, takeable = True))
                        print(output_count)
                        if line_time_diff<480:
                            present_time = (line_time_diff - 0)
                            OEE = output_count/500
                            speed_loss = ((500*present_time)-output_count)/500
                            
                            
                        if line_time_diff>480 and line_time_diff<960:
                            present_time = line_time_diff - 480
                            OEE = output_count/500
                            speed_loss = ((500*present_time)-output_count)/500


                        if line_time_diff>960:
                            present_time = line_time_diff - 960
                            OEE = output_count/500
                            speed_loss = ((500*present_time)-output_count)/500
                            

                        return(OEE, speed_loss)
                    
                    
                def speed_loss_and_oee_2(file_name,output_count1,speed):
                        line_csv = pd.read_csv(file_name)
                        line_csv.replace(np.nan,0)
                        line_csv_without_dash = line_csv.iloc[1:,:]
                        dt3 = datetime.strptime('2021-10-20 06:00:48.00000', "%Y-%m-%d %H:%M:%S.%f")
                        dt_line =line_csv_without_dash._get_value(1,0, takeable = True)
                        line_time = datetime.strptime(dt_line, "%Y-%m-%d %H:%M:%S.%f")

                        line_time_diff=round(((line_time-dt3).seconds)/60)
                        output_count = float(line_csv_without_dash._get_value(1,output_count1, takeable = True))
                        print(output_count)
                        if line_time_diff<480:
                            present_time = (line_time_diff - 0)
                            OEE2 = (output_count*SKU)/220
                            speed_loss2 = ((220*present_time)-(output_count*SKU))/220
                            
#                             df_stamper_without_dash_for_machine_status = df_CPM1.iloc[1:480,:]
#                             stopped = pd.to_numeric(df_stamper_without_dash_for_machine_status["CPM_1_Running           "])
#                             stopped= 480- stamper_runmode.sum()
#                             stopped= stopped.astype(str)
                            
                            
                        if line_time_diff>480 and line_time_diff<960:
                            present_time = line_time_diff - 480
                            OEE2 = (output_count*SKU)/220
                            speed_loss2 = ((220*present_time)-(output_count*SKU))/220


                        if line_time_diff>960:
                            present_time = line_time_diff - 960
                            OEE2 = (output_count*SKU)/220
                            speed_loss2 = ((220*present_time)-(output_count*SKU))/220

                        return(OEE2, speed_loss2)
        
        
        
        
        
        
        
        
                    
                def speed_loss_and_oee_3(file_name,output_count1,speed):
                        line_csv = pd.read_csv(file_name)
                        line_csv.replace(np.nan,0)
                        line_csv_without_dash = line_csv.iloc[1:,:]
                        dt3 = datetime.strptime('2021-10-20 06:00:48.00000', "%Y-%m-%d %H:%M:%S.%f")
                        dt_line =line_csv_without_dash._get_value(1,0, takeable = True)
                        line_time = datetime.strptime(dt_line, "%Y-%m-%d %H:%M:%S.%f")

                        line_time_diff=round(((line_time-dt3).seconds)/60)
                        output_count = float(line_csv_without_dash._get_value(1,output_count1, takeable = True))
                        print(output_count)
                        if line_time_diff<480:
                            present_time = (line_time_diff - 0)
                            OEE = output_count/250
                            speed_loss = ((250*present_time)-output_count)/250
                        if line_time_diff>480 and line_time_diff<960:
                            present_time = line_time_diff - 480
                            OEE = output_count/250
                            speed_loss = ((250*present_time)-output_count)/250

                        if line_time_diff>960:
                            present_time = line_time_diff - 960
                            OEE = output_count/250
                            speed_loss = ((250*present_time)-output_count)/250

                        return(OEE, speed_loss)  
                    
                    
                if option =="L4- STAMPER":
                    
                    
                    OEE, speed_loss = speed_loss_and_oee("L4STAMPER.csv",10,500)
                    breakdown_time, minor_stop_time = breakdown_time_and_minor_stop_time("L4Stamper.csv",7)
                    speed_loss_minus_stop = speed_loss - minor_stop_time -  breakdown_time
                    
                    st.write("Stamper Loss Capturing")
                    labels = ['Breakdown/Other loss', 'Minor Stop',  'OEE', 'Speed Loss/Recycle']
                    values2 = [breakdown_time, minor_stop_time, OEE, speed_loss_minus_stop]
                    fig2 = px.pie(labels, values = values2, names = labels, 
                                 color_discrete_map={'OEE':'lightcyan',
                                 'Breakdown/Other loss':'cyan',
                                 'Minor Stop':'royalblue',
                                 'Speed Loss/Recycle':'darkblue'},
                                  width=350, height=400)
                    fig2.update_layout(legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1))
                    st.write(fig2)

    #################################################################   MACHINE lOSS CAPTURING            # 
                    
                if option == "L4- CPM1":
                    OEE, speed_loss = speed_loss_and_oee_2("L4CPM1.csv",5,250)
                    breakdown_time, minor_stop_time = breakdown_time_and_minor_stop_time("L4CPM1.csv",3)
                    speed_loss_minus_stop = speed_loss - minor_stop_time -  breakdown_time
                    st.write("CPM1 Loss Capturing")
                    labels = ['Breakdown/Other loss', 'Minor Stop Time',  'OEE', 'Speed Loss']
                    values2 = [breakdown_time, minor_stop_time, OEE, speed_loss_minus_stop]
                    fig2 = px.pie(labels, values = values2, names = labels,width=400, height=400)
                    fig2.update_layout(legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1))
                    st.write(fig2)

#################################################################   MACHINE lOSS CAPTURING            # 
                    
                if option == "L4- CPM2":
                    OEE, speed_loss = speed_loss_and_oee_2("L4CPM2.csv",11,250)
                    breakdown_time, minor_stop_time = breakdown_time_and_minor_stop_time("L4CPM2.csv",3)
                    speed_loss_minus_stop = speed_loss - minor_stop_time -  breakdown_time
                    st.write("CPM2 Loss Capturing")
                    labels = ['Breakdown/Other loss', 'Minor Stop Time',  'OEE', 'Speed Loss']
                    values2 = [breakdown_time, minor_stop_time, OEE, speed_loss_minus_stop]
                    fig2 = px.pie(labels, values = values2, names = labels,width=400, height=400)
                    fig2.update_layout(legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1))
                    st.write(fig2)



    #################################################################   MACHINE lOSS CAPTURING            # 
                    
                if option == "L4- BOSCH1":
                    OEE, speed_loss = speed_loss_and_oee_3("L4BOSCH1.csv",8,250)
                    breakdown_time, minor_stop_time = breakdown_time_and_minor_stop_time("L4BOSCH1.csv",3)
                    speed_loss_minus_stop = speed_loss - minor_stop_time -  breakdown_time
                    st.write("BOSCH1 Loss Capturing")
                    labels = ['Breakdown/Other loss', 'Minor Stop Time',  'OEE', 'Speed Loss']
                    values2 = [breakdown_time, minor_stop_time, OEE, speed_loss_minus_stop]
                    fig2 = px.pie(labels, values = values2, names = labels,width=400, height=400)
                    fig2.update_layout(legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1))
                    st.write(fig2)



    #################################################################   MACHINE lOSS CAPTURING            # 
                    
                if option == "L4- BOSCH2":
                    OEE, speed_loss = speed_loss_and_oee_3("L4BOSCH2.csv",9,250)
                    breakdown_time, minor_stop_time = breakdown_time_and_minor_stop_time("L4BOSCH2.csv",3)
                    speed_loss_minus_stop = speed_loss - minor_stop_time -  breakdown_time
                    st.write("BOSCH2 Loss Capturing")
                    labels = ['Breakdown/Other loss', 'Minor Stop Time',  'OEE', 'Speed Loss']
                    values2 = [breakdown_time, minor_stop_time, OEE, speed_loss_minus_stop]
                    fig2 = px.pie(labels, values = values2, names = labels,width=400, height=400)
                    fig2.update_layout(legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1))
                    st.write(fig2)
                    
                    

 
                
        with fig_col3:
            if option=="L4- CPM1" or option=="L4- CPM2" or option== "L4- BOSCH1" or option=="L4- BOSCH2" or option=="L4- STAMPER":
            
#                         ################## TOTAL FBC
                df_LINE_CSV = pd.read_csv("Line.csv")
                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[1,:]
                first= df_LINE_CSV.iloc[1,:]
                first = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x1= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[30,:]   
                second= df_LINE_CSV.iloc[30,:]
                second = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x2= df_line_csv_without_dash_for_machine_status['DateAndTime            ']


                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[60,:]
                third= df_LINE_CSV.iloc[60,:]
                third = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x3= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[90,:]
                fourth= df_LINE_CSV.iloc[90,:]
                fourth = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x4= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[120,:]
                fifth= df_LINE_CSV.iloc[120,:]
                fifth = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x5= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[150,:]
                sixth= df_LINE_CSV.iloc[150,:]
                sixth = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x6= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[180,:]
                seven= df_LINE_CSV.iloc[180,:]
                seven = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x7= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[210,:]
                eight=df_LINE_CSV.iloc[210,:]
                eight = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x8= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[240,:]
                nine=df_LINE_CSV.iloc[240,:]
                nine = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x9= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[270,:]
                ten=df_LINE_CSV.iloc[270,:]
                ten = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x10= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[300,:]
                el= df_LINE_CSV.iloc[300,:]
                el = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x11= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[330,:]
                twel= df_LINE_CSV.iloc[330,:]
                twel = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x12= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[360,:]
                thir= df_LINE_CSV.iloc[360,:]
                thir = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x13= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[390,:]
                fourteen= df_LINE_CSV.iloc[390,:]
                fourteen = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x14= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[420,:]
                fifteen= df_LINE_CSV.iloc[420,:]
                fifteen = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x15= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[450,:]
                sixteen= df_LINE_CSV.iloc[450,:]
                sixteen = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x16= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[480,:]
                seventeen= df_LINE_CSV.iloc[480,:]
                seventeen = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x17= df_line_csv_without_dash_for_machine_status['DateAndTime            ']



                #df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[1,:]

                #line_tot = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])


    #first,second, third, fourth, fifth, sixth, seven, eight,nine,ten,el,twel,thir,fourteen, fifteen, sixteen, seventeen

                fig_line_tot = go.Figure()

                fig_line_tot.add_trace(go.Bar(
                    x=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],
                    y=[seventeen-first,first-second, second-third, third-fourth, fourth-fifth, fifth-sixth, sixth-seven, seven-eight,eight-nine,nine-ten,ten-el,el-twel,twel-thir,thir-fourteen, fourteen-fifteen, fifteen-sixteen, sixteen-seventeen],
                    name='Primary Product',
                    marker_color='darkcyan', 

                    ))
                fig_line_tot.update_layout( bargap=0.5 ,title= "Total FBC (every 30 mins)",width=650,margin_b=0,
                    height=320,
                    margin_r = 0)
                fig_line_tot.update_yaxes(range=[0,300])
                st.write(fig_line_tot)


            if option=="Line 6":
                df_LINE_CSV = pd.read_csv("Line6.csv")
                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[1,:]
                first= df_LINE_CSV.iloc[1,:]
                first = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x1= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[30,:]   
                second= df_LINE_CSV.iloc[30,:]
                second = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x2= df_line_csv_without_dash_for_machine_status['DateAndTime            ']


                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[60,:]
                third= df_LINE_CSV.iloc[60,:]
                third = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x3= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[90,:]
                fourth= df_LINE_CSV.iloc[90,:]
                fourth = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x4= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[120,:]
                fifth= df_LINE_CSV.iloc[120,:]
                fifth = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x5= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[150,:]
                sixth= df_LINE_CSV.iloc[150,:]
                sixth = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x6= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[180,:]
                seven= df_LINE_CSV.iloc[180,:]
                seven = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x7= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[210,:]
                eight=df_LINE_CSV.iloc[210,:]
                eight = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x8= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[240,:]
                nine=df_LINE_CSV.iloc[240,:]
                nine = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x9= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[270,:]
                ten=df_LINE_CSV.iloc[270,:]
                ten = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x10= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[300,:]
                el= df_LINE_CSV.iloc[300,:]
                el = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x11= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[330,:]
                twel= df_LINE_CSV.iloc[330,:]
                twel = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x12= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[360,:]
                thir= df_LINE_CSV.iloc[360,:]
                thir = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x13= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[390,:]
                fourteen= df_LINE_CSV.iloc[390,:]
                fourteen = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x14= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[420,:]
                fifteen= df_LINE_CSV.iloc[420,:]
                fifteen = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x15= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[450,:]
                sixteen= df_LINE_CSV.iloc[450,:]
                sixteen = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x16= df_line_csv_without_dash_for_machine_status['DateAndTime            ']

                df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[480,:]
                seventeen= df_LINE_CSV.iloc[480,:]
                seventeen = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
                x17= df_line_csv_without_dash_for_machine_status['DateAndTime            ']



                #df_line_csv_without_dash_for_machine_status =  df_LINE_CSV.iloc[1,:]

                #line_tot = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])


    #first,second, third, fourth, fifth, sixth, seven, eight,nine,ten,el,twel,thir,fourteen, fifteen, sixteen, seventeen

                fig_line_tot = go.Figure()

                fig_line_tot.add_trace(go.Bar(
                    x=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],
                    y=[seventeen-first,first-second, second-third, third-fourth, fourth-fifth, fifth-sixth, sixth-seven, seven-eight,eight-nine,nine-ten,ten-el,el-twel,twel-thir,thir-fourteen, fourteen-fifteen, fifteen-sixteen, sixteen-seventeen],
                    name='Primary Product',
                    marker_color='darkcyan', 

                    ))
                fig_line_tot.update_layout( bargap=0.5 ,title= "Total FBC (every 30 mins)",width=650,margin_b=0,
                    height=320,
                    margin_r = 0)
                fig_line_tot.update_yaxes(range=[0,300])
                st.write(fig_line_tot)

                
            
            
#             ################## TOTAL FBC
#             df_LINE_CSV = pd.read_csv("Line.csv")
#             df_line_csv_without_dash_for_machine_status = df_LINE_CSV.iloc[1:480,:]
#             line_tot = pd.to_numeric(df_line_csv_without_dash_for_machine_status["TOTAL_FBC               "])
            


#             fig_line_tot = go.Figure()

#             fig_line_tot.add_trace(go.Bar(
#                 x=df_line_csv_without_dash_for_machine_status['DateAndTime            '],
#                 y=line_tot,
#                 name='Primary Product',
#                 marker_color='red'

#                 ))
#             fig_line_tot.update_layout( bargap=0 ,title= "Total FBC",width=650,
#                 height=320,
#                 margin_r = 0)
#             st.write(fig_line_tot)
        
            

            
            ###############Machine RUnning Speed
            if option == "L4- STAMPER":
                    figl = go.Figure(data=go.Scatter(x=df_stamper_without_dash['DateAndTime            '],y=pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[1:481])))
                    avgspd= pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[1:481])
                    #wrong = avgspd.mean()
                    sum_spd= avgspd.sum()
                    zero= avgspd.value_counts()[0]
                    avg_spd= sum_spd/(480-zero)
                    avg_spd= round(avg_spd,2)
                    avg_spd= avg_spd.astype(str)
                    #no= (avgspd==0).sum()
                    #no=no.sum()
                    
                    
                    figl.update_layout(
                    title="Stamper Running Speed", height=300)
                    st.write(figl)
                    st.write("Average speed of stamper in the last 8 hours is:   " +avg_spd+ "  UPM ")
                    #st.write(wrong)
                    
                    
                    #av1 = avgspd.iloc[1:60,:]
                    av1 = pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[1:60])
                    
                    stopped= 61- av1.value_counts()[0]
                    avg1= round(av1.sum()/stopped)
                   
                    
                    av2 = pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[60:120])
                    stopped= 61- av2.value_counts()[0]
                    avg2= round(av2.sum()/stopped)
                    
                    
                    av3 = pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[120:180])
                    stopped= 61- av3.value_counts()[0]
                    avg3= round(av3.sum()/stopped)
                    
                    
                    av4 = pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[180:240])
                    stopped= 61- av4.value_counts()[0]
                    avg4= round(av4.sum()/stopped)
                    
                    
                    av5 = pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[240:300])
                    stopped= 61- av5.value_counts()[0]
                    avg5= round(av5.sum()/stopped)
                  
                    av6 = pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[300:360])
                    stopped= 61- av6.value_counts()[0]
                    avg6= round(av6.sum()/stopped)
                    
                    
                    
                    av7 = pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[360:410])
                    stopped= 61- av7.value_counts()[0]
                    avg7= round(av7.sum()/stopped)
                   
                    
                    av8 = pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[410:480])
                    stopped= 61- av8.value_counts()[0]
                    avg8= round(av8.sum()/stopped)
                   
                    
                    hourtimes = ['1 hour', '2 hour', '3 hour', '4 hour'  , '5 hour', '6 huor', '7 hour', '8 hour']
                    avgspeeds= [avg1 , avg2, avg3, avg4, avg5, avg6, avg7, avg8]
                    
                    figT= go.Figure(data= go.Table(header=dict(values=['Last hour', 'Avg speed (UPM)'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[hourtimes,avgspeeds], fill_color='lavender',font=dict(color='black', size=12))))
                    figT.update_layout(title= "Average speed", margin_l=5, margin_b=0, margin_t=25, width=500)
                    
                    
                    
                    st.write(figT)
                    
                    
                    
                    
                    
                    
                    

            if option == "L4- BOSCH1":

                figl_BOSCH1_speed = go.Figure(data=go.Scatter(x=df_BOSCH1_without_dash['DateAndTime            '],y=pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[1:481])))
                avgspd= pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[1:481])
                sum_spd= avgspd.sum()
                zero= avgspd.value_counts()[0]
                avg_spd= sum_spd/(480-zero)
                avg_spd= round(avg_spd,2)
                avg_spd= avg_spd.astype(str)
                figl_BOSCH1_speed.update_layout(
                title="BOSCH1 Running Speed", margin_b=0,height=300)
                st.write(figl_BOSCH1_speed)
                st.write("Average speed of BOSCH 1 in the last 8 hours is:   " +avg_spd+ "  UPM ")
                
                    
                    
                    #av1 = avgspd.iloc[1:60,:]
                av1 = pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[1:60])

                stopped= 61- av1.value_counts()[0]
                avg1= round(av1.sum()/stopped)


                av2 = pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[60:120])
                stopped= 61- av2.value_counts()[0]
                avg2= round(av2.sum()/stopped)


                av3 = pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[120:180])
                stopped= 61- av3.value_counts()[0]
                avg3= round(av3.sum()/stopped)


                av4 = pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[180:240])
                stopped= 61- av4.value_counts()[0]
                avg4= round(av4.sum()/stopped)


                av5 = pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[240:300])
                stopped= 61- av5.value_counts()[0]
                avg5= round(av5.sum()/stopped)

                av6 = pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[300:360])
                stopped= 61- av6.value_counts()[0]
                avg6= round(av6.sum()/stopped)



                av7 = pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[360:410])
                stopped= 61- av7.value_counts()[0]
                avg7= round(av7.sum()/stopped)


                av8 = pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[410:480])
                stopped= 61- av8.value_counts()[0]
                avg8= round(av8.sum()/stopped)


                hourtimes = ['1 hour', '2 hour', '3 hour', '4 hour'  , '5 hour', '6 huor', '7 hour', '8 hour']
                avgspeeds= [avg1 , avg2, avg3, avg4, avg5, avg6, avg7, avg8]

                figT= go.Figure(data= go.Table(header=dict(values=['Last hour', 'Avg speed (UPM)'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[hourtimes,avgspeeds], fill_color='lavender',font=dict(color='black', size=12))))
                figT.update_layout(title= "Average speed", margin_l=5, margin_b=0, margin_t=25, width=500)

                    
                    
                st.write(figT)                    
            if option == "L4- BOSCH2":


                figl_BOSCH2_speed = go.Figure(data=go.Scatter(x=df_BOSCH1_without_dash['DateAndTime            '],y=pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[1:481])))
                avgspd= pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[1:481])
                sum_spd= avgspd.sum()
                zero= avgspd.value_counts()[0]
                avg_spd= sum_spd/(480-zero)
                avg_spd= round(avg_spd,2)
                avg_spd= avg_spd.astype(str)
                figl_BOSCH2_speed.update_layout(
                title="BOSCH2 Running Speed",margin_b=0, height=300)

                st.write(figl_BOSCH2_speed)
                st.write("Average speed of BOSCH 2 in the last 8 hours is:   " +avg_spd+ "  UPM ")
                st.write(avg_spd)

                av1 = pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[1:60])

                stopped= 61- av1.value_counts()[0]
                avg1= round(av1.sum()/stopped)


                av2 = pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[60:120])
                stopped= 61- av2.value_counts()[0]
                avg2= round(av2.sum()/stopped)


                av3 = pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[120:180])
                stopped= 61- av3.value_counts()[0]
                avg3= round(av3.sum()/stopped)


                av4 = pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[180:240])
                stopped= 61- av4.value_counts()[0]
                avg4= round(av4.sum()/stopped)


                av5 = pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[240:300])
                stopped= 61- av5.value_counts()[0]
                avg5= round(av5.sum()/stopped)

                av6 = pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[300:360])
                stopped= 61- av6.value_counts()[0]
                avg6= round(av6.sum()/stopped)



                av7 = pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[360:410])
                stopped= 61- av7.value_counts()[0]
                avg7= round(av7.sum()/stopped)


                av8 = pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[410:480])
                stopped= 61- av8.value_counts()[0]
                avg8= round(av8.sum()/stopped)


                hourtimes = ['1 hour', '2 hour', '3 hour', '4 hour'  , '5 hour', '6 huor', '7 hour', '8 hour']
                avgspeeds= [avg1 , avg2, avg3, avg4, avg5, avg6, avg7, avg8]

                figT= go.Figure(data= go.Table(header=dict(values=['Last hour', 'Avg speed (UPM)'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[hourtimes,avgspeeds], fill_color='lavender',font=dict(color='black', size=12))))
                figT.update_layout(title= "Average speed", margin_l=5, margin_b=0, margin_t=25, width=500)

                    
                    
                st.write(figT)                    
            if option == "L4- CPM1":

                figl_CPM1_speed =  go.Figure(data=go.Scatter(x=df_CPM1_without_dash['DateAndTime            '],y=pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[1:481])))
                avgspd= pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[1:481])
                sum_spd= avgspd.sum()
                zero= avgspd.value_counts()[0]
                avg_spd= sum_spd/(480-zero)
                avg_spd= round(avg_spd,2)
                avg_spd= avg_spd.astype(str)
                figl_CPM1_speed.update_layout(
                title="CPM1 Running Speed", height=300)
                st.write(figl_CPM1_speed)
                st.write("Average speed of CPM 1 in the last 8 hours is:   " +avg_spd+ "  UPM ")
                
                av1 = pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[1:60])

                stopped= 61- av1.value_counts()[0]
                avg1= round(av1.sum()/stopped)


                av2 = pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[60:120])
                stopped= 61- av2.value_counts()[0]
                avg2= round(av2.sum()/stopped)


                av3 = pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[120:180])
                stopped= 61- av3.value_counts()[0]
                avg3= round(av3.sum()/stopped)


                av4 = pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[180:240])
                stopped= 61- av4.value_counts()[0]
                avg4= round(av4.sum()/stopped)


                av5 = pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[240:300])
                stopped= 61- av5.value_counts()[0]
                avg5= round(av5.sum()/stopped)

                av6 = pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[300:360])
                stopped= 61- av6.value_counts()[0]
                avg6= round(av6.sum()/stopped)



                av7 = pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[360:410])
                stopped= 61- av7.value_counts()[0]
                avg7= round(av7.sum()/stopped)


                av8 = pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[410:480])
                stopped= 61- av8.value_counts()[0]
                avg8= round(av8.sum()/stopped)


                hourtimes = ['1 hour', '2 hour', '3 hour', '4 hour'  , '5 hour', '6 huor', '7 hour', '8 hour']
                avgspeeds= [avg1 , avg2, avg3, avg4, avg5, avg6, avg7, avg8]

                figT= go.Figure(data= go.Table(header=dict(values=['Last hour', 'Avg speed (UPM)'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[hourtimes,avgspeeds], fill_color='lavender',font=dict(color='black', size=12))))
                figT.update_layout(title= "Average speed", margin_l=5, margin_b=0, margin_t=25, width=500)                
                
            if option == "L4- CPM2":


                figl_CPM2_speed = go.Figure(data=go.Scatter(x=df_CPM2_without_dash['DateAndTime            '],y=pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[1:481])))
                avgspd= pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[1:481])
                sum_spd= avgspd.sum()
                zero= avgspd.value_counts()[0]
                avg_spd= sum_spd/(480-zero)
                avg_spd= round(avg_spd,2)
                avg_spd= avg_spd.astype(str)
                figl_CPM2_speed.update_layout(
                title="CPM2 Running Speed", height=300)

                st.write(figl_CPM2_speed)
                st.write("Average speed of CPM 2 in the last 8 hours is:   " +avg_spd+ "  UPM ")
                

    
                av1 = pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[1:60])

                stopped= 61- av1.value_counts()[0]
                avg1= round(av1.sum()/stopped)


                av2 = pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[60:120])
                stopped= 61- av2.value_counts()[0]
                avg2= round(av2.sum()/stopped)


                av3 = pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[120:180])
                stopped= 61- av3.value_counts()[0]
                avg3= round(av3.sum()/stopped)


                av4 = pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[180:240])
                stopped= 61- av4.value_counts()[0]
                avg4= round(av4.sum()/stopped)


                av5 = pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[240:300])
                stopped= 61- av5.value_counts()[0]
                avg5= round(av5.sum()/stopped)

                av6 = pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[300:360])
                stopped= 61- av6.value_counts()[0]
                avg6= round(av6.sum()/stopped)



                av7 = pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[360:410])
                stopped= 61- av7.value_counts()[0]
                avg7= round(av7.sum()/stopped)


                av8 = pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[410:480])
                stopped= 61- av8.value_counts()[0]
                avg8= round(av8.sum()/stopped)


                hourtimes = ['1 hour', '2 hour', '3 hour', '4 hour'  , '5 hour', '6 huor', '7 hour', '8 hour']
                avgspeeds= [avg1 , avg2, avg3, avg4, avg5, avg6, avg7, avg8]

                figT= go.Figure(data= go.Table(header=dict(values=['Last hour', 'Avg speed (UPM)'],fill_color='paleturquoise', font=dict(color='black', size=12)),cells=dict(values=[hourtimes,avgspeeds], fill_color='lavender',font=dict(color='black', size=12))))
                figT.update_layout(title= "Average speed", margin_l=5, margin_b=0, margin_t=25, width=500)          
    
    
    
    
    
    
    
    
    
    
    

           
        
        time.sleep(1)
    #placeholder.empty()