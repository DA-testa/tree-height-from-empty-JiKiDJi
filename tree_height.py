# python3

import sys
import threading


def compute_height(n, parents):
    max_height = 0
    heights = [0]*n
    for i in range(n):
        t = i
        height = 1
        while(parents[t]!=-1):
            if (t<i):
                height += heights[t]-1
                break
            else:
                t = parents[t]
                height+=1
            # if (height>n):
            #     height = 0
            #     break
        heights[i] = height
        if (height > max_height):
            max_height = height
    # Write this function
    # Your code here
    return max_height


def main():
    let = input()[0]
    if let == 'F' :
        text = input()
        if 'a' in text:
            return
        if(int(text)<10):
            text = sys.path[0]+ "/test/0" + text
        else:
            text = sys.path[0]+ "/test/" + text
        print(text)
        with open(text) as file:
            n = int(file.readline())
            nums = [int(i) for i in file.readline().split(' ')]         
    elif let == 'I' :
        n = int(input())
        nums = [int(i) for i in input().split(' ')]
    else: 
        return
    # print(n)
#     print(nums)
#     print()
    print(compute_height(n,nums))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
