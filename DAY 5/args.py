#def a_sum(*args):
    #total=0

    #for arg in args:
        #total += arg
    #return total
#print(a_sum(5,6,5))

def a_sum(*args):
    return sum(args)
print(a_sum(5,6,5,6,80))