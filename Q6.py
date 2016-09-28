arr = [1, 0, 1, 1, 1, 0, 0,0,1]
zero = one = 0
for element in arr:
    if 0 == element:
        zero += 1
    elif 1== element:
        one += 1
t0=t1=0
if zero<=one:
    f_ind = arr.index(0)
    ending =0 
    for i,x in enumerate(arr[f_ind:]):
        if 0==x: t0 +=1
        elif 1==x: t1 +=1
        if t0==zero and t1==zero:
            ending = i+f_ind
            break;
    print(f_ind,"to",ending)
else:
    f_ind = arr.index(1)
    ending =0 
    for i,x in enumerate(arr[f_ind:]):
        if 0==x: t0 +=1
        elif 1==x: t1 +=1
        if t0==zero and t1==zero:
            ending = i+f_ind
            break;
    print(f_ind,"to",ending)

    
