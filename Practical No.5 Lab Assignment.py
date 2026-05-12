#Titanic Dataset – Data Analysis & Visualization
#Load Dataset
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
#Assumed columns:
#Survived, Pclass, Sex, Age, Fare

#Identified 5 Grains (Insights)
#Grain 1: Survival Count
survival = df["Survived"].value_counts()

plt.figure()
plt.bar(survival.index, survival.values)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.show()

#Grain 2: Survival by Gender
gender_survival = df.groupby("Sex")["Survived"].sum()

plt.figure()
plt.bar(gender_survival.index, gender_survival.values)
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Survivors")
plt.show()

#Grain 3: Passenger Class Distribution
class_count = df["Pclass"].value_counts()

plt.figure()
plt.bar(class_count.index, class_count.values)
plt.title("Passenger Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()

#Grain 4: Age Distribution
plt.figure()
plt.hist(df["Age"].dropna(), bins=10)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#Grain 5: Fare Distribution
plt.figure()
plt.hist(df["Fare"], bins=10)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.show()
