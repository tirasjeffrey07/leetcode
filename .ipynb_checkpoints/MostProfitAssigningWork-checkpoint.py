
def maxProfitAssignment(difficulty: list[int], profit: list[int], worker: list[int]) -> int:
    # zip 'zips' the two lists into a tuple of tuples while maintaingorder
    # ((difficulty1, profit1), (d2,p2), (d3, p3)....)
    jobs = zip(difficulty, profit)
    sortedJobs = sorted(jobs) # sorts by key ie difficulty
    sortedWorkers = sorted(worker)
    
    i = bestProfit = maxP = 0
    
    for skill in sortedWorkers:
        # skill must be greater than or equal to difficulty
        while i < len(sortedJobs) and skill >= sortedJobs[i][0]:
            # update the max profit
            maxP = max(maxP, sortedJobs[i][1])
            i += 1
        # sum up all the valid max profits
        bestProfit += maxP
    return bestProfit

"""
# tried this, but couldnt pass cases after case 46, please let me know the correct version of this implementation

        def traverse(w):
            maxP = -1
            for i in range(len(difficulty)):
                # stop when you find difficulty greater than w
                if difficulty[i] > w:
                    return i - 1
                # traversed the entire list with no match, ie the worker can perform all difficulty level jobs
                if i == len(difficulty) - 1:
                    return i            
            return -1
        res = []
        for w in worker:
            assign = traverse(w)
            if assign >= 0:
                res.append(profit[assign])

        if len(res) == 0:
            return 0
        return sum(res)


"""