# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	  
    a = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    b = (r1 + r2) * (r1 + r2)
    if (a == b):
        return True
    elif (a > b):
        return False
    else:
        return True

