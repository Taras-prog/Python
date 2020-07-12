a=10
b=0
c=1
d=[a]

for i in range(a) :
    temp = b
    b=a
    a+=temp
    d.append(a)
    print('Fibonacci number for {} is {}'.format(a,b))
    
# %%

