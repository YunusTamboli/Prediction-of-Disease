import numpy as np
import pandas as pd 
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of Disease Outbreaks", layout='wide')

# Load the models
diabetes_model = pickle.load(open('C:/Users/Yunus/Downloads/pptj/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('C:/Users/Yunus/Downloads/pptj/heart_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/Yunus/Downloads/pptj/parkinsons_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu(
        "Prediction of Disease Outbreak System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
        menu_icon="hospital-fill",
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    
    # Use simple form without columns for compatibility
    Pregnancies = st.text_input("Number of Pregnancies")
    BloodPressure = st.text_input("Blood Pressure value")
    Insulin = st.text_input("Insulin level")
    Glucose = st.text_input("Glucose level")
    SkinThickness = st.text_input("Skin Thickness value")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age of the person")
    
    # Convert input to float and predict
    diab_diagnosis = ''
    if st.button("Diabetes Test Result"):
        # Indentation corrected here
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]  # Convert all inputs to float
        
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not diabetic"
        st.success(diab_diagnosis)
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    
    # Input fields for heart disease prediction
    age = st.text_input("Age of the person")
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    trestbps = st.text_input("Resting Blood Pressure")
    cholestrol = st.text_input("Cholesterol level")
    
    fbs = st.selectbox("Fasting Blood Sugar", ["True", "False"])
    restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
    thalach = st.text_input("Maximum Heart Rate Achieved")
    exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.text_input("Depression Induced by Exercise Relative to Rest")
    
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

    # Convert inputs to numeric values
    heart_diagnosis = ''
    
    if st.button("Heart Disease Test Result"):
        # Prepare the input for the model with raw string inputs
        user_input = [age, sex, cp, trestbps, cholestrol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        
        # Make prediction
        heart_prediction = heart_model.predict([user_input])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = "The person is at risk of heart disease"
        else:
            heart_diagnosis = "The person is not at risk of heart disease"
        
        # Display the result
        st.success(heart_diagnosis)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    
    # Input fields for Parkinson's disease prediction (use all 22 features)
    # Assuming the model was trained with 22 features. Add all required fields here.
    MDVP_Fo = st.text_input("MDVP:Fo(Hz)")
    MDVP_Fhi = st.text_input("MDVP:Fhi(Hz)")
    MDVP_Flo = st.text_input("MDVP:Flo(Hz)")
    MDVP_Jitter = st.text_input("MDVP:Jitter(%)")
    MDVP_JitterAbs = st.text_input("MDVP:Jitter(Abs)")
    MDVP_RAP = st.text_input("MDVP:RAP")
    MDVP_PPQ = st.text_input("MDVP:PPQ")
    Jitter_DDP = st.text_input("Jitter:DDP")
    MDVP_Shimmer = st.text_input("MDVP:Shimmer")
    MDVP_ShimmerDB = st.text_input("MDVP:Shimmer(dB)")
    Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
    Shimmer_APQ5 = st.text_input("Shimmer:APQ5")
    MDVP_APQ = st.text_input("MDVP:APQ")
    Shimmer_DDA = st.text_input("Shimmer:DDA")
    NHR = st.text_input("NHR")
    HNR = st.text_input("HNR")
    RPDE = st.text_input("RPDE")
    DFA = st.text_input("DFA")
    spread1 = st.text_input("spread1")
    spread2 = st.text_input("spread2")
    D2 = st.text_input("D2")
    PPE = st.text_input("PPE")
    
    # Convert inputs to numeric values with error handling
    parkinsons_diagnosis = ''
    
    if st.button("Parkinson's Test Result"):
        user_input = [
            MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_JitterAbs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
            MDVP_Shimmer, MDVP_ShimmerDB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR,
            RPDE, DFA, spread1, spread2, D2, PPE
        ]
        
        try:
            # Validate and convert inputs to float
            user_input = [float(x) if x else 0.0 for x in user_input]  # Replace empty fields with 0.0
            parkinsons_prediction = parkinsons_model.predict([user_input])
            
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person is likely to have Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person is unlikely to have Parkinson's disease"
            st.success(parkinsons_diagnosis)
        except ValueError:
            st.error("Please ensure all inputs are valid numbers.")
