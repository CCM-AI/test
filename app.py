import streamlit as st
import openai

# Set your OpenAI API key using Streamlit secrets
openai.api_key = st.secrets["general"]["openai_api_key"]

# Function to get AI response
def get_ai_response(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Title of the app
st.title("Chronic Care Management System")

# Patient Input Data
st.header("Patient Input Data")

age = st.number_input("Age:", min_value=0, max_value=120)
gender = st.selectbox("Gender:", ("Male", "Female", "Other"))
smoking_status = st.selectbox("Smoking Status:", ("Non-smoker", "Former smoker", "Current smoker"))
cholesterol = st.number_input("Cholesterol Level (mg/dL):", min_value=0)
blood_pressure = st.number_input("Blood Pressure (mmHg):", min_value=0)
blood_sugar = st.number_input("Blood Sugar Level (mg/dL):", min_value=0)
weight = st.number_input("Weight (kg):", min_value=0)
height = st.number_input("Height (cm):", min_value=0)
diagnosis = st.text_area("Chronic Condition Diagnosis:")

# AI-Driven Risk Stratification
st.header("AI-Driven Risk Stratification")

def risk_stratification(age, cholesterol, blood_pressure, blood_sugar):
    risk_score = (cholesterol / 200) + (blood_pressure / 120) + (blood_sugar / 100) + (age / 80)
    
    if risk_score < 1:
        risk_level = "Low Risk"
        risk_description = "Continue healthy lifestyle. Regular check-ups are recommended."
    elif 1 <= risk_score < 2:
        risk_level = "Moderate Risk"
        risk_description = "Monitor health closely. Consider lifestyle modifications."
    else:
        risk_level = "High Risk"
        risk_description = "Immediate action required. Consult with a healthcare provider."
    
    return risk_level, risk_description

risk_level, risk_description = risk_stratification(age, cholesterol, blood_pressure, blood_sugar)

st.write(f"**Risk Level:** {risk_level}")
st.write(f"**Risk Description:** {risk_description}")

# Personalized Care Plans
st.header("Personalized Care Plans")

if risk_level == "Low Risk":
    care_plan = "Maintain a healthy diet, exercise regularly, and have annual health screenings."
elif risk_level == "Moderate Risk":
    care_plan = "Adopt a balanced diet, increase physical activity, and have semi-annual health screenings."
else:
    care_plan = "Follow a strict diet, engage in regular exercise, and schedule monthly consultations with healthcare providers."

st.write(f"**Care Plan:** {care_plan}")

# Self-Management Support
st.header("Self-Management Support")

if risk_level == "Low Risk":
    steps = [
        "1. Continue healthy eating habits.",
        "2. Engage in at least 150 minutes of moderate exercise per week.",
        "3. Schedule yearly check-ups with your healthcare provider."
    ]
elif risk_level == "Moderate Risk":
    steps = [
        "1. Implement a heart-healthy diet.",
        "2. Aim for 30 minutes of physical activity most days.",
        "3. Regularly check your blood pressure and blood sugar."
    ]
else:
    steps = [
        "1. Follow a strict diet plan as prescribed.",
        "2. Participate in a structured exercise program.",
        "3. Monitor your health metrics daily and keep logs."
    ]

st.write("**Self-Management Steps:**")
for step in steps:
    st.write(step)

# Monitoring & Follow-Up
st.header("Monitoring & Follow-Up")

if risk_level == "Low Risk":
    follow_up = "Follow-up every 12 months."
elif risk_level == "Moderate Risk":
    follow_up = "Follow-up every 6 months."
else:
    follow_up = "Immediate follow-up in 1 month, then monthly thereafter."

st.write(f"**Follow-Up Schedule:** {follow_up}")

# Outcome Evaluation
st.header("Outcome Evaluation")

expected_outcomes = [
    "Improved health metrics.",
    "Reduction in symptoms.",
    "Enhanced quality of life."
]

st.write("**Expected Outcomes:**")
for outcome in expected_outcomes:
    st.write(outcome)

# AI Q&A Section
st.header("AI Q&A Section")

user_question = st.text_input("Ask a health-related question:")
if st.button("Get Answer"):
    if user_question:
        ai_answer = get_ai_response(user_question)
        st.write(f"**AI Response:** {ai_answer}")
    else:
        st.write("Please enter a question.")
