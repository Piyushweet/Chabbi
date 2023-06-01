
'''Something fishy there -
Find output of following:'''


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

# f(2)
'''This give us the result [0,1] 
as intially the list is emppty and 0*0 | 1*1'''

# f(3,[3,2,1])
'''this give the output as [3,2,1,0,1,4] 
as intially the list is given [3,2,1] 
and now it append the previous one so that 0*0|1*1|2*2]'''

# f(3)
'''this give us the [0,1,0,1,4] 
as the previous state of the list is retained due to the default argument 
and now the list continue to append to 0*0|1*1|2*2'''

'''So the overall result 
[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 0, 1, 4]'''