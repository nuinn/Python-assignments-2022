fname = input("Enter file name: ")
fh = open(fname)
linecount = 0
for line in fh:
    if not line.startswith("From"):
        continue
    if line.startswith("From:"):
        continue
    linecount = linecount + 1
    words = line.split()
    print(words[1])
print("There were", linecount, "lines in the file with From as the first word")
