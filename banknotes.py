#100, R$ 50, R$ 20, R$ 10, R$ 5, R$ 2 e R$ 1.


def banknotes(x):
    
    arr = [0,0,0,0,0,0,0]
    
    f = True
    
    d = x
    
    
    while d > 0:
        
        
        if d >= 100:
            d = d - 100
            arr[0] = arr[0] + 1
        elif d >= 50:
            d = d - 50
            arr[1] =  arr[1] + 1
        elif d >= 20:
            d = d - 20
            arr[2] =  arr[2] + 1
        elif d >= 10:
            d = d - 10
            arr[3] =  arr[3] + 1
        elif d >= 5:
            d = d - 5
            arr[4] =  arr[4] + 1
        elif d >= 2:
            d = d - 2
            arr[5] =  arr[5] + 1
        else:
            d = d - 1
            arr[6] =  arr[6] + 1
            return arr
            
    print(f"{arr[0]} nota(s) de R$ 100,00\n{arr[1]} nota(s) de R$ 50,00\n{arr[2]} nota(s) de R$ 20,00\n{arr[3]} nota(s) de R$ 10,00\n{arr[4]} nota(s) de R$ 5,00\n{arr[5]} nota(s) de R$ 2,00\n{arr[6]} nota(s) de R$ 1,00")
            

a = int(input())

result = banknotes(a)















