def fractional_knapsack_algorithm(item_weight,price,capacity):
    n=len(item_weight)
    items=[(price[i],item_weight[i],price[i]/item_weight[i]) for i in range(n)]
    print(items)
    for i in range(n):
        for j in range(i+1,n):
            if items[i][2]<items[j][2]:
                items[i],items[j]=items[j],items[i]
    profit=0.0
    for price ,item_weight,perkgprice in items:
        if (capacity>=item_weight):
            capacity-=item_weight
            profit+=price
        else:
            profit+=perkgprice*capacity
            break
    print("Total Profit =", profit)
price=[24,21,12,10]
item_weight=[7,3,4,5]
capacity=20
fractional_knapsack_algorithm(item_weight,price,capacity)