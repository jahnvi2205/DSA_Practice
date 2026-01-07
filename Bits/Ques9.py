def square(num):
    num= abs(num)
    temp= num
    result=0
    shift=0

    while temp>0:
        if temp&1:
            result= result+ (num<<shift)
        temp= temp>>1
        shift+=1

    return result