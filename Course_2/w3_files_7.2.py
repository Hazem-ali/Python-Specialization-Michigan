# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count += 1
        ind = line.find(".")
        snum = line[ind - 1:]
        num = float(snum)
        total += num
avg = total / count
print("Average spam confidence:", avg)
