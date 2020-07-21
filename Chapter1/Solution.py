import math
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
#C-1.14
def has_odd_product(data):
    count_odd_numbers = 0
    for datumn in data:
        if datumn&1 == 1:
            count_odd_numbers += 1
            if count_odd_numbers >= 2:
                return True

    return False

print(has_odd_product([2,6,4,5]))   

#C- 1.15
def check_distinct(data):
    result = True
    set_numbers = set()
    for datumn in data:
        if datumn in set_numbers:
            result = False
            break
        else:
            set_numbers.add(datumn)
    return result

print("check_distinction")
print(check_distinct([2,3,4,5]))


def p_norm(p,data):
    sum = 0
    for datumn in data:
        sum +=math.pow(datumn,p)

    return math.pow(sum,1/p)

print(p_norm(2,[3,4]))

