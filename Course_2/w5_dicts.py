name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mails = {}
for line in handle:
    if line.startswith("From "):
        line = line.split()
        mail = line[1]
        mails[mail] = mails.get(mail, 0) + 1
bigword = 0
bigcount = 0
for key, value in mails.items():
    if mails[key] > bigcount:
        bigcount = mails[key]
        bigword = key
print (bigword, bigcount)
        