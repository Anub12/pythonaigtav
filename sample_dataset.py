import pandas as pd

print("This file is for sample dataset")

df = pd.DataFrame(
    {
        "Name": [
            "Anubhav",
            "Saksham",
            "Himanshu",
            "Ankur",
            "Robin",
            "Sanjiwan",
            "Vansh",
            "Shubham"
        ],
        "Age": [22, 22, 19, 23, 24, 22, 22, 22],
        "Sex": ["male", "male", "male", "male", "male", "male", "male", "male"],
        "Marks": [98, 92, 85, 78, 88, 92, 78, 65],
        "Status": ["Single", "Married", "Single", "Single", "Single", "Married", "Single", "Married"],
        "Admission Number": [6669, 8382, 3382, 2934, 2842, 2942, 1182, 5931]
    }
)

print(df)

df.info()
df.head()

df.to_csv('out.csv', index=False)

# For first commit, date: 25-04-2024
