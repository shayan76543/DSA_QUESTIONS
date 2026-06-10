def min_max(array,start,end):
    if start==end:
        return array[start],array[end]
    if start+1==end:
        if array[start]<array[end]:
            return array[start],array[end]
        else:
            return array[end],array[start]
    mid=start+(end-start)//2
    min1,max1=min_max(array,start,mid)
    min2,max2=min_max(array,mid+1,end)
    return min(min1,min2),max(max1,max2)
array=[9,2,12,43,2]
minimum,maximum=min_max(array,0,len(array)-1)
print("minimun Value is =",minimum)
print("maximun value is =",maximum)
