import streamlit as st
import pandas as pd
from PIL import Image

# Read the dataset
data = pd.read_csv(r"E:\Project 4\Disease-symptom-checker\disease_and_symptoms_data\DiseaseandSymptoms_new.csv")
precautions_data = pd.read_csv(r"E:\Project 4\Disease-symptom-checker\disease_and_symptoms_data\Disease precaution.csv")

# Create a dictionary to store precautions for each disease
precautions_dict = dict(zip(precautions_data['Disease'], precautions_data.iloc[:, 1:].values.tolist()))


# Create a dictionary to store precautions for each disease

def check_symptoms(symptoms):
    possible_diseases = []
    for index, row in data.iterrows():
        disease_symptoms = [symptom.strip().lower() for symptom in row[1:].dropna().tolist()]  # Make case-insensitive and strip spaces
        print("Disease Symptoms:", disease_symptoms)  # Debugging statement
        print("User Symptoms:", symptoms)  # Debugging statement
        if set(symptoms).issubset(disease_symptoms):
            possible_diseases.append(row['diseasename'])
    return possible_diseases

# Streamlit app
st.title("Disease Symptom Checker")

# Set background image
background_image = Image.open(r"E:\Project 4\Disease-symptom-checker\disease_and_symptoms_data\new.jpg")
st.image(background_image, use_column_width=True)

st.write(
    """
    This app allows you to enter your symptoms and receive suggestions for possible diseases.
    Simply enter your symptoms in the text box below, select your gender, and enter your age.
    Then click the "Check Symptoms" button to see the suggested diseases.
    
    """
)


# User input for gender
gender = st.selectbox("Select your gender", ["Male", "Female"])

# User input for age range
age = st.number_input("Enter your age", min_value=1, max_value=150, value=20)


# User input for symptoms
symptoms_input = st.text_input("Enter your symptoms", "")

if st.button("Check Symptoms"):
    if symptoms_input:
        user_symptoms = [s.strip() for s in symptoms_input.split(',')]  # Strip spaces from input
        suggested_diseases = check_symptoms(user_symptoms)
        unique_diseases = set(suggested_diseases)
        if unique_diseases:
            st.success(f"Suggested diseases: {', '.join(unique_diseases)}")
            for disease in unique_diseases:
                st.subheader("Precautions for {}: ".format(disease))
                st.write(precautions_dict.get(disease, "Precautions not available"))
        else:
            st.info("No matching diseases found.")
    else:
        st.warning("Please enter your symptoms.")