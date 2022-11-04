
def main(accounts):
        richest = 0
        for acount in accounts:
            count = 0
            for wealth in acount:
                count += wealth
            if count > richest:
                richest = count
        return richest

accounts1 = [[1,2,3], [3,2,1], [2,3,2]]
print(main(accounts1))