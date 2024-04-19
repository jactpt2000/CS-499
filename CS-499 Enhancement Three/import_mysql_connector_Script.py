# ----------------------------------------------------------------------------------
# Name: Jorge Argueta
# Course: CS-499
# Date: 4/6/2024
# Instructor: Professor Goggin 
# 
# Description: This Python script demonstrates how to securely connect to a MySQL 
# database using environment variables, fetch data from the database, perform data 
# analysis using the K-means clustering algorithm, and visualize the results. This
# aligns with course objectives on database management, data mining, and visualization.
# ----------------------------------------------------------------------------------

import os
import mysql.connector
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Database connection parameters using environment variables for security
db_config = {
    "host": "localhost",
    "user": "root",
    "password": os.getenv("MYSQL_DB_PASSWORD"),  # Fetch password from environment variable
    "database": "employees_table"
}

try:
    # Attempt to establish a database connection
    conn = mysql.connector.connect(**db_config)
    print("Successfully connected to the database.")
except mysql.connector.Error as e:
    # Handle exceptions for database connection errors
    print(f"Error connecting to MySQL: {e}")
    exit(1)

# Create a cursor with dictionary results for easier data handling
cursor = conn.cursor(dictionary=True)

# SQL query to select non-zero salaries from the Employee table
query = "SELECT Salary FROM Employee WHERE Salary > 0;"

# Execute the query and retrieve the data
cursor.execute(query)
results = cursor.fetchall()

# Convert the query results into a pandas DataFrame for analysis
df = pd.DataFrame(results)

# Close the cursor and database connection to release resources
cursor.close()
conn.close()

# Proceed with data analysis if the DataFrame is not empty
if not df.empty:
    # Initialize and apply K-means clustering to the salary data
    kmeans = KMeans(n_clusters=3, random_state=0).fit(df[['Salary']])
    df['Cluster'] = kmeans.labels_

    # Visualization of salary clusters using a scatter plot
    sns.scatterplot(data=df, x='Salary', y='Cluster', hue='Cluster', palette='viridis', legend='full')
    plt.title('Salary Clusters')  # Title for the plot
    plt.xlabel('Salary')  # Label for the x-axis
    plt.ylabel('Cluster')  # Label for the y-axis
    plt.show()  # Display the plot
else:
    # Output a message if no data is available
    print("No data found in the database.")
