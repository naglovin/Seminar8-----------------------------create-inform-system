def get_da(n,f):
    list=[]
    for i in f:
        list.append(i.split()[n])
    return list


def sort(n,f):
    list=[]
    for i in f:
        if n in i:
            list.append(i)
    return list    