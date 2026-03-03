# practice first question 
# Jump Game
def jump_game():
    arr=[3,2,5,4,1,5,0,7,4]
    n=len(arr)
    max_reach=arr[0]
    step=arr[0]
    jump=1
    for i in range(0,n):
        if n==1:
            return 1
        if i>max_reach:
            return "Game Over"
        max_reach=max(max_reach,arr[i]+i)
        step-=1
        if step==0:
            jump+=1
            step=max_reach-i
    return f"Your succesfully complete your Game with {jump} jumps"
print(jump_game())