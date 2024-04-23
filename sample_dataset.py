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
        "Sex": ["male", "male", "male", "male", "male", "male", "male", "male"]
    }
)

print(df)
# For pushing file
