import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read the data from the CSV file
data = pd.read_csv("staff_data.csv")

# Step 2: Check the data
print("First 5 rows of the data:")
print(data.head())

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Step 3: Clean the data
# Remove duplicate entries
data = data.drop_duplicates()

# Step 4: Explore the data
# Number of jobs posted by each company
jobs_per_company = data['Company'].value_counts()

# Locations of the jobs
job_locations = data['Location'].value_counts()

# Step 5: Make pictures
# Chart showing where the jobs are located
plt.figure(figsize=(10,6))
job_locations.plot(kind='bar', color='skyblue')
plt.title('Job Locations')
plt.xlabel('Location')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=45)
plt.show()

# Step 6: Look Deeper
# Example 1: Number of Jobs per Company
plt.figure(figsize=(12, 8))
sns.countplot(y='Company', data=data, order=data['Company'].value_counts().index)
plt.title('Number of Jobs Posted by Each Company')
plt.xlabel('Number of Jobs')
plt.ylabel('Company')
plt.show()

# Example 2: Deadline Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Deadline'], kde=True)
plt.title('Deadline Distribution')
plt.xlabel('Deadline')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=45)
plt.show()




