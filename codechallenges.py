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

def is_positive(a, b, c):
    
    positive_count = 0
    
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2

# print(is_positive(4, -6, 9)) 
# print(is_positive(-4, 6, 0)) 


## Challenge 3: Consonant value 

def is_consonant(char):
    # Check if the alphabetical character is a consonant and separate out the vowel - "aeiou"
    return char.isalpha() and char.lower() not in "aeiou"

def max_consonant_value(s):
    max_value = 0
    current_value = 0

    for char in s:
        if is_consonant(char):
            
            current_value += ord(char.lower()) - ord('a') + 1
        else:
            
            current_value = 0

        # Update the maximum value if the current value is greater
        max_value = max(max_value, current_value)

    return max_value

# print(max_consonant_value("abcabc"))  
# print(max_consonant_value("xyz"))