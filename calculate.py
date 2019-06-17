from scipy import optimize
import numpy as np
import math
from decimal import Decimal #maybe using this I can fix the math error

#calculate2 will attempt to create two list objects and increment based on distance rather than radius. the two list objects create pairs of values. also will save to a text file.

def intersectionArea(d,r):
    return float(r*r*(2*math.acos(d/(2*r))-math.sin(2*math.acos(d/(2*r)))))
#source of equation: http://mathforum.org/library/drmath/view/54785.html
#it is unclear to me how to show that cos(CBD)= d^2r/2d but otherwise i believe this equation is valid.

# radius we want (will be an array of values once I get this working)
#r2 = 10/A

#new value which is the set of distances
fib=[0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 218922995834555169026]
nums = list(reversed(fib)) #the starting value for this range has to be modified based on area size.
#18,


def approximateDist(r2,A):
    #inc = float(0.01)
    incstart = float(10) #10 works wel
    incc = float(0.8)
    dec=2 #decimal places of specificity # this variable isnt even used lol delete it
    p = 0.1 #tolerance

    #better seed value, using limitation of arccos
    # d <= 2r
    #n = (3*r2*r2) - r2
  #  n = 0.2*r2 #d, distance start seed
    n = 1400
    i=0
    #two booleans. when the alg has gone too far in one direction, incrememnts become smaller
    pos = False
    neg = False
    while (abs(A - np.nan_to_num(intersectionArea(n,r2))) >= p):
        if neg == True & pos == True:
            pos = False
            neg = False
            incc = incc*incc
            print(":)")
        elif (A - np.nan_to_num(intersectionArea(n,r2))) > 0:
            n = n - incstart*incc
            neg = True
            print(intersectionArea(n,r2),"too big")
        elif ((A - np.nan_to_num(intersectionArea(n,r2))) < 0)  :
            n = n + incstart*incc
            pos =True
            print(intersectionArea(n,r2),"too small") #too small is in the distance is too small => area is too big
    print(n)
    print(A-intersectionArea(n,r2))
    print("YAYY!!")
    return n


def approximateRadius(d,A):
    #I decided to create two functions because behavior for tolerance/increment choice might be difference, if i ever try to make those automatically chosen.
    #inc = float(0.01)
    incstart = float(d/5) 
    incc = float(.8)
    p = 0.1 #tolerance
    n =  d/2 +5 # NEED TO FIND A WAY TO GET THIS TO GUESS.
    #debug note -- 33.38555 is extremely close to the actual value. my estimator should be efficent and not deviate too far.
    i=0
    #two booleans. when the alg has gone too far in one direction, incrememnts become smaller
    pos = False
    neg = False

    #ADD A TRY BLOCK FOR THIS WHILE STATEMENT TO CATCH ERRORS AND ADJUST THE N VALUE.
    while (abs(A - np.nan_to_num(intersectionArea(d,n))) >= p):

        try:
            if neg == True & pos == True:
                pos = False
                neg = False
                incc = incc*incc
                print("flip")
            elif (A - np.nan_to_num(intersectionArea(d,n))) > 0:
                n = n + incstart*incc
                neg = True
                print(n,"toosmall")
                print(intersectionArea(d,n),(A - np.nan_to_num(intersectionArea(d,n))), "too small")
 #               print("inc:", incc)
            elif ((A - np.nan_to_num(intersectionArea(d,n))) < 0 )  :
                n = n - incstart*incc #opposite of dist fn, because rrelationship between area and radisu is direct.
                pos =True
                print(n,"toobig")
#                print(d,n,intersectionArea(d,n),"too small")

                
                
        except ValueError:
                print("value error")
                if neg == True:
                    n = n + incstart*incc

                elif pos == True:
                    n = n - incstart*incc
                    
                incc = incc - incc*0.1                  
#                neg = True
#                pos = True


                    	
    print(n)
    print(A-intersectionArea(d,n))
    print("YAYY!!")
    return n

#output two new list of corresponding values
distnums = list()
radiusnums = list()

variableswitch = False # False: estimate radius. True: estimate distance

if variableswitch == True:
    for i in range(0,len(nums)):
        distnums.append(approximateDist(nums[i],float(1000))) #r, A
        radiusnums.append(nums[i])
elif variableswitch == False:
    for i in range(0,len(nums)):
        radiusnums.append(approximateRadius(nums[i],float(1000))) #r, A
        distnums.append(nums[i])
