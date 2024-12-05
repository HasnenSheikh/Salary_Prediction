import streamlit as st
import joblib
import numpy as np

st.title('Salary Prediction App')

st.divider()

st.write("With this app, you can get estimation for the salaries of the company employeess")

years = st.number_input('Enter the years at Company',value=1, step=1, min_value=0)
jobrate = st.number_input('Enter the job rate',value=3.5, step=0.5, min_value=0.0)

X = [years,jobrate]

st.divider()

predict = st.button('Click the button for salary prediction')

st.divider()

model = joblib.load('linear_model.pkl')

if predict:

    st.balloons()
    
    X2 = np.array([X])

    prediction = model.predict(X2)[0]

    st.write(f"Salary Prediction is {prediction:,.2f}")

    
else:
    "Please press the button for the app to make prediction"