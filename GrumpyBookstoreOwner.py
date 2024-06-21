def maxSatisfied(customers: list[int], grumpy: list[int], minutes: int) -> int:
        window, maxWindow = 0, 0
        # stores the customers who come at non grumpy score
        satisfied = 0
        # starting point of  the window
        l = 0 
        
        # right limit of the winddow
        for r in range(len(customers)):
            # if 1 add it to the score
            if grumpy[r]:
                window += customers[r]
            # track the non grumpy minutes to get the base score which can be improved
            else:
                satisfied += customers[r]

            # if the window gets bigger
            if r - l + 1 > minutes:
                if grumpy[l]:
                    # remove customer from the score if owner is grumpy
                    # coz we added it when we went past it once  
                    window -= customers[l]
                l += 1
            maxWindow = max(maxWindow, window)
        return satisfied + maxWindow