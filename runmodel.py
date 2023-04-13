from tensorflow import keras
import numpy as np
import pandas as pd
import os

feature_cols_index={'age':0, 'hypertension':1, 'heart_disease':2, 'ever_married':3,
       'Residence_type':4, 'avg_glucose_level':5, 'bmi':6, 'gender_Female':7,
       'gender_Male':8, 'gender_Other':9, 'work_type_Govt_job':10,
       'work_type_Never_worked':11, 'work_type_Private':12,
       'work_type_Self-employed':13, 'work_type_children':14,
       'smoking_status_Unknown':15, 'smoking_status_formerly smoked':16,
       'smoking_status_never smoked':17, 'smoking_status_smokes':18}

absolute_path = os.path.dirname(__file__)
relative_path = "Stroke_prediction.h5"
full_path = os.path.join(absolute_path, relative_path)

model=keras.models.load_model(full_path)

def strokepred():

 features=np.zeros(19)
 features=features.reshape(-1,19)

 info=float(input("\nEnter Age : "))
 features[0][0]=info

 info=int(input("\nHypertension (Yes=1/No=0): "))
 features[0][1]=info

 info=int(input("\nHeart disease (Yes=1/No=0): "))
 features[0][2]=info

 info=int(input("\nEver married? (Yes=1/No=0): "))
 features[0][3]=info

 info=int(input("\nResidence Type : (Urban = 1 / Rural = 0 ) : "))
 features[0][4]=info

 info=float(input("\nEnter Avg Glucose level : "))
 features[0][5]=info

 info=float(input("\nEnter Bmi  : "))
 features[0][6]=info

 info=int(input("\nGender : (Female  = 1 / Male = 2 / Other = 3  ) : "))
 if info==1:
    features[0][7]=1
 elif info==2:
    features[0][8]=1
 elif info==3:
    features[0][9]=1    

 info=int(input('''\nWork type... 
 Govt. Job = 1 
 Never worked = 2 
 Private = 3 
 Self-Employed = 4 
 Children = 5
 \n Enter your input :  '''))

 if info==1:
    features[0][10]=1
 elif info==2:
    features[0][11]=1
 elif info==3:
    features[0][12]=1
 elif info==4:
    features[0][13]=1
 elif info==5:
    features[0][14]=1

 info=int(input('''\nSmoking Status... 
 Unknown = 1 
 Formerly smoked = 2 
 Never smoked = 3 
 Smokes = 4 
 \n Enter your input :'''))

 if info==1:
    features[0][15]=1
 elif info==2:
    features[0][16]=1
 elif info==3:
    features[0][17]=1
 elif info==4:
    features[0][18]=1
        
 
 print("\nData retrieved... generating output\n")

 label=model.predict(features)
 if label>0.5:
    print("Stroke probable!")
 else:
    print("Stroke not probable.")


strokepred()
