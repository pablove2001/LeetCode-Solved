
def main(low, high):
    arr = []
    if low % 2 == 0:
        low += 1
    
    if high % 2 == 0:
        high -= 1
    
    return int((high-low)/2+1)

low1=0
high1=0
print(main(low1, high1))