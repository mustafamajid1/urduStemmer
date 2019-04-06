strings = []
with open(r"urdu.txt",encoding='utf-8') as f: #formatting and pushing into array
    for line in f:
        if line == '\ufeff\n':
            continue
        line = line.replace("\ufeff","")
        strings.append(line.rstrip()) 

print("Array: ",strings)
for contents in strings:
    if contents[-2:] == "اں": #regular plural
        contents_new = contents[:-2]
    elif contents[-4:] == "وانا":
        contents_new = contents.replace("وا","") #verb, infinitive to direct causative infinitive
    elif contents[-2:] == "گی":
         contents_new = contents.replace("گی","") #suffix extraction
    elif contents[0:2] == "بد":
         contents_new = contents.replace("بد","")
    print(contents," -> ",contents_new)


