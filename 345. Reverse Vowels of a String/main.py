

def main(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    finded = []

    for letter in s:
        if letter in vowels:
            finded.append(letter)

    arr = list(s)
    for i in range(len(arr)):
        if arr[i] in vowels:
            arr[i] = finded[-1]
            finded.pop()
    return "".join(arr)



s1 = 'hello wOrld'
print(main(s1))