
def main(salary):
    min = salary[0]
    max = salary[0]
    sum = 0
    for s in salary:
        if s < min:
            min = s
        if s > max:
            max = s
        sum += s
    return (sum - min - max)/(len(salary)-2)

salary1 = [1000,2000,3000]
print(main(salary1))