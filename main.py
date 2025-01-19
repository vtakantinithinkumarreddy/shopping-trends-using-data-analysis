# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('shopping_trends_updated.csv')

# Check the dataset structure
print(df.info())

# Checking for null values
print(df.isnull().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Display basic statistics
print(df.describe())

# Visualization for Gender
gender_counts = df['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['red', 'blue'])
plt.title('Gender Distribution')
plt.show()

# Gender vs Purchase Amount
sns.barplot(x='Gender', y='Purchase Amount (USD)', data=df, estimator=sum)
plt.title('Total Purchase Amount by Gender')
plt.show()

# Distribution of Purchase Amount by Category
sns.barplot(x='Category', y='Purchase Amount (USD)', data=df, estimator=sum)
plt.title('Total Purchase Amount by Category')
plt.xticks(rotation=45)
plt.show()

# Review Ratings distribution
sns.histplot(df['Review Rating'], bins=10, kde=False)
plt.title('Distribution of Review Ratings')
plt.show()

# Frequency of Purchases
purchase_frequency = df['Frequency of Purchases'].value_counts()
sns.barplot(x=purchase_frequency.index, y=purchase_frequency.values)
plt.title('Frequency of Purchases')
plt.show()

# Seasonal Purchase Trends
seasonal_purchases = df.groupby('Season')['Purchase Amount (USD)'].sum().reset_index()
sns.barplot(x='Season', y='Purchase Amount (USD)', data=seasonal_purchases)
plt.title('Total Purchase Amount by Season')
plt.show()

# Subscription Status vs Purchase Amount
sns.barplot(x='Subscription Status', y='Purchase Amount (USD)', data=df, estimator=sum)
plt.title('Total Purchase Amount by Subscription Status')
plt.show()

# Payment Method Usage
payment_method_counts = df['Payment Method'].value_counts()
sns.barplot(x=payment_method_counts.index, y=payment_method_counts.values)
plt.title('Payment Method Distribution')
plt.xticks(rotation=45)
plt.show()

# Shipping Type vs Purchase Amount
sns.barplot(x='Shipping Type', y='Purchase Amount (USD)', data=df, estimator=sum)
plt.title('Total Purchase Amount by Shipping Type')
plt.show()

# Discount Applied vs Purchase Amount
sns.barplot(x='Discount Applied', y='Purchase Amount (USD)', data=df, estimator=sum)
plt.title('Total Purchase Amount by Discount Applied')
plt.show()

print("Analysis Complete!")
