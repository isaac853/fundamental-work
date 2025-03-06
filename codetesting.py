# thing = "thing"
# if "thing" in thing:
#     print("thing")

# numbers = [2,5,1,6,1]
# numbers.sort()
# print(numbers)


# def doloop(scorelist):
#     for i in range(len(scorelist)):
#         for j in range(len(scorelist[i])):
#             for k in scorelist[i][j]:
#                 if k == "-":
#                     return True
#     return False



# list = [[[2,1],[1,2],[0]],[[],[]]]

# print(doloop(list))

# scorelist = [[['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], [0]], [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], [0]]]
# player = 1
# result = (55,4)

# scorelist[player][0][result[1]-1] = result[0]


# print(scorelist)

# import random
# def smallstraight(die):
#     die.sort()
#     count = 0
#     for i in range(4):

#         if die[i+1] == die[i]+1:
#             count += 1

#         elif die[i+1] == die[i]:
#             pass
        
#         else: 
#             count = 0

#         if count == 3:
#             return 30

#     return "invalid"

# def diceroll():
#     return random.randint(1,6)

# print(smallstraight([3, 4, 5, 5, 6]))

# die = [0,0,0,0,0]
# # while True:
# #     for i in range(5):
# #         die[i] = diceroll()
# #     print(smallstraight(die))

# #     def largestraight(die):
# #     die.sort()
# #     count = 0
# #     for i in range(4):

# #         if die[i+1] == die[i]+1:
# #             count += 1

# #         elif die[i+1] == die[i]:
# #             pass
        
# #         else: 
# #             count = 0
            
# #         if count == 4:
# #             return 40

# #     return "invalid"

# def yahtzee(die):
#     for i in numbercount(die):
#         if i >= 5:
#             return 50

#     return "invalid"


# for i in range(5):
#     die[i] = diceroll()

#     print(yahtzee(die))

# list = [1,2,23,3,3,45,4,4,42]
# print(*list)




# card = (f"┌────────────┐\n│ {symbols[self.suit]}          │\n│            │\n│            │\n│     {self.value}     │\n\n│            │\n\n│            │\n│          {symbols[self.suit]} │\n└────────────┘")
# print(card)

card = [f"┌────────────┐",
        f"│ 1          │",
        f"│            │",
        f"│            │",
        f"│     2      │",
        f"│            │",
        f"│            │",
        f"│          1 │",
        f"└────────────┘"]

cards= [card,card]
layer = []

for i in range(len(card)):
    for j in range (len(cards)):
        layer += cards[j][i]
    print(layer)