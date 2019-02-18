#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 13:13:24 2019

@author: yang.2677a
"""

# importing modules
import sklearn 
from sklearn.datasets import load_breast_cancer 
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import accuracy_score 

# loading and managing the dataset 
data = load_breast_cancer() 
label_names = data['target_names'] 
labels = data['target'] 
feature_names = data['feature_names'] 
features = data['data'] 
train, test, train_labels, test_labels = train_test_split(features, labels, 
                                       test_size = 0.33, random_state = 42) 

# visualize the data 
print "Label names:".add(label_names)
print(feature_names) 

# training
gnb = GaussianNB() 
model = gnb.fit(train, train_labels) 

# making the predictions 
predictions = gnb.predict(test) 

print(accuracy_score(test_labels, predictions)) 