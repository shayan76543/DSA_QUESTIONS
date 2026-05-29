def divide(array,start,end):
    if start>=end:
        return 
    mid=start+(end-start)//2
    divide(array,start,mid)
    divide(array,mid+1,end)
    conquer(array,start,mid,end)
def conquer(array,start,mid,end):
    merge=[]
    first_half=start
    second_half=mid+1
    while first_half<=mid and second_half<=end:
        if array[first_half]<=array[second_half]:
            merge.append(array[first_half])
            first_half+=1
        else:
            merge.append(array[second_half])
            second_half+=1
    while first_half<=mid:
        merge.append(array[first_half])
        first_half+=1
    while second_half<=end:
        merge.append(array[second_half])
        second_half+=1
    for i in range(len(merge)):
        array[start+i]=merge[i]
array=[3,2,4,7,6,9,2,1]
print(array)
divide(array,0,len(array)-1)
print(array)        


    




        