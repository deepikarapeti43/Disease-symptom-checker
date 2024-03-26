## Disease Symptom Checker

## Overview

This project is centered on developing a machine learning model that could predict disease (target) based off of a set of symptoms (features).

The data were retreived from Kaggle. The first of two .csv files contained a column of diseases and 17 additional columns that contained symptoms. The second .csv file contain remedies associated with each diesase. The data were loaded into jupyter notebook using a sqlite database. Once loaded the data were cleaned and standardized. White space was removed from string values, recoded, and then standardized using the standard scaler.

The team utilized multiple machine learning algorithms to determine the best fit for the data described above. The three algorithms tested included: 

1. **Decision Tree**
2. **Random Forest Classifier**
3. **Logistic Regression**

Each algorithm was evaluated for its performance on the dataset to determine its effectiveness in solving the problem at hand.

## Methodology

1. **Selection of Algorithms:** The team chose these three algorithms based on their suitability for the task and their different approaches to modeling the data.

2. **Testing and Evaluation:** The dataset was divided into training and testing sets, and each algorithm was trained on the training data and evaluated on the test data. Performance metrics such as accuracy, precision, recall, and F1-score were used to assess the models.

3. **Optimization:** After initial testing, the models were optimized to enhance their performance. Optimization techniques, including hyperparameter tuning and feature engineering, were employed to improve the models' predictive capabilities.

4. **Comparison:** The performance of each optimized model was compared to determine the most effective algorithm for the dataset. This comparison guided the selection of the final model for deployment or further analysis.

### Results

The analysis yielded insights into the strengths and weaknesses of each algorithm, providing valuable information for decision-making in model selection and deployment.
Each model was then optimized for performance.

Additionally, a data visualization tool, Streamlit, was used to show how the input of the various symptoms predicted disease, and the precautions that should be taken for each disease predicted.

## Developed Disease Symptom Checker Web App:
** Objective:**
To create a web application that allows users to input symptoms and receive suggestions for possible diseases along with remedies.

** Overview of tools and libraries used:**
  Streamlit: For building the interactive web application.

  Pandas: For data manipulation and analysis.

  PIL (Python Imaging Library): For handling image files.

  PostgreSQL: For data cleansing and preprocessing.

** User Inputs:**
Select gender using a dropdown.
Enter age using a numeric input field.
Input symptoms using a text input box.

** Output:**
Success message for suggested diseases.
Subheaders and remedy lists for each suggested disease.
Information message if no matching diseases are found.
Warning message if symptoms are not provided.
Warning message if age is below 14 yrs old.

Here is the link to the App : http://192.168.0.11:8501/

## Data Visualizations using Tableau:
https://public.tableau.com/app/profile/deepak.adari1615/viz/Diseasesymptomchecker/Story1

## Google documention:
https://docs.google.com/document/d/1sVMmcmleB0XUTIAwtON-VRb7RAYU554BMuHMnAr2JJA/edit

## Project Presentation:
https://onedrive.live.com/edit?id=695F4863786D5C8A!14223&resid=695F4863786D5C8A!14223&ithint=file%2cpptx&authkey=!AAyH-bj8LOpzhV8&wdo=2&cid=695f4863786d5c8a




