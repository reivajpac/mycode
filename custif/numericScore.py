#!/usr/bin/env python3

message = 'Numeric score: '

# wrap connection in a float() to accept decimals as numbers
score = int(input("What is the numeric score? "))

# if input value was higher or equal to 25
if score >= 90 and score <= 100 :
    message = message + 'A'
elif score >= 80 and score <=89:
    message = message + 'B'
elif score >= 70 and score <= 79:
    message = message + 'C'
elif score >= 60 and score <= 69:    
    message = message + 'D'
elif score >= 0 and score <= 59:
    message = message + 'F'
else:
    message = 'The numeric score: '+ str(score) +' is not on a valid range -  Valid score range: 0 - 100'
print(message)

