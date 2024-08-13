def counting_zeroes(*args):

    count=0

    for n in args:
        if args[count]==0 and args[count+1] ==0:
            return True
        else:
            count+=1

    return False

print(counting_zeroes(1,2,3,4,5,6,0,4,5,6))