# JUMP GAME
def jump(arr):
    n=len(arr)
    max_reach=arr[0]
    step=arr[0]
    jump=1
    for i in range(1,n):
        if i>max_reach:
            return -1
        if i==n-1:
            return jump
        if n==1:
            return 0
        max_reach=max(max_reach,i+arr[i])
        step-=1
        if step==0:
            jump+=1
            step=max_reach-i
arr=[1,2,0,3,0,0,4,0,0,1,2,0,2,1,1,1]
print(jump(arr))
#TIME COMPLEXITY =O(N)
#SPACE COMPLEXITY =O(1)