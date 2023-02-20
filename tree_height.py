import sys
import threading


def compute_height(n, parents):
    max_height = 0
    for i in range(n):
        t = i
        height = 1
        while(parents[t]!=-1):
            t = parents[t]
            height+=1
        if (height > max_height):
            max_height = height
    # Write this function
    # Your code here
    return max_height


def main():
    let = input()[0]
    n = int(input()[0])
#     if let == 'F' :
#         if 'a' in text:
#             return
#         with open(text) as file:
#             text = file.read()
    if let != 'I' :
        return
    nums = [int(i) for i in input().split(' ')]
    print(n)
    print(nums)
    print()
    print(compute_height(n,nums))

    
    


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
