def kanpsack_algorithm(w_o_t, value, capacity):
    n = len(w_o_t)
    dp = [[0]*(capacity+1) for i in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if (w_o_t[i-1] <= w):
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_o_t[i-1]]+value[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    print("Max Profit is =", dp[n][capacity])
wt = [2, 3, 4, 5]
value = [3, 4, 5, 6]
kanpsack_algorithm(wt, value, 5)
