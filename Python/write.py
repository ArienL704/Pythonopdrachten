f = open("Lorum.txt", "w") #Open File
f.write("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.")
f.close()

#open and read the file
f = open("Lorum.txt", "r")
print(f.read()) 

    # Read all lines into a list
lines = f.readlines()

# Remove any trailing newline characters from each line
lines = [line.strip() for line in lines]

# Print the resulting list
print(lines)