#create a new file
new_file = open("New_File.txt", "x")
new_file.close()

#check if a file exists
import os

# Check if file exists, and delete it first
if os.path.exists("New_File.txt"):
    os.remove("New_File.txt")
    print("Old file deleted.")
else:
    print("File not found, creating a new one.")

# Now safely create a new file
new_file = open("New_File.txt", "x")
new_file.close()

# Create another file if it doesn't exist
my_file = open("my_file.txt", "w")
my_file.write("Hi! I am a student of MHSS")
my_file.close()

# Delete file named codingal.txt if it exists
if os.path.exists("codingal.txt"):
    os.remove("codingal.txt")
    print("codingal.txt deleted successfully.")
else:
    print("codingal.txt does not exist.")