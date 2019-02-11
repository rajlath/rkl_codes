import re
equation = "15 7 1 1 + − ÷ 3 × 2 16 8 + + +"

def eval_rpn_left_right(equation):
    '''stack to hold values'''
    stack = []
    '''create tokens from equation separating values and operator'''
    equation_tokens = [x for x in equation.split()]
    '''
    Iterate through tokens
    1.If current token is a value deposit it to stack
    2.if operator, get last two operand from stack
    3.calculate its value using operator
    4.push result to stack
    '''
    operators = ["+","-","÷","×" ]
    for i in equation_tokens:
        #check if i is a value, if it is add to stack
        if re.match(r"\d+", i):
            stack.append(i)
        else:
            #i is an operator , process it
            operator = i
            result   = 0
            second   = int(stack.pop())
            first    = int(stack.pop())
            print(first, second, operator)
            if   operator == "+":result = first + second
            elif operator == "÷":result = first // second
            elif operator == "×":result = first * second
            else:result = first - second
            '''
            push result to stack
            '''
            print(result)
            stack.append(str(result))

        print(stack)


    '''
    all tokens are processed.
    result is the value in the stack
    return result from stack
    '''
    return result




print(eval_rpn_left_right(equation))
