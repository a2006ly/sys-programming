#!/usr/bin/python3

#count = 4
#s = "Number   of  goals: " 
#print(s + str(count))

#count = 9
#print(s + str(count))

#count = 11
#print(s + str(count))
g1 = "Number  of  goals:"
def goal(count):
    if count < 10:
        s1= g1 +str(count)
        return s1
    else:
        return g1 + "many"

print(goal(4))  
print(goal(9))  
print(goal(10)) 
print(goal(99))


