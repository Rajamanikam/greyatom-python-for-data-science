# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)
print(data.head())

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()
print(loan_status)

#Plotting bar plot

plt.xlabel('Loan Status')
plt.ylabel('Count for Loan Status')
plt.title('Bar plot for Loan Status')
loan_status.plot.bar(rot=0)


# Step 2
#Plotting an unstacked bar plot

property_and_loan =  data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()

property_and_loan.plot(kind='bar', stacked=False, rot=45)
plt.ylabel('Loan Status')
plt.show()


# Step 3
#Plotting a stacked bar plot

education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()

education_and_loan.plot(kind='bar',stacked=True, rot=45)
plt.xlabel("Education Status")
plt.ylabel("Loan Status")


# Step 4 
#Subsetting the dataframe based on 'Education' column

graduate = data[data['Education']=='Graduate']

#Subsetting the dataframe based on 'Education' column

not_graduate = data[data['Education']=='Not Graduate']

#Plotting density plot for 'Graduate'

graduate['LoanAmount'].plot(kind='density', label='Graduate')

#Plotting density plot for 'Graduate'

not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

#For automatic legend display

plt.legend()

# Step 5
#Setting up the subplots


fig,(ax_1,ax_2,ax_3) = plt.subplots(nrows=3, ncols=1, figsize = (8,10))
plt.subplots_adjust(hspace=1.35)

#Plotting scatter plot

ax_1.scatter(data['LoanAmount'], data['ApplicantIncome'])

#Setting the subplot axis title

ax_1.set_title("Applicant Income")


#Plotting scatter plot

ax_2.scatter(data['LoanAmount'] ,data['CoapplicantIncome'])

#Setting the subplot axis title

ax_2.set_title('Coapplicant Income')

#Creating a new column 'TotalIncome'

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Plotting scatter plot

ax_3.scatter(data['LoanAmount'], data['TotalIncome'])


#Setting the subplot axis title

ax_3.set_title('Total Income')




