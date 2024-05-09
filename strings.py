text = "X-DSPAM-Confidence:    0.8475"
tlen = len(text)
stnum = text.find("0")
data = text[stnum : tlen + 1]
num = float(data)
print(num)
