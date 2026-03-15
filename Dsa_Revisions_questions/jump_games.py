def jump_games(arr):
    n=len(arr)
    max_reach=arr[0]
    jump=1
    step=arr[0]
    for i in range(1,n):
        if n==1:
            return 1
        if i>max_reach:
            return "Game over"
        max_reach=max(max_reach,i+arr[i])
        step-=1
        if step==0:
            jump+=1
            step=arr[i]
    return jump
arr=[3,6,1,0,3,4,7]
print(jump_games(arr))
