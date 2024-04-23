import pandas

print("This file is for sample dataset")

df = pandas.DataFrame(
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
        "Marks": [98, 92, 85, 78, 88, 92, 78, 65]
    }
)

print(df)

df.info()
df.head()

df.to_csv('out.csv', index=False)

# For pushing file
