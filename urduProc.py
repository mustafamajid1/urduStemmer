strings = []
with open(r"urdu.txt",encoding='utf-8') as f:
    for line in f:
        if line == '\ufeff\n':
            continue
        strings.append(line.rstrip())

print(strings)
for contents in strings:
    if contents[-2:] == "اں":
        contents = contents[:-2]
        print(contents)


