def gas_station(gas,cost):
    if sum(gas)<sum(cost):
        return -1

    total_tank = 0
    start_index = 0
    for i in range(len(gas)):
        total_tank += gas[i]-cost[i]
        if total_tank<0:
            start_index = i+1
            total_tank =0

    return start_index
print(gas_station([1,2,3,4,5],[3,4,5,1,2]))