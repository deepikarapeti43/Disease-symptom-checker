import streamlit as st
import pandas as pd
from PIL import Image

# Read the dataset
data = pd.read_csv(r"E:\Project 4\Disease-symptom-checker\disease_and_symptoms_data\DiseaseandSymptoms_new.csv")
remedies_data = pd.read_csv(r"E:\Project 4\Disease-symptom-checker\disease_and_symptoms_data\Disease precaution.csv")

# Create a dictionary to store precautions for each disease
remedies_dict = dict(zip(remedies_data['Disease'], remedies_data.iloc[:, 1:].values.tolist()))


# Create a dictionary to store precautions for each disease

def check_symptoms(symptoms):
    possible_diseases = []
    for index, row in data.iterrows():
        disease_symptoms = [str(symptom).strip().lower() for symptom in row[1:].dropna().tolist()]
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
        user_symptoms = [s.strip() for s in symptoms_input.split(',')]  
        if age < 14:
            st.warning("Please consult a doctor as the patient is less than 14 years old.")
        else:
            suggested_diseases = check_symptoms(user_symptoms)
            unique_diseases = set(suggested_diseases)
            if unique_diseases:
                st.success(f"Suggested diseases: {', '.join(unique_diseases)}")
                for disease in unique_diseases:
                    st.subheader(f"Remedies for {disease}:")
                    remedies = remedies_dict.get(disease, "Remedies not available")
                    for index, remedy in enumerate(remedies, 1):
                        st.write(remedy)
            else:
                st.info("No matching diseases found.")
    else:
        st.warning("Please enter your symptoms.")


        
        