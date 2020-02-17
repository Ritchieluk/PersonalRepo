arr = [2,3,5,5,7,11,11,13,13,13,15]

i = 0
while(i<len(arr)-1):
    if arr[i] == arr[i+1]:
        del arr[i+1]
        i-=1
    i+=1
print(arr)