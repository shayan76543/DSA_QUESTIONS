def backtrack(current):
    if len(current) == 3:
        print(current)
        return
    backtrack(current + "0")
    backtrack(current + "1")
backtrack("")