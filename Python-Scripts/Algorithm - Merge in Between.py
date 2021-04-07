"""
Check out the algorithm definition in the image below:
https://github.com/cassiobolba/Python/blob/master/Python-Scripts/img/merge%20in%20between.jpg
"""

# starting nodes to be replaces a and b
a = 2
b = 3
# ordered list which will receive the merge
list1 = [1,2,3,4,5]
# list to replace nodes
list2 = [6,7,8,9]

def mergeInBetween(list1, list2, a, b):
    # temp list to receive values before nodes to replace
    list1a = []
    # append every item in list that comes before the first node
    for i in list1:
        if i < a:
            list1a.append(i)
        else:
            break
    # temp list to receive values after nodes to replace
    list1b = []
    # append every item to the list that comes after the second node
    for i in list1:
        if i > b:
            list1b.append(i)
        else:
            continue
    
    # concatenate lists to have them merged
    full_list = list1a+list2+list1b
    for i in full_list:
        print(i)

mergeInBetween(list1,list2,a,b)
