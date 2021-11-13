Experiment-4

In this experiment, the aim is to implement the Naive Bayes Algorithm to train a machine learning model which helps to predict whether a patient is highly likely to be diabetic or not. The dataset used for the preparation of the model, is taken from kaggle namely, Pima Indians Diabetes Database. The dataset contains numerous patient's medical details like Glucose, Blood Pressure, Insulin, Skin Thickness, Age, etc.
To train the model, the data set was split into an 80:20 ratio and was trained on the 80% of data and the rest was kept as test data. Using the Naive Bayes Algorithm, the probabilities for each individual feature were calculated. Then using the test data, I calculated the accuracy of the model trained which came around 70-80%. 
An ambiguity observed in the model I trained was, for certain values present in the test data and absent from the data used for training the model, the probability assigned was zero and the prediction couldn't be made. For such cases, the model needed to be trained again with these data included in training set.