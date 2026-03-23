# Function to display dictionary data
def show_student(data):
    for key, value in data.items():
        print(key, ":", value)

# Creating dictionary
student = {
    "name": "yash",
    "age": 22,
    "course": "BCA"
}

# Calling function
show_student(student)