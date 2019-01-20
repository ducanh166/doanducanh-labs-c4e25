def eval(x ,y, op):

    rs = 0

    if op == "+":
        rs = x + y
    elif op =="-":
        rs = x - y
    elif op =="*":
        rs = x * y
    elif op =="/":
        rs = x / y
    return rs
    
# a = int(input("a = "))
# b = int(input("b = "))
# op = input("op =")
# r = eval(a, b, op)
# print(r)
# #print(result)
