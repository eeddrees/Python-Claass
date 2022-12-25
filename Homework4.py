
#ЗАД 1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = my_list[::2]
print(even)

#ЗАД 2
d_= [4,9,6,7,4,2,0,55,4,3,77,8,5]

def list_(x):
    new_list= []
    s  = 0
    for i  in x:
        if i>=s:
            new_list.append(i)

            s= i

        else:
            s=i
            continue

    return new_list[1:]     


print(list_(d_))

#ЗАД 3

A = [3,6,0,7,10,5,6,9]

def swap_min_max(A):
    x = max(A)
    y = min(A)
    A[A.index(x)] = y
    A[A.index(y)] = x
    
    print (A)
    
    
swap_min_max(A)

#ЗАД 4

def keys_(a,y):
     print(a[y])
    

a = {'a':'HELLO', 'b': 'WORLD'}
keys_(a,'b')

