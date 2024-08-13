#def a_sum(**kwargs):

    #for key, value in kwargs.items():
        #print(f'{key}={value}')
#a_sum(x=3,y=5,z=2)


#def a_sum(**kwargs):
    #total = 0
    #for key, value in kwargs.items():
        #print(f'{key}={value}')
        #total +=value
    #return total
#print(a_sum(x=3,y=5,z=2))


def test(num1,num2,*args,**kwargs):
    print(f'The first number is {num1}')
    print(f'The second number is {num2}')

    for arg in args:
        print(f'args={arg}')

    for key, value in kwargs.items():
        print(f'{key}={value}')

args=[100,200,300,400]
kwargs={'x':'one','y':'two','z':'three'}

test(15,50,*args,**kwargs)