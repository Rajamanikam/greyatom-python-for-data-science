# --------------
# importing required libraries

import pandas as pd
import numpy as np

# Creating a new Dataframe 

bank = pd.read_csv(path)
# print(bank.head())

# Creating a variable to check all categorcial values.

categorical_var = bank.select_dtypes(include = 'object')
# print(categorical_var.head())

# Creating a variable to check all numerical values.

numerical_var = bank.select_dtypes(include = 'number')
#print(numerical_var.head())

# print(categorical_var.shape, numerical_var.shape)

# Creating a new dataframe to drop the column "Loan-ID"

banks = bank.drop(['Loan_ID'], axis=1)
# print(banks.isnull().sum())

# Cacluating mode for the dataframe "Banks"

bank_mode = banks.mode()
# print(bank_mode)

# Filling missing(NaN) values of banks with bank_mode
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)

print(banks.isnull().sum()) # To Check

# Calculating Average loan amount of a person

avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'], values='LoanAmount' ,aggfunc=np.mean)

#print(avg_loan_amount['LoanAmount'][1],2) #125.27

# print(banks.shape)

Loan_Status = 614

# Calculate the percentage of loan approval for self-employed people

loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].count()[0]
percentage_se = (loan_approved_se/Loan_Status)*100

print(percentage_se)

# Calculate the percentage of loan approval for people who are not self-employed

loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].count()[0]
percentage_nse = (loan_approved_nse/Loan_Status)*100

print(percentage_nse)

# convert Loan_Amount_Term which is in months to a year

loan_term = banks['Loan_Amount_Term'].apply(lambda months : months/12 )

# Find the number of applicants having loan amount term greater than or equal to 25 years

big_loan_term = loan_term[loan_term >= 25].size

print(big_loan_term)

# Groupby the 'banks' dataframe by Loan_Status

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]

print(loan_groupby)

#  find the mean of 'loan_groupby'

mean_values = loan_groupby.mean()

print(mean_values.iloc[1,0], 2) #Checkng... 5384.07



