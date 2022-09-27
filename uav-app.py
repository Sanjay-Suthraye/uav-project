# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 01:10:44 2022

@author: sanja
"""

from catboost import CatBoostClassifier
import streamlit as st
import pandas as pd
import joblib
import pipreqs


#pipreqs C:/Users/sanja/spyder files/uav project - IN CMD

#Loading up the Regression model we created
model = CatBoostClassifier()
model.load_model('catboost_model_AP.json')
scaling_fn=joblib.load('catboost_scaling_AP.bin')


#st.cache
#streamlit run "C:\Users\sanja\spyder files\uav project\uav_deployment.py"

#Caching the model for faster loading
st.title('Unmanned Aerial Vehicle (UAV) Intrusion Detection')
st.subheader('By Sanjay Suthraye')

st.text('The Current Model can predict if the provided drone is a UAV or Not?')
st.text('Mention the drone data for below 54 columns')

#pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]], columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z'])

def predict(col_1,	col_2,	col_3,	col_4,	col_5,	col_6,	col_7,	col_8,	col_9,	col_10,	col_11,	col_12,	col_13,	col_14,	col_15,	col_16,	col_17,	col_18,	col_19,	col_20,	col_21,	col_22,	col_23,	col_24,	col_25,	col_26,	col_27,	col_28,	col_29,	col_30,	col_31,	col_32,	col_33,	col_34,	col_35,	col_36,	col_37,	col_38,	col_39,	col_40,	col_41,	col_42,	col_43,	col_44,	col_45,	col_46,	col_47,	col_48,	col_49,	col_50,	col_51,	col_52,	col_53,	col_54):
    data = pd.DataFrame([[col_1, col_2,	col_3,	col_4,	col_5,	col_6,	col_7,	col_8,	col_9,	col_10,	col_11,	col_12,	col_13,	col_14,	col_15,	col_16,	col_17,	col_18,	col_19,	col_20,	col_21,	col_22,	col_23,	col_24,	col_25,	col_26,	col_27,	col_28,	col_29,	col_30,	col_31,	col_32,	col_33,	col_34,	col_35,	col_36,	col_37,	col_38,	col_39,	col_40,	col_41,	col_42,	col_43,	col_44,	col_45,	col_46,	col_47,	col_48,	col_49,	col_50,	col_51,	col_52,	col_53,	col_54]],columns=['col_1',	'col_2',	'col_3',	'col_4',	'col_5',	'col_6',	'col_7',	'col_8',	'col_9',	'col_10',	'col_11',	'col_12',	'col_13',	'col_14',	'col_15',	'col_16',	'col_17',	'col_18',	'col_19',	'col_20',	'col_21',	'col_22',	'col_23',	'col_24',	'col_25',	'col_26',	'col_27',	'col_28',	'col_29',	'col_30',	'col_31',	'col_32',	'col_33',	'col_34',	'col_35',	'col_36',	'col_37',	'col_38',	'col_39',	'col_40',	'col_41',	'col_42',	'col_43',	'col_44',	'col_45',	'col_46',	'col_47',	'col_48',	'col_49',	'col_50',	'col_51',	'col_52',	'col_53',	'col_54'])

    
    tranf_data = scaling_fn.transform(data)
    print(tranf_data.shape)
    y_value = model.predict(tranf_data)
    
    return y_value
    


col_1 = st.number_input('col_1:', min_value=0.0001, max_value=2255.797)
col_2 = st.number_input('col_2:', min_value=0.00, max_value=4195.147)
col_3 = st.number_input('col_3:', min_value=9.99, max_value=505.0615)
col_4 = st.number_input('col_4:', min_value=0.00, max_value=748.804)
col_5 = st.number_input('col_5:', min_value=-3.2779, max_value=9.33624153199995)
col_6 = st.number_input('col_6:', min_value=-2.75, max_value=86.3997624592538)
col_7 = st.number_input('col_7:', min_value=0.0, max_value=20145.118076)
col_8 = st.number_input('col_8:', min_value=-0.0, max_value=342.0766)

col_9 = st.number_input('col_9:', min_value=0.0002365625, max_value=4378.13022591564)
col_10 = st.number_input('col_10:', min_value=64.1754385964912, max_value=1667.20833333333)
col_11 = st.number_input('col_11:', min_value=0.2425356, max_value=1032.376)
col_12 = st.number_input('col_12:', min_value=62.0, max_value=1676.0)
col_13 = st.number_input('col_13:', min_value=0.0, max_value=1082.298)
col_14 = st.number_input('col_14:', min_value=-8.72678401176836, max_value=6.652461)
col_15 = st.number_input('col_15:', min_value=-2.75, max_value=75.0727245687091)
col_16 = st.number_input('col_16:', min_value=70.0, max_value=1676.0)
col_17 = st.number_input('col_17:', min_value=62.0, max_value=1676.0)
col_18 = st.number_input('col_18:', min_value=64.9755689579053, max_value=1667.74139931825)
col_19 = st.number_input('col_19:', min_value=2.77, max_value=314.790735453125)
col_20 = st.number_input('col_20:', min_value=6.00, max_value=2181.02669254236)
col_21 = st.number_input('col_21:', min_value=1.99, max_value=66.7764200000001)
col_22 = st.number_input('col_22:', min_value=0.0, max_value=64.0600607094006)

col_23 = st.number_input('col_23:', min_value=-1.852649, max_value=9.598504)
col_24 = st.number_input('col_24:', min_value=-2.75, max_value=91.0608214905017)
col_25 = st.number_input('col_25:', min_value=0.000, max_value=17173.680336)
col_26 = st.number_input('col_26:', min_value=-0.000, max_value=1.142084544)
col_27 = st.number_input('col_27:', min_value=6.338, max_value=2181.05977973254)
col_28 = st.number_input('col_28:', min_value=63.8478260869565, max_value=1675.683)
col_29 = st.number_input('col_29:', min_value=0.205195670417031, max_value=765.396075744829)
col_30 = st.number_input('col_30:', min_value=61.0, max_value=1676.0)
col_31 = st.number_input('col_31:', min_value=0.0, max_value=1137.1542)
col_32 = st.number_input('col_32:', min_value=-9.54634744950372, max_value=9.598511)
col_33 = st.number_input('col_33:', min_value=-2.75, max_value=91.0609121199509)
col_34 = st.number_input('col_34:', min_value=70.0, max_value=1676.0)
col_35 = st.number_input('col_35:', min_value=61.0, max_value=1664.0)

col_36 = st.number_input('col_36:', min_value=64.1404708432983, max_value=1675.68440412335)
col_37 = st.number_input('col_37:', min_value=0.000138879999999517, max_value=225.5675)
col_38 = st.number_input('col_38:', min_value=4.65273, max_value=1606.23964059326)
col_39 = st.number_input('col_39:', min_value=9.9999, max_value=66.7613154999999)
col_40 = st.number_input('col_40:', min_value=3.371, max_value=89.3036815607993)
col_41 = st.number_input('col_41:', min_value=-0.88, max_value=9.84889808980961)
col_42 = st.number_input('col_42:', min_value=-2.01, max_value=98.0039489478187)
col_43 = st.number_input('col_43:', min_value=0.00, max_value=16033.855624)
col_44 = st.number_input('col_44:', min_value=-0.00, max_value=0.000963)
col_45 = st.number_input('col_45:', min_value=0.00, max_value=1607.4059374986)
col_46 = st.number_input('col_46:', min_value=68.4, max_value=1620.64)
col_47 = st.number_input('col_47:', min_value=1.79, max_value=758.536105024845)
col_48 = st.number_input('col_48:', min_value=62.0, max_value=1676.0)
col_49 = st.number_input('col_49:', min_value=0.0, max_value=1137.1542)
col_50 = st.number_input('col_50:', min_value=-5.96, max_value=9.67432830648289)
col_51 = st.number_input('col_51:', min_value=-2.01, max_value=92.70316)
col_52 = st.number_input('col_52:', min_value=138.0, max_value=1676.0)
col_53 = st.number_input('col_53:', min_value=61.0, max_value=304.0)
col_54 = st.number_input('col_54:', min_value=71.44, max_value=1635.99)



if st.button('Predict Class'):
    value = predict(col_1,	col_2,	col_3,	col_4,	col_5,	col_6,	col_7,	col_8,	col_9,	col_10,	col_11,	col_12,	col_13,	col_14,	col_15,	col_16,	col_17,	col_18,	col_19,	col_20,	col_21,	col_22,	col_23,	col_24,	col_25,	col_26,	col_27,	col_28,	col_29,	col_30,	col_31,	col_32,	col_33,	col_34,	col_35,	col_36,	col_37,	col_38,	col_39,	col_40,	col_41,	col_42,	col_43,	col_44,	col_45,	col_46,	col_47,	col_48,	col_49,	col_50,	col_51,	col_52,	col_53,	col_54)
    st.success(f'The predicted class is {value[0]}')
    
    if value >0.5:
        st.text("According to the provided Wifi Data, the Drone is a UAV")
    else:
        st.text("According to the provided Wifi Data, the Drone is not a UAV")