import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import joblib


st.title("Project Cost Prediction App")
st.write("From the project data encoded in IMPRESSION, we built a machine learning model to predict the project costs.")

#Data frame
project = pd.read_csv("project.csv")

#Sidebar
st.sidebar.title("Options")
option_sidebar = st.sidebar.selectbox("Choose your option:",['Data', 'Chart 1', 'Chart 2', 'Chart 3'])

st.sidebar.title("Project Cost Parameters")
st.sidebar.write("Tweak the values to change predictions")

if option_sidebar == 'Data':
    st.header("IMPRESSION Project Data Frame")
    st.write(project.head(20))
    
elif option_sidebar == 'Chart 1':
    st.header("Chart 1")
    graph1 = sns.countplot(data=project, x='province', color='gray')
    graph1.set(xlabel='Province', ylabel='Number of Projects', title='Total Number of Projects in CALABARZON')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

elif option_sidebar == 'Chart 2':
    st.header("Chart 2")
    graph1 = sns.countplot(data=project, y='prj_type', hue='more_coop')
    graph1.set(xlabel='Number of Projects', ylabel='Project Type', title='Number of Cooperators per Project Type in CALABARZON')
    graph1.legend(title='Number of Cooperators')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
elif option_sidebar == 'Chart 3':
    st.header("Chart 3")
    graph1 = sns.barplot(data=project, y='sector', x='prj_cost_setup',ci=None, color='green', estimator=sum)
    graph1.set(xlabel='Total Project Cost', ylabel='Project Sectors', title='Total Amount of Project Cost per Sector in CALABARZON')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

#MLR Model for Projec Cost Predictions
#Project Type
prj_type = st.sidebar.selectbox("Project Type", ['GIA (Community Based)','GIA (Region-initiated Projects) Internally Funded','GIA (Region-initiated Projects) Externally Funded','Roll-out','SETUP', 'TAPI-assisted'])

if prj_type == 'GIA (Community Based)':
    type_list = [1, 0, 0, 0, 0, 0]
elif prj_type == 'GIA (Region-initiated Projects) Internally Funded':
    type_list = [0, 1, 0, 0, 0, 0]
elif prj_type == 'GIA (Region-initiated Projects) Externally Funded':
    type_list = [0, 0, 1, 0, 0, 0]
elif prj_type == 'Roll-out':
    type_list = [0, 0, 0, 1, 0, 0]
elif prj_type == 'SETUP':
    type_list = [0, 0, 0, 0, 1, 0]
elif prj_type == 'TAPI-assisted':
    type_list = [0, 0, 0, 0, 0, 1]

#Project Sector
sector = st.sidebar.selectbox("Project Sectors", ['Agriculture / Marine / Aquaculture / Forestry / Livestock','Food Processing', 'Furniture','Gifts / Decors / Handicrafts','Halal Products & Service','Health & Wellness Products', 'ICT', 'Metals & Engineering', 'Other Regional Industry Priorities'])
              
if sector == 'Agriculture / Marine / Aquaculture / Forestry / Livestock':
    sector_list = [1, 0, 0, 0, 0, 0, 0, 0, 0]
elif sector == 'Food Processing':
    sector_list = [0, 1, 0, 0, 0, 0, 0, 0, 0]
elif sector == 'Furniture':
    sector_list = [0, 0, 1, 0, 0, 0, 0, 0, 0]
elif sector == 'Gifts / Decors / Handicrafts':
    sector_list = [0, 0, 0, 1, 0, 0, 0, 0, 0]
elif sector == 'Halal Products & Service':
    sector_list = [0, 0, 0, 0, 1, 0, 0, 0, 0]
elif sector == 'Health & Wellness Products':
    sector_list = [0, 0, 0, 0, 0, 1, 0, 0, 0]
elif sector == 'ICT':
    sector_list = [0, 0, 0, 0, 0, 0, 1, 0, 0]
elif sector == 'Metals & Engineering':
    sector_list = [0, 0, 0, 0, 0, 0, 0, 1, 0]
elif sector == 'Other Regional Industry Priorities':
    sector_list = [0, 0, 0, 0, 0, 0, 0, 0, 1]

#Province
province = st.sidebar.selectbox("Province", ['Batangas', 'Cavite', 'Laguna', 'Quezon', 'Rizal'])

if province == 'Batangas':
    province_list = [1, 0, 0, 0, 0]
elif province == 'Cavite':
    province_list = [0, 1, 0, 0, 0]
elif province == 'Laguna':
    province_list = [0, 0, 1, 0, 0]
elif province == 'Quezon':
    province_list = [0, 0, 0, 1, 0]
elif province == 'Rizal':
    province_list = [0, 0, 0, 0, 1]

#Number of Cooperators
num_coop = st.sidebar.slider("Number of cooperators",1,100,2)
    
#Main Page
st.subheader("Project Cost Prediction")

#Loading the model
filename = 'project_data_model.sav'
loaded_model = joblib.load(filename)

#Prediction
prediction = round(loaded_model.predict([[num_coop] + type_list + sector_list + province_list])[0])
st.write(f"Predicted project cost of the project is :  {prediction}")