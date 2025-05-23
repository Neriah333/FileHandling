
with open("input.txt","w") as infile:
  infile.write("Hi,Im Pheobe.\n")
  infile.write("I Love coding n building projects.\n")
  infile.write("I'm a junior software engineer.\n")
  infile.write("I also love dancing.\n")

# Create input.txt with sample content
with open("input.txt","r") as infile:
  content = infile.read() 

# Read input.txt
word_count = len(content.split())

# Convert text to uppercase
content_upper = content.upper()

# Write to output.txt
with open('output.txt', 'w') as outfile:
  outfile.write(content_upper)
  outfile.write(f"\nWORD COUNT: {word_count}\n")

# print("output.txt has been created successfully with the processed content.")
print("output.txt has been created successfully with the processed content.")

