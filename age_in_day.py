	
# 1 ano(s)
# 1 mes(es)
# 5 dia(s)

def age_in_day(day):

    resolution = [0,0,0]

    while day > 0:

        if 365 <= day:
            day = day - 365
            resolution[0] = 1 + resolution[0] 
        elif 30 <= day:
            day = day - 30
            resolution[1] = 1 + resolution[1] 
        else:
            day = day - 1
            resolution[2] = 1 + resolution[2] 

    print(f"{resolution[0]} ano(s)\n{resolution[1]} mes(es)\n{resolution[2]} dia(s)", end="")

day = int(input())

age_in_day(day)
