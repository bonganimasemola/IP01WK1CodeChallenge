## Challenge 1: Converting 12-hour time to 24-hour time

def every_hour(hour, minute, period):
     # confirm input is valid 
    if not (1 <= hour <= 12) or not (0 <= minute <= 59) or period.lower() not in ['am', 'pm']:
        print("Invalid input")
     # convert 12-hour time to 24-hour time
    if period.lower() == 'pm':
        hour += 12
        # make sure hour remains 12:00 pm and not change to 24:00 
        if hour == 24:
            hour = 12
     #format the time to four-digit string       
    result = f"{hour:02d}{minute:02d}"
    return result
            
# hour_input = 9
# minute_input = 21
# period_input = "am"
# result = every_hour(hour_input, minute_input, period_input)
# print(result)


## Challenge 2: Two numbers are positive

 def is_positive(num1, num2, num3):
     pass





## Challenge 3: Consoant value 