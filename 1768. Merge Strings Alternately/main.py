def main(word1, word2):
    list1 = list(word1)
    list2 = list(word2)
    res = []

    while len(list1) > 0 and len(list2) > 0:
        if len(list1) > 0:
            res.append(list1[0])
            list1.pop(0)
        if len(list2) > 0:
            res.append(list2[0])
            list2.pop(0)
    res += list1
    res += list2
    return "".join(res)
        


word1="abcdefg"
word2="123"

print(main(word1, word2))