def convert_seconds(total_seconds):
    hours = total_seconds // 3600 
    
    total_seconds %= 3600     
    
    minutes = total_seconds // 60  
    seconds = total_seconds % 60 
    
    return hours, minutes, seconds

total_seconds = int(input("Enter total seconds: "))
hours, minutes, seconds = convert_seconds(total_seconds)

print(f"{hours}:{minutes}:{seconds}")
