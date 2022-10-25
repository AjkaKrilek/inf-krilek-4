def uloha3(ret):
    s = 'a,e,i,o,u,y'
    for i in range(len(ret)):
        if ret[i] in s:
            return (True)
        else:
            return (False)
ret = input('zadaj vetu:')
print(uloha3(ret))