# UAV Project - Applied Roots

Unmanned aerial vehicles (UAVs) have attracted unprecedented interest and have grown to be a widely used technology. However, because of their constrained computing and communication capabilities, drone networks are vulnerable to a variety of cyber-intrusions and threats. UAVs are especially vulnerable because the majority of signals they get are over wifi data. To determine if the drone is a UAV or an Anamoly, a classification model might be utilized. We may address the issues caused by unauthorized UAVs by using binary classification model metrics to know the model's performance and deploying the model in real-time.

A catboost model is been build to solve this problem and able to obtain **1 recall** and **1 precision**. 

The usage of files is provided below 

##### 1. Requirements.txt 

##### 2. Data Folder - 

The datasets are combinations between different UAV types and traffic modes.

![Image](https://github.com/[Sanjay-Suthraye]/[uav-project]/blob/[main]/capture.jpg?raw=true)

In this project we are using **Bi Directional Flow Data**.

##### 3. Python Model Building file - **EDA_and_Model_Error Analysis_96.ipynb**

This file consists of the EDA, Catboost Model & Shap Analysis

##### 4. Deployment file - **uav-app.py**

Consists of Code files build using Streamlit and deployed on Heroku.
