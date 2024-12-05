# thing = "thing"
# if "thing" in thing:
#     print("thing")

# numbers = [2,5,1,6,1]
# numbers.sort()
# print(numbers)


def doloop(scorelist):
    for i in range(len(scorelist)):
        for j in range(len(scorelist[i])):
            for k in scorelist[i][j]:
                if k == "-":
                    return True
    return False



list = [[[2,1],[1,2],[0]],[[],[]]]

print(doloop(list))