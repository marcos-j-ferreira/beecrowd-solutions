def banknotes(x):
    denominations = [100, 50, 20, 10, 5, 2, 1]
    arr = [0, 0, 0, 0, 0, 0, 0]
    
    d = x
    for i in range(len(denominations)):
        while d >= denominations[i]:
            d -= denominations[i]
            arr[i] += 1
    
    print(f"{x}")
    print(f"{arr[0]} nota(s) de R$ 100,00")
    print(f"{arr[1]} nota(s) de R$ 50,00")
    print(f"{arr[2]} nota(s) de R$ 20,00")
    print(f"{arr[3]} nota(s) de R$ 10,00")
    print(f"{arr[4]} nota(s) de R$ 5,00")
    print(f"{arr[5]} nota(s) de R$ 2,00")
    print(f"{arr[6]} nota(s) de R$ 1,00")

a = int(input()) 
banknotes(a)
