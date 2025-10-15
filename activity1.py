#write in file using with() function
with open("condingal.txt", "w") as file:
    file.write("Hi! I am Chimi and I am 14 yrs old")
file.close()

#split file into words
with open("condingal.txt", "r") as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
        word= line.split()
        print(word)
file.close()