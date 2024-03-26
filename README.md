## Disease Symptom Checker

## Overview

This project is centered on developing a machine learning model that could predict disease (target) based off of a set of symptoms (features).

The data were retreived from Kaggle. The first of two .csv files contained a column of diseases and 17 additional columns that contained symptoms. The second .csv file contain remedies associated with each diesase. The data were loaded into jupyter notebook using a sqlite database. Once loaded the data were cleaned and standardized. White space was removed from string values, recoded, and then standardized using the standard scaler.

The team utilized multiple machine learning algorithms to determine the best fit for the data described above. The three algorithms tested included: decision tree, random forest, and logistic regression.

Each model was then optimized for performance.

Additionally, a data visualization tool, Streamlit, was used to show how the input of the various symptoms predicted disease, and the precautions that should be taken for each disease predicted.

Developed Disease Symptom Checker Web App
* Objective: 
To create a web application that allows users to input symptoms and receive suggestions for possible diseases along with remedies.

* Overview of tools and libraries used:
Streamlit: For building the interactive web application.
Pandas: For data manipulation and analysis.
PIL (Python Imaging Library): For handling image files.

* User Inputs:
Select gender using a dropdown.
Enter age using a numeric input field.
Input symptoms using a text input box.

* Output :
Success message for suggested diseases.
Subheaders and remedy lists for each suggested disease.
Information message if no matching diseases are found.
Warning message if symptoms are not provided.
Warning message if age is below 14 yrs old.

Here is the link to the App : http://192.168.0.11:8501/


