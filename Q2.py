'''
Input: 1, 4, 7, 2, 5

Output: 1, 2, 4, 5, 7

'''
lst = [int(x) for x in input().split(',')]
sorted_list = sorted(lst)
# print(sorted_list)
for x in sorted_list:
    print(x,end= ', ')

