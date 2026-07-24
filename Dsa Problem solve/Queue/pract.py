def noOfTicket():
    index = 0
    tickets = [5, 1, 1, 1]
    times = 0
    i = 0
    while tickets[index] > 0:
        if tickets[i]>0:
            tickets[i] -= 1
            times += 1
        i=(i+1)% len(tickets)
    return times
print(noOfTicket())
