
"""
Check out the algorithm definition in the image below:
https://github.com/cassiobolba/Python/blob/master/Python-Scripts/img/minimum%20swaps2.jpg
"""


def moves(arr):
    # start index counting from left
    l = 0
    # start index counting from right
    r = len(arr)-1
    # start swipes counting
    swaps = 0
    
    while l < r:
        # keep incrementing index from left while it is even and l < r
        while (arr[l] % 2 == 0 and l < r ):
            l += 1
        # keep decreasing index from left while it is odd and l < r
        while (arr[r] % 2 != 0 and l < r):
            r -= 1

        # when both while stops, then we have indexes to swipe
        if (l < r):
            # do the swipe
            arr[l],arr[r] = arr[r],arr[l]
            # increment l and decrease r to continue checking next values
            l += 1
            r -= 1
            # at every swipe, count 1
            swaps += 1
    return print(swaps)
 
arr2 = [8,5,3,5,6]

moves(arr2)


