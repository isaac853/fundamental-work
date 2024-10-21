import numpy as np

myarray = np.zeros(5) # static, homogenous, contiguous, numerically indexed
print(myarray)

##lists
#-------------------------------------------------------

# mylist = [] #in python, this is a list

# mylist = [1,"bob",True,2.2] #heterogenous

# mylist[2] = False #mutable, indexed numerically

# mylist.append("cat") #dynamic and therefore non-contiguous





# ##tuple
#---------------------------------------------------------

# mytuple = (1,"bob",True,2.2) #heterogenous

# mytuple[1] = "steven" #immutable, 
# print(mytuple[1]) #numerically indexed

# mytuple.append(steven) this does not work therefore static, therefore likely contiguous

# print(hex(id(mytuple[1])))
# print(hex(id(mytuple[2])))

