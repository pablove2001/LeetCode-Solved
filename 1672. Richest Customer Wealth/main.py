





def maximumWealth(self, accounts):
        richest = 0
        for acount in accounts:
            count = 0
            for wealth in acount:
                count += wealth
            
            if count > richest:
                richest = count
        return richest
