def group(l,size):
    sub=[l[i:i+size] for i in range(0, len(l), size)]
    print(sub)
list_full=[1,2,3,4,5,6,7]
s=2
group(list_full,s)