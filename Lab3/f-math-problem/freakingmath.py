import random 
import calc_slect


def generate_quiz():
    x = random.randint(0,20)
    y = random.randint(0,20)
    error = random.randint(-1,1)
    operator = ["+","-","*","/"]
    op = random.choice(operator)
    result = calc_slect.eval(x,y,op)+error
    return [x,y,op,result]
    

def check_answer(x, y, op, result, user_choice):
    t = calc_slect.eval(x,y,op)
    check = None
    if user_choice == True:
        if t == result:
            check = True
        else :
            check = False
    if user_choice == False:
        if t != result:
            check = True
        else :
            check = False
    return check