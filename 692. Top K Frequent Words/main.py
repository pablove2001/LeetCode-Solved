def main(words, n):
    m = {}
    for w in words:
        m[w] = m.get(w, 0) + 1

    arr = []
    for k, v in m.items():
        arr.append([v, k])

    arr.sort()
    return arr[0:n+1]

    data = list(m.items())

    print(data)


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 2
print(main(words, k))
