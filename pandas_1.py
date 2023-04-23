import pandas as pd

data ={
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Country': ['USA', 'Canada', 'Australia', 'UK', 'India'],
    'Attempts': [1, 3, 2, 4, 3],
    'Score': [85, 92, 88, 95,90]
}
labels=[1,2,3,4,5]
# Create a Pandas dataframe from the dictionary
df=pd.DataFrame(data,index=labels)
print(df)
# Display only the middle rows of the dataframe
print(df.iloc[2:4])
# Select rows where Attempts > 2
result=df[df['Attempts']>2]
print(result)
# Select rows where score between 90 and 100
result_1=df[df['Score'].between(90,100)]
print(result_1)
#add new column
column = 'Gender'
column_values = ['F', 'M', 'M', 'M', 'F']
df[column]= column_values
print(df)
#describe
desc = df.describe()
print(desc)
#chnage name of column
df.rename(columns={'Country':'Location'},inplace=True)
print(df.columns)
#combine column
