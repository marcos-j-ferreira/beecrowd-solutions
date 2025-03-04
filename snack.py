numbers = input()

number = numbers.split()

x = int(number[0])
y = int(number[1])

def snack(x, y):
    
    if x == 1:
        return 4.00 * y
    elif x == 2:
        return 4.50 * y
    elif x == 3:
        return 5.00 * y
    elif x == 4:
        return 2.00 * y
    elif 5:
        return 1.50 * y
        

result = snack(x,y) 

print(f"Total: R$ {result:.2f}")
