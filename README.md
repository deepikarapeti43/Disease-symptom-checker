This project centered on developing a machine learning model that could predict disease (target) based off of a set of symptoms (features).

The data were retreived from Kaggle. The first of two .csv files contained a column of diseases and 17 additional columns that contained symptoms. The second .csv file contain precautions associated with each diesase. The data were loaded into jupyter notebook using a sqlite database. Once loaded the data were cleaned and standardized. White space was removed from string values, recoded, and then standardized using the standard scaler.

The team utilized multiple machine learning algorithms to determine the best fit for the data described above. The three algorithms tested included: decision tree, random forest, and logistic regression.

Each model was then optimized for performance.

Additionally, a data visualization tool, Streamlit, was used to show how the input of the various symptoms predicted disease, and the precautions that should be taken for each disease predicted.