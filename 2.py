list1 =[44,33,22,55,24,343,55,22]

def half(lst):
    if len(lst) < 3:
        return []
    mid = len(lst) // 2
    return lst[mid:]


print(half(list1))