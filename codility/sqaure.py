


import math 



def solution(A,B):
    
    sq = set()
    for i in range(4,B):
        
        sq.add(int(math.sqrt(i) + 0.5) **2)

    return len(sq)
             
        #print(math.sqrt(i))
def is_square(a):
    count = 0 
   # print(a)
    for i in a:
        print(i)
        #root = math.sqrt(i)
       # print(root)
        #if int(math.sqrt(i) + 0.5)** 2 == i:
          #  print('yes')
           # return count 
       

    """
    root = math.sqrt(a)
    if int(root + 0.5) ** 2 == a:
        return True
    else:
        return False 

"""
print(solution(4,17))
