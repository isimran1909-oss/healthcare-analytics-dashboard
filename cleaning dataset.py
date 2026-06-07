import pandas as pd
import numpy as np

df=pd.read_csv("c:/Users/dell/OneDrive/Documents/Data science projects/Healthcare data/healthcare_dirty.csv")
hel=df.copy()

#age cleaning

hel=hel[(hel['Age'] >=1 )& (hel['Age'] <=100)]
hel['Age']=hel['Age'].fillna(hel['Age'].mode()[0]).astype("int16")
# print(hel['Age'].to_string())

#cleaning of blood group

hel['Blood_Group']=hel['Blood_Group'].fillna(hel['Blood_Group'].mode()[0]).astype("str")
# print(hel['Blood_Group'].unique())

#cleaning Discharge date

hel['Discharge_Date']=pd.to_datetime(hel['Discharge_Date'], errors='coerce')
hel['Discharge_Date']=hel['Discharge_Date'].fillna(hel['Discharge_Date'].mode()[0])
hel['Discharge_Date']=hel['Discharge_Date'].dt.strftime("%d-%m-%Y")
# print(hel['Discharge_Date'].to_string())

# Billing_Amount
hel=hel[(hel['Billing_Amount'] >=50)]
hel['Billing_Amount']=hel['Billing_Amount'].fillna(hel['Billing_Amount'].median())
# print(hel['Billing_Amount'].to_string())

# cleaning doctor name and blood prssure

hel['Doctor_Name']=hel['Doctor_Name'].fillna(hel['Doctor_Name'].mode()[0])


# print(hel['Blood_Group'].dtype)
import numpy as np
import pandas as pd

# Remove mmHg
hel['Blood_Pressure'] = hel['Blood_Pressure'].astype(str)
hel['Blood_Pressure'] = hel['Blood_Pressure'].str.replace(' mmHg', '', regex=False)

# Split blood pressure
hel[['systolic_bp', 'diastolic_bp']] = hel['Blood_Pressure'].str.split('/', expand=True)

# Convert to numeric
hel['systolic_bp'] = pd.to_numeric(hel['systolic_bp'], errors='coerce')
hel['diastolic_bp'] = pd.to_numeric(hel['diastolic_bp'], errors='coerce')

# Mark invalid readings as NaN
mask = hel['systolic_bp'] < hel['diastolic_bp']
hel.loc[mask, ['systolic_bp', 'diastolic_bp']] = np.nan

# Fill missing values with median
hel['systolic_bp'] = hel['systolic_bp'].fillna(hel['systolic_bp'].median())
hel['diastolic_bp'] = hel['diastolic_bp'].fillna(hel['diastolic_bp'].median())

# Optional: Drop original column
hel.drop('Blood_Pressure', axis=1, inplace=True)

# gender cleaning

hel['Gender']=hel['Gender'].replace({'F':'Female','f':'Female','female':'Female','FEMALE':'Female',
                                         'm':'Male','M':'Male','MALE':'Male','male':'Male'})
# print(hel['Gender'].value_counts())

# print(hel.isnull().sum())
# print(hel.to_string())

# cleaning Diagnosis
hel['Diagnosis']=hel['Diagnosis'].str.strip()
hel.loc[hel['Diagnosis']=='Cancer','Diagnosis']='Cancer'
hel.loc[hel['Diagnosis']=='COVID-19','Diagnosis']='Covid-19'
hel.loc[hel['Diagnosis']=='COVID19','Diagnosis']='Covid-19'
hel.loc[hel['Diagnosis']=='DIABETES','Diagnosis']='Diabetes'
hel.loc[hel['Diagnosis']=='diabetes','Diagnosis']='Diabetes'
hel.loc[hel['Diagnosis']=='heart disease','Diagnosis']='Heart Disease'
hel.loc[hel['Diagnosis']=='Hypertension','Diagnosis']='Hypertension'


# print(hel['Diagnosis'].unique())
# print(hel['Diagnosis'].value_counts())

hel.to_csv("c:/Users/dell/OneDrive/Documents/Data science projects/Healthcare data/healthcare_cleaned1.csv")