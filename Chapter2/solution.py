'''
12+345*6-78+9+10 = 2023
12+3/4*5*67*8-9+10 = 2023
1+2*34*5*6-7+8-9-10 =2023
1*2*3*456+7-8*9*10 = 2023
1/2*345*6+78+910 = 2023
 
10-9*87+65*43+2-1 =2023
10-9*8-76+5*432+1 = 2023
10*987/6+54/3*21 = 2023
10*98-7*6+543*2-1 = 2023


9*8+7+6*54*3*2*1 = 2023
9*8+7+6*54*3*2/1 = 2023
1+2*3+4*567*8/9  = 2023
'''

OPERATOR_LIST = ['','+','-','*','/']
YEAR = 2023
def build_input(start,end):
    arr =[]
    step = 1
    if start > end:
        step = -1
    arr.append(str(start))
    while(start != end):
        arr.append('')
        start = start + step
        arr.append(str(start))
    return arr 

def slove(n,size,input):
    if n < size:
        for  op in OPERATOR_LIST:
            input[n*2+1] = op
            slove(n+1,size,input) 
    else:
        expr = tranforms(input)
        if eval(expr) == YEAR:
            print(expr) 
def tranforms(arr_expr):
    expr = ''
    for c in arr_expr:
        if c !='':
            expr = expr + c
    return expr          
        
start = 1
end = 9
arr = build_input(start,end)
size = (end -start)  if end > start else (start - end)
print(arr)

slove(0,size,arr )

                
    