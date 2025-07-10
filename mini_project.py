import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
#load csv file 
df = pd.read_csv("Week2/data.csv")
#full empty cities with 'Unknown'
df['city'] = df['city'].fillna("Unknown")
#filter age
adults = df[df['age'] >= 18]
#city-wise Count & Average Age
print("\n City-wise person count:")
print(adults['city'].value_counts())

print("\n City-wise average age:")
print(adults.groupby('city')['age'].mean())

#Visualization
# Bar Chart - Adults per City
adults['city'].value_counts().plot(kind = 'bar', title = 'Adults per City')
plt.xlabel("City")
plt.ylabel("Adults Count")
plt.tight_layout()
plt.show()
#Pie Chart - Adults per City

adults['city'].value_counts().plot(kind = 'pie', autopct='%1.1f%%')
plt.title("City Distribution of Adults")
plt.ylabel("")
plt.tight_layout()
plt.show()

adults.to_csv("Week2/adults_filtered.csv", index = False)
print("\n Filtered data saved as adults_filtered.csv")

