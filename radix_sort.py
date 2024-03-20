from countingsort import *
import math

def radix_sort_simple(items):
    magnitude = 1
    
    for i in items:
        if i>0 and math.floor(math.log(i,10))>magnitude:
            # print("i",type(i),i)
            # print(math.floor(math.log(i,10)))
            magnitude = math.floor(math.log(i,10))
            print("newmag ",magnitude)
    print("magnitude",magnitude+1)
    for i in range(magnitude+1):
        items = counting_sort_stable(items,(lambda x:math.floor(x/(10**i))%10))
        print(items)
    return items

if __name__ == "__main__":
    bignum = 123456
    biggernum = 12345678
    smallnum = 12
    print(math.floor(bignum/(10**0))%10)
    # print(math.floor(biggernum/(10**2))%10)
    # print(math.floor(smallnum/(10**2))%10)
    
    bignums = [
        72345,
        63456,
        54567,
        45678,
        36789,
        27898,
        12834,
        34588,
        45405,
        96850,
        12345,
        1234,
        345,
        456,
        567,
        0,
        100000
    ]
    
    lessbignums = [
        1234,
        4321,
        33
    ]
    
    # print(list(map((lambda x:math.floor(x/(10**12))%10),bignums)))
    
    print(radix_sort_simple(bignums))