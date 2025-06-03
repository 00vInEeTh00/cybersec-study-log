substr="ERROR"
with open('Logs.txt', 'rt') as myfile:
    for line in myfile:
        line=line.rstrip('\n')
        index = line.find(substr)
        if index != -1:
            print(line)
       