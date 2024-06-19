def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        # impossible case
        if m * k > len(bloomDay):
            return -1
        
        def possible(day) -> bool:
            
            adjacent, nob = 0, 0
            
            for i in range(0, len(bloomDay)): 
                if bloomDay[i] <= day:
                    adjacent += 1
                else: 
                    # before setting count = 0 
                    # if bouquet can be formed from the most recent number of adjacent flowers, add it to the number of bouquets
                    nob += adjacent // k
                    
                    adjacent = 0
                    
            # after traversing the entire bloomDay, you may have a count that is greater >= k
            nob += (adjacent // k)
            
            #   bloomDay    [x, x, x, x, x, _, _, _, x, x, x]
            #   count        1, 2, 3, 4, 5 |       | 1  2  3
            

            return nob >= m

        
        low, high = min(bloomDay), max(bloomDay)
        # binary search the days array
        while low <= high:
            # check the center day
            mid = (low+high) // 2
            
            if possible(mid):
                # since 'mid' day is possible, check if lesser days are possible
                high = mid - 1

            else:
                # if day x cannot make 'm' bouquets,
                # day x-1, x-2, x-3 ...1 will not have enough flowers to make 'm'  
                low = mid + 1
                # so simply search for days with more flowers bloomed
        
        # at the end the answer will be pointed by low
        return low
        
        """
        refer the following array = [7, 7, 7, 7, 13, 11, 12, 7]
        at the end of all iterations

         _  _  _  _   h,m  l  _         
        [7, 8, 9, 10, 11, 12, 13]


        high and mid point to the same value at the end but the answer, 
        least value, is pointed by low

        """