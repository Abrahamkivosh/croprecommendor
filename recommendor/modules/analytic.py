import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

class CropRecommendor():
    def __init__(self,nitrogen=0,phosphorus=0,potassium=0,temperature=0.0,humidity=0.0,ph=0.0,rainfall=0):
        self.N = nitrogen
        self.P = phosphorus
        self.K = potassium
        self.temp = temperature
        self.humi = humidity
        self.ph = ph
        self.rf = rainfall
        
        
    def analyse_data(self):
        df = pd.read_csv("static/Crop_recommendation.csv")
        features = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
        target = df['label']
        labels = df['label']
        # acc = []
        # model=[]

        Xtrain, Xtest, Ytrain, Ytest = train_test_split(features, target, test_size=0.2, random_state=2)

        # Random Forest Classification
        RF = RandomForestClassifier()
        RF.fit(Xtrain, Ytrain)
        sample = [[self.N, self.P, self.K, self.temp, self.humi, self.ph, self.rf]]
        sample_data = np.array(sample)
        prediction = RF.predict(sample_data)
        return prediction
            