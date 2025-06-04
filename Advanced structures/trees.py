def bft(tree, root):
    queue = []
    queue.append(root)
    #append will enqueue
    #queue.pop(0) will dequeue


    while len (queue) != 0:
       node = queue.pop(0)

       print(tree[node]["data"])

       for i in tree[node]["childeren"]:
           queue.append(i)






tree = [
    {"data":"A", "childeren": [1] },#1
    {"data":"B", "childeren": [2,3,4] },#2
    {"data":"C", "childeren": [5] },#3
    {"data":"D", "childeren": [] },#4
    {"data":"E", "childeren": [6] },#5
    {"data":"F", "childeren": [] },#6
    {"data":"G", "childeren": [] }#7
]


bft(tree,0)

