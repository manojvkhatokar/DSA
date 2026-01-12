# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

def climbing_stairs(n):
    #This is basically bottom up DP approach of fibonacci series
    if n ==1 :
        return 1
    res = [None] * (n+1)
    res[1] = 1
    res[2] = 2
    for i in range(3, n+1):
        res[i] = res[i-1] + res[i-2]
    return res[n]