def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    # The cost differences tell us how much cost we can avoid by picking city A over B.        
    a = sorted(costs, key=lambda cost: cost[1] - cost[0], reverse=True)
    
    #  Since our cutoff is the (N+1)th person, we send the remaining N people to city B.
    res, n = 0, len(costs)//2
    for cost in a[:n]:
        res += cost[0]
    for cost in a[n:]:
        res += cost[1]
    return res