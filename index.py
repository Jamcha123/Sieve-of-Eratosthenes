myList = [int(i) for i in range(2, 21)]
targets = []
for x in range(len(myList)):
    if myList[x] not in targets:
        for y in range(len(myList)):
            if myList[y] % myList[x] == 0 and x != y:
                targets.append(myList[y])
target = []
for x in range(len(myList)):
    if myList[x] not in targets:
        target.append(myList[x])
print(target)