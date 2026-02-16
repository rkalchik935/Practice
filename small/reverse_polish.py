def evaluate_rpn(expression):
    stack = []

    for i in expression.split():
        try:
            num = int(i)
            stack.append(num)
            print(f"Push {i} onto stack")
        except ValueError:
            b = stack.pop()
            print(f"Pop {b} from stack")
            a = stack.pop()
            print(f"Pop {a} from stack")
            
            if i == "-":
                stack.append(a - b)
                print(f"Push {a - b} onto stack")
            elif i == "+":
                stack.append(a + b)
                print(f"Push {a + b} onto stack")
            elif i == "*":
                stack.append(a * b)
                print(f"Push {a * b} onto stack")
            elif i == "/":
                stack.append(int(a / b))
                print(f"Push {int(a / b)} onto stack")
    
    return stack[0]

print(evaluate_rpn("1 2 + -3 *"))