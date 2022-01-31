import pickle

import streamlit as st

model = 'model/diabetes_model.sav'
load_model = pickle.load(open(model, 'rb'))

apptitle = 'Diabetes Prediction Dashboard'
st.set_page_config(page_title=apptitle, page_icon=":package:")
st.markdown("""
            # Diabetes Prediction Dashboard
            * Predict whether or not a patient has diabetes, based on several medical predictor variable
            * Model source: Model source: <https://github.com/trizkynoviandy/pima-indian-diabetes>
            ---
            """)

st.write("1. Pregnancies")
user_input = st.text_input("Number of times pregnant")
st.write("2. Glucose")
user_input = st.text_input("Plasma glucose concentration a 2 hours in an oral glucose tolerance test")
st.write("3. Blood Pressure")
user_input = st.text_input("Diastolic blood pressure (mm Hg)")
st.write("4. Skin Thickness")
user_input = st.text_input("Triceps skin fold thickness (mm)")
st.write("5. Insulin")
user_input = st.text_input("2-Hour serum insulin (mu U/ml)")
st.write("6. BMI")
user_input = st.text_input("Body mass index (weight in kg/(height in m)^2)")
st.write("7. Diabetes Pedigree Function")
user_input = st.text_input("Diabetes pedigree function")
st.write("8. Age")
user_input = st.text_input("Age (years)")

user_output = None
if user_output != None:
    st.write("Output : {}".format(user_output))