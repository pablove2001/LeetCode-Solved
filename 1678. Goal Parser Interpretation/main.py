def main(command):
    lista = list(command)
    res = []

    while len(lista) > 0:
        if lista[0] == "G":
            lista.pop(0)
            res.append("G")
        elif lista[0] == "(" and lista[1] == ")":
            lista.pop(0)
            lista.pop(0)
            res.append("o")
        else:
            lista.pop(0)
            lista.pop(0)
            lista.pop(0)
            lista.pop(0)
            res.append("al")
    
    return "".join(res)



command = "(al)G(al)()()G"
print(main(command))