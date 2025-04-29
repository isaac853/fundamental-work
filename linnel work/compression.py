fullList = []

with open("file.txt") as f:
  for i in f:
    if i not in fullList:
      fullList.append([i,1])
    else: 
      for j in range(len(fullList)):
        if fullList[j][0] == i:
          fullList[j][1] += 1

print(fullList)