def FactorialRec(n:int) -> int:
    if n == 0:
        return 1
    return n * FactorialRec(n-1)

####################################################
n=int(input("Número para cálcular el factorial: "))

print(f"{n}! = {FactorialRec(n)}")