name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = {}
for line in handle:
    if line.startswith("From "):
        line = line.split()
        hour = line[5]
        hour = hour.split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1
for key, value in sorted(hours.items()):
    print(key, value)
        