COPY (SELECT DISTINCT diseasename, symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9, symptom10 FROM diseases) 
TO 'E:\Project 4\DiseaseandSymptoms.csv' WITH CSV HEADER;

