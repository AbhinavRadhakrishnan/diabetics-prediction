import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import Settings
from crew import diabetes_prediction_crew

settings = Settings()

def run(patient_data: dict):
    result = diabetes_prediction_crew.kickoff(inputs={"patient_data": patient_data})
    print(result)


if __name__ == "__main__":
    patient_diabetic = {
        "Pregnancies": 3,
        "Glucose": 150,
        "BloodPressure": 80,
        "SkinThickness": 25,
        "Insulin": 100,
        "BMI": 30.5,
        "DiabetesPedigreeFunction": 0.6,
        "Age": 40
    }

    # Example patient 2 - Likely Non-Diabetic
    patient_non_diabetic = {
        "Pregnancies": 1,
        "Glucose": 95,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 85,
        "BMI": 22.5,
        "DiabetesPedigreeFunction": 0.2,
        "Age": 25
    }

    run(patient_diabetic)
    print("-"*50)
    run(patient_non_diabetic)
