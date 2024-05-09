name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst = list()
for line in handle:
    if not line.startswith("From:"):
        continue
    else:
        words = line.split()
        lst.append(words[1])
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value

print(bigword,bigcount)
