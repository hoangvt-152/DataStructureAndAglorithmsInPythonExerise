#R-1.1
def is_multipe(n,m):
    return (n%m == 0)

print(is_multipe(5,3))    
print(is_multipe(6,3)) 

#R-1.2
def is_even(k):
    return k&1==0

print(is_even(2))
print(is_even(3))

#R-1.3
def minmax(data):
    if len(data) < 2:
        return None

    min = data[0]
    max = data[0]
    for datumn in data:
        if datumn < min:
            min = datumn
        if datumn > max:
            max = datumn         
    return (min,max)

#R-1.4
def sum_of_squares(n):
    sum = 0
    for i in range(n):
        sum = sum + i*i

    return sum

print(sum_of_squares(4))        

#R-1.6
def sum_of_odd_squares(n):
    sum = 0
    for i in range(1,n,2):
        sum = sum + i*i
    return sum

print(sum_of_odd_squares(9))       

#R-13
def reserves_list(data):
    size_of_data = len(data)
    haft_size_of_data =size_of_data//2
    for i in range(0,haft_size_of_data):
        tmp = data[i]
        data[i]=data[size_of_data - 1 -i]
        data[size_of_data - 1 -i] = tmp
    return data    
    

print(reserves_list([1,2,3,4,5,6]))
#R-1.15    