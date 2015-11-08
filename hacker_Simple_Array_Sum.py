
lista = [1,2,3,4,5,6]


def func_1(point):
    sum = 0
    for i in range(len(point)):
        sum += point[i]
    print(sum)

func_1(lista)


def Simple_Array_Sum(point):
    sum = 0

    for i in range(len(point)):
        sum += point[i]
    print(sum)

Simple_Array_Sum(lista)



def simple_array_sum():
    n = int(input())
    a, b, c, d, e, f = input().split()

    for i in range(0,n):


# simple_array_num()

'''
def solveMeSecond(a,b):
   return a+b
n = int(input())
for i in range(0,n):
    a, b = input().split()
    a,b = int(a),int(b)
    res = solveMeSecond(a,b)
    print (res)
'''