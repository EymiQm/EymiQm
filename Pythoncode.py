# Mars Survival Energy Check

battery = 80
daily_use = 10

def check_battery(battery, daily_use):
    remaining = battery - daily_use
    
    if remaining > 20:
        return "Battery level is safe."
    else:
        return "Warning! Battery level is low."

result = check_battery(battery, daily_use)
print(result)
