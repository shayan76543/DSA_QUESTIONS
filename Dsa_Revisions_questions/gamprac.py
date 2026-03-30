def jumping_game():
    arr=[2,1,4,1,1,3,4]
    n=len(arr)
    max_reach=arr[0]
    step=arr[0]
    jump=1
    if n==1:
        return 0
    for i in range(1,n):
        if max_reach<i:
            return "Game over"
        if arr[0]==0:
            return "game over"
        max_reach=max(max_reach,i+arr[i])
        step-=1
        if step==0:
            jump+=1
            step=max_reach-i
    return jump
print(jumping_game())
