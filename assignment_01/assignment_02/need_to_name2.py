x = 5
if x > 2:  # true so continues
    x = -3 # x is now assigned value of -3
if x > 1:  # false, but continues; x is still -3
    x = 1  # does execute because prior line is false
else:      # true and is last test so is true
    x = 3  # final else is a catch all, so it changes x to 3
print(x)   


x = 5
if x > 2:   # true
    x = -3  # true so -3 is assigned to x
elif x > 1: # false, so testing is over; so catch all else is not executed
    x = 1   # not executed because prior line is false
else:       # not executed because elif ends process 
    x = 3
print(x)   

