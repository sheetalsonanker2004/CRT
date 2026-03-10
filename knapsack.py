def knapsack(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]>W:
        return knapsack(wt,val,,n-1)
    else:
        return max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
    
