# Created by Devesh Singh (Demonforms)
import streamlit as st
from PredictorUtility import PredictorUtility

class PremiumPredictorApp(object):
    def __init__(self):
        # Define the page layout
        st.markdown(
            "<h1 style='white-space: nowrap;'>Health Insurance Premium Predictor</h1>",
            unsafe_allow_html=True)
        st.markdown(
            f"<p style='text-align: center; font-size:14px; color:lightgray;'>"
            f"Project by <b>Devesh Singh</b>"
            f"</p>",
            unsafe_allow_html=True
        )
        # Create four rows of three columns each
        self.row1 = st.columns(3)
        self.row2 = st.columns(3)
        self.row3 = st.columns(3)
        self.row4 = st.columns(4)
        self.predictor = PredictorUtility()
        self.initiate_categorical_options()
        
    def initiate_categorical_options(self):
        self.categorical_options = {
            'Gender': ['Male', 'Female'],
            'Marital Status': ['Unmarried', 'Married'],
            'Physical Activity': ['Low', 'Medium', 'High'],
            'Stress Level': ['Low', 'Medium', 'High'],
            'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
            'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
            'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', 'Unemployed'],
            'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
            'Medical History': [
                'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
                'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
                'Diabetes & Heart disease'
            ],
            'Insurance Plan': ['Bronze', 'Silver', 'Gold']
        }

    def initiate_grid(self):
        # Assign inputs to the grid
        with self.row1[0]:
            age = st.number_input('Age', min_value=18, step=1, max_value=100)
        with self.row1[1]:
            number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
        with self.row1[2]:
            income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

        with self.row2[0]:
            physical_acitivity = st.selectbox('Physical Activity', self.categorical_options['Physical Activity'])
        with self.row2[1]:
            stress_level = st.selectbox('Stress Level', self.categorical_options['Stress Level'])
        with self.row2[2]:
            medical_history = st.selectbox('Medical History', self.categorical_options['Medical History'])

        with self.row3[0]:
            gender = st.selectbox('Gender', self.categorical_options['Gender'])
        with self.row3[1]:
            marital_status = st.selectbox('Marital Status', self.categorical_options['Marital Status'])
        with self.row3[2]:
            employment_status = st.selectbox('Employment Status', self.categorical_options['Employment Status'])

        with self.row4[0]:
            smoking_status = st.selectbox('Smoking Status', self.categorical_options['Smoking Status'])
        with self.row4[1]:
            region = st.selectbox('Region', self.categorical_options['Region'])
        with self.row4[2]:
            insurance_plan = st.selectbox('Insurance Plan', self.categorical_options['Insurance Plan'])
        with self.row4[3]:
            bmi_category = st.selectbox('BMI Category', self.categorical_options['BMI Category'])
        # Create a dictionary for input values
        self.input_dict = {
            'Age': age,
            'Number of Dependants': number_of_dependants,
            'Income in Lakhs': income_lakhs,
            'Physical Activity': physical_acitivity,
            'Stress Level': stress_level,
            'Insurance Plan': insurance_plan,
            'Employment Status': employment_status,
            'Gender': gender,
            'Marital Status': marital_status,
            'BMI Category': bmi_category,
            'Smoking Status': smoking_status,
            'Region': region,
            'Medical History': medical_history
        }

    def run(self):
        # Button to make prediction
        if st.button('Predict'):
            prediction = self.predictor.predict(self.input_dict)
            st.success(f'Predicted Health Insurance Cost: {prediction} INR')


if __name__ == "__main__":
    predictor = PremiumPredictorApp()
    predictor.initiate_grid()
    predictor.run()