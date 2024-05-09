# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = 0
linecount = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    linecount = linecount + 1
    stno = line.find(" ")
    no = float(line[stno + 1:])
    x = x + no
print("Average spam confidence:",x/linecount)
