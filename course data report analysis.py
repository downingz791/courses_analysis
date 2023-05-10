# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:54:15 2023

@author: downi
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\downi\Documents\Upwork Projects\PG report.xlsx')
data_size = df.size
print("Data size: " + str(data_size))

#--------post code info
unique = df['Residential Zip/Postal Code'].unique()
print("Number of unique zip codes: " + str(unique.size))
unique_counts = df['Residential Zip/Postal Code'].value_counts()
print()
#dataframe of just top 20 zip codes and their counts
top20zipscounts = unique_counts.head(20).to_frame().reset_index()
top20zipscounts = top20zipscounts.rename(columns= {'index':'Residential Zip/Postal Code','Residential Zip/Postal Code':'counts'})
#dataframe of top 20 zip codes from original data
top20zip_df = pd.merge(df, top20zipscounts, on='Residential Zip/Postal Code')
#total top 20 courses taken
course_counts = top20zip_df['Course Cd'].value_counts()
course_counts_df = course_counts.head(20).to_frame().reset_index()
course_counts_df = course_counts_df.rename(columns= {'index':'Course Cd','Course Cd':'counts'})
course_counts_df.plot(x='Course Cd',y='counts',kind='bar',title='Top 20 Courses Taken based from Top 20 Zip Codes')
plt.show()

#--------course info
course_counts = df['Course Cd'].value_counts()
course_counts_df = course_counts.head(20).to_frame().reset_index()
course_counts_df = course_counts_df.rename(columns= {'index':'Course Cd','Course Cd':'counts'})
course_counts_df.plot(x='Course Cd',y='counts',kind='bar',title='Top 20 Courses Taken based from all data')
plt.show()

top20course_df = pd.merge(course_counts_df, df, on='Course Cd')
top20course_unique_names = top20course_df['Program Full Name'].unique()
print(top20course_unique_names)







