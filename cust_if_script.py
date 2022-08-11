#!/usr/bin/env python3

message = 'You recieved an '

connection = int(input("What is your score from  0 - 100 (enter whole numbers only)?: "))

if connection > 100:
    message = 'You are an overachiever, or you cannot read directions...'
elif connection >= 90:
    message = message + 'A, Great job keep up the great work.'
elif connection >= 80:
    message = message + 'B, Good job keep working hard for that A.'
elif connection >= 70:
    message = message + 'C, OK you might need to do some more studying.'
elif connection >= 60:
    message = message + 'D, Ouch you failed and should spend some more time studying.'
elif connection <= 59:
    message = message + 'F, This was not good please try harder.'
else:
    message = 'Please read the directions again and enter a valid score.'
print(message)

