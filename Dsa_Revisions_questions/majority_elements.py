def majority_elements(arr):
    n=len(arr)
    majority_element=arr[0]
    count=1
    frequency=0
    for i in range(1,n):
        if count==0:
            majority_element=arr[i]
            count=1
        elif arr[i]==majority_element:
            count+=1
        else: 
            count-=1
    for i in range(0,n):
        if arr[i]==majority_element:
            frequency+=1
    if frequency>n//2:
        return f"majority element is {majority_element} that comes {frequency} times"
    else:
        return "there is no majority elements"
arr=[3,4,3,3,2,3,3,8,8,4,3]
print(majority_elements(arr))


    