import pickle

import streamlit as st

model = 'model/diabetes_model.sav'
load_model = pickle.load(open(model, 'rb'))

apptitle = 'Diabetes Prediction Dashboard'
st.set_page_config(page_title=apptitle, page_icon=":package:")
st.markdown("""
            # Diabetes Prediction Dashboard
            * Predict whether or not you have diabetes, based on several medical predictor variable
            
            * The predictions obtained by this application have no medical value, to get accurate results please consult a doctor.
            * Model source: <https://github.com/trizkynoviandy/pima-indian-diabetes>
            ---
            """)

st.write("1. Pregnancies")
user_input_1 = st.text_input("Number of times pregnant")
st.write("2. Glucose")
user_input_2 = st.text_input("Plasma glucose concentration a 2 hours in an oral glucose tolerance test")
st.write("3. Blood Pressure")
user_input_3 = st.text_input("Diastolic blood pressure (mm Hg)")
st.write("4. Skin Thickness")
user_input_4 = st.text_input("Triceps skin fold thickness (mm)")
st.write("5. Insulin")
user_input_5 = st.text_input("2-Hour serum insulin (mu U/ml)")
st.write("6. Body Mass Index")
user_input_6 = st.text_input("Body mass index (weight in kg/(height in m)^2)")
st.write("7. Diabetes Pedigree Function")
user_input_7 = st.text_input("Diabetes pedigree function")
st.write("8. Age")
user_input_8 = st.text_input("Age (years)")

input_data = [[user_input_1, user_input_2, user_input_3, user_input_4, user_input_5, user_input_6, user_input_7, user_input_8]]

predict = st.button("Predict")
if predict:
    try:
        prediction = load_model.predict(input_data)
        st.success('Prediction Succesful!')
        if str(prediction) == "[0]":
            st.write("Result: NEGATIVE")
        else:
            st.write("Result: POSITIVE")
    except ValueError:
        st.write("Make sure you have entered all the required data")