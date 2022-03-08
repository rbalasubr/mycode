#!/usr/bin/env python3


score = int(input('Enter Numeric Score: '))

if score >= 90 and score <= 100:
    print(f'Letter grade for numeric score {score} is A')

elif score >= 80 and score <= 89:
    print(f'Letter grade for numeric score {score} is B')

elif score >= 70 and score <= 79:
    print(f'Letter grade for numeric score {score} is C')

elif score >= 60 and score <= 69:
    print(f'Letter grade for numeric score {score} is D')

elif score <= 59:
    print(f'Letter grade for numeric score {score} is F')
