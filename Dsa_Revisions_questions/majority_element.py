def majority_element():
    arr=[3,2,7,5,2,2,2,2,2,2,2,2,2,9,9,9,9,9,9]
    n=len(arr)
    arr.sort()
    majority_element1=arr[0]
    count=1
    frequency=0
    for i in range(1,n):
        if count==0:    
            majority_element1=arr[i]
            count=1
        elif majority_element1==arr[i]:
            count+=1
        else:
            count-=1
    for i in range(0,n):
        if arr[i]==majority_element1:
            frequency+=1
    if frequency>n//2:
        return f"Majority Element is {majority_element1} And come {frequency} Times \n For Testing {arr}"
    else:
        return "There is no any majority Element"
print(majority_element())


