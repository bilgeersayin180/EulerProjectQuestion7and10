import math
def isPrime(num):
    limit = int(math.sqrt(num))
    for i in range(2, limit + 1):
        if (num % i == 0):
            return False
    return True

SumOf = 0

for j in range(2,2000000):
    if(isPrime(j)):
        SumOf += j

print("Ans of the 10th question: ",SumOf)

bigNum = 0
i = 2
count = 0
run = True
while(count < 10001):
    if ((isPrime(i) and (i > bigNum))):
        bigNum = i
        count += 1
    i += 1
print("Ans of the 7th question: ",bigNum)
