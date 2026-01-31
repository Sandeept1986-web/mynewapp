# Write to a File Program

with open("student_data.txt", "w") as file:
    file.write("This is a sample file.\n")
    file.write("We are writing student data here.\n")
    file.write("End of the file.\n")

print("Data written to student_data.txt successfully!")