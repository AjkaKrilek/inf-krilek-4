def uloha1(n, ret:str)->str:
    if n <= len(ret):
        print(ret[n])
    else:
        print('zly index')
    return ""
n = int(input("Zadaj cislo: "))
ret = input("Zadaj retazec: ")
print(uloha1(n, ret))