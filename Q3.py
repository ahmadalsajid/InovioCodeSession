r_c = [int(x) for x in input().split(',')]
r,c=r_c
if 0 in r_c:
    print(r_c," = 0")
elif 1 in r_c:
    print(r_c," = 1")
elif 0==r%2 and 0==c%2:
    print(r_c," = ",(r**2)*(c**2))
elif 1==r%2 or 1==c%2:
    print(r_c," = ",(r**2)*(c**2)+1)

'''
input format :
0, 0
0, 1
1, 0
1, 1
3, 2

output:
[0, 0] = 0
[0, 1] = 0
[1, 0] = 0
[1, 1] = 1
[3, 2] = 37
'''
