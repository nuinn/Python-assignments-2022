name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst = list()
for line in handle:
    if not line.startswith("From"):
        continue
    if line.startswith("From:"):
        continue
    else:
        words = line.split()
        hours = words[5].split(":")
        lst.append(hours[0])
counts = dict()
for hr in lst:
    counts[hr] = counts.get(hr,0) + 1
for k,v in (sorted(counts.items())):
    print(k,v)
