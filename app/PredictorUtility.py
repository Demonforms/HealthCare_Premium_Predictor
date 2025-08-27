# Created by Devesh Singh (Demonforms)
import pandas as pd
import joblib
from pathlib import Path

class PredictorUtility(object):
    def __init__(self):
        model_details = joblib.load(Path("model/model.joblib"))
        self.model = model_details.get("model")
        self.scaler = model_details.get("scaler")
        self.expected_cols = model_details.get("expected_cols")
        self.cols_to_scale = model_details.get("cols_to_scale")

    @staticmethod
    def calculate_life_style_risk(physical_activity, stress):
        physical_activity_risk_score = {
            "High": 0,
            "Medium": 1,
            "Low": 4
        }
        stress_risk_score = {
            "High": 4,
            "Medium": 1,
            "Low": 0
        }
        life_style_risk = physical_activity_risk_score[physical_activity] + stress_risk_score[stress]
        return life_style_risk

    @staticmethod
    def calculate_normalized_risk(medical_history):
        risk_scores = {
            "diabetes": 6,
            "heart disease": 8,
            "high blood pressure": 6,
            "thyroid": 5,
            "no disease": 0,
            "none": 0
        }
        # Split the medical history into potential two parts and convert to lowercase
        diseases = medical_history.lower().split(" & ")

        # Calculate the total risk score by summing the risk scores for each part
        total_risk_score = sum(risk_scores.get(disease, 0) for disease in diseases)  # Default to 0 if disease not found

        max_score = 14 # risk score for heart disease (8) + second max risk score (6) for diabetes or high blood pressure
        min_score = 0  # Since the minimum score is always 0

        # Normalize the total risk score
        normalized_risk_score = (total_risk_score - min_score) / (max_score - min_score)

        return normalized_risk_score

    def preprocess_input(self, input_dict):
        # Define the expected columns and initialize the DataFrame with zeros

        insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}

        df = pd.DataFrame(0, columns=self.expected_cols, index=[0])
        # df.fillna(0, inplace=True)

        # Manually assign values for each categorical input based on input_dict
        for key, value in input_dict.items():
            if key == 'Gender' and value == 'Male':
                df['gender_Male'] = 1
            elif key == 'Region':
                if value == 'Northwest':
                    df['region_Northwest'] = 1
                elif value == 'Southeast':
                    df['region_Southeast'] = 1
                elif value == 'Southwest':
                    df['region_Southwest'] = 1
            elif key == 'Marital Status' and value == 'Unmarried':
                df['marital_status_Unmarried'] = 1
            elif key == 'BMI Category':
                if value == 'Obesity':
                    df['bmi_category_Obesity'] = 1
                elif value == 'Overweight':
                    df['bmi_category_Overweight'] = 1
                elif value == 'Underweight':
                    df['bmi_category_Underweight'] = 1
            elif key == 'Smoking Status':
                if value == 'Occasional':
                    df['smoking_status_Occasional'] = 1
                elif value == 'Regular':
                    df['smoking_status_Regular'] = 1
            elif key == 'Employment Status':
                if value == 'Salaried':
                    df['employment_status_Salaried'] = 1
                elif value == 'Self-Employed':
                    df['employment_status_Self-Employed'] = 1
            elif key == 'Insurance Plan':  # Correct key usage with case sensitivity
                df['insurance_plan'] = insurance_plan_encoding.get(value, 1)
            elif key == 'Age':  # Correct key usage with case sensitivity
                df['age'] = value
            elif key == 'Number of Dependants':  # Correct key usage with case sensitivity
                df['number_of_dependants'] = value
            elif key == 'Income in Lakhs':  # Correct key usage with case sensitivity
                df['income_lakhs'] = value

        # Calculate normalized risk score through medical history given by input
        df['normalized_risk_score'] = self.calculate_normalized_risk(input_dict['Medical History'])
        # calculate life style risk through physical activity and stress level
        df['lifestyle_risk_score'] = self.calculate_life_style_risk(input_dict['Physical Activity'], input_dict['Stress Level'])
        df = self.handle_scaling(input_dict['Age'], df)

        return df

    def handle_scaling(self, age, df):
        # scale age and income_lakhs column

        df['income_level'] = None # since scaler object expects income_level supply it. This will have no impact on anything
        df[self.cols_to_scale] = self.scaler.transform(df[self.cols_to_scale])

        df.drop('income_level', axis = 1, inplace=True)

        return df

    def predict(self, input_dict):
        input_df = self.preprocess_input(input_dict)

        prediction = self.model.predict(input_df)

        return int(prediction[0])
