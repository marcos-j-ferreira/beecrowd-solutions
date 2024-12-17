def conta (x, y):
    
    step_one = x - y
    
    step_two = (step_one + x + y) / 2 
    
    return step_two
    

def main(a,b,c):
    
    n1 = conta(a,b)
    n2 = conta(b,a)
    
    n = 0
    
    if n1 > n2:
        n = n1
    else:
        n = n2
        
    n3 = conta(n, c)
    n4 = conta(c, n)
    
    maior = 0
    
    if n3 > n4:
        maior = n3
    else:
        maior = n4
    
    return maior
    
a, b, c = map(int, input().split())
result = main(a,b,c)

print(f"{result:.0f} eh o maior")
