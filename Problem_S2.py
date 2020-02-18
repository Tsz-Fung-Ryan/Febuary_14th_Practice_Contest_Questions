from pathlib import Path

def find_Primes(x):
    for i in range (1,x//2):
        p1= i
        #print(p1)
        if(is_Prime(p1)):
            #print(p1, "is prime")
            p2 = x - p1
            if(is_Prime(p2)):
                #print(p2, " is prime")
                #print(p1, " ", p2, " is the answer")
                return [p1,p2]
def is_Prime(x):
    for i in range(2,x):
        if(x%i==0):
            #print(x, "is not prime")
            return False
    return True

inputFile = open("all_data\s2\s2.1-11.in", 'r')
lines = inputFile.readlines()[1:]
for line in lines:
    print(line)
    answer = find_Primes(int (line)*2)
    print(answer)
inputFile.close()
