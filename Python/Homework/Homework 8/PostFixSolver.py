# PostFixSolver.py

from Stack import Stack

'''pre: creates an empty LIFO stack
   post: returns result of postfix'''

def PostFixSolver(postfix): 

    stack = Stack() #creates empty stack

    for i in postfix: #iterates through every character in stack
        if i != " ": #checks if i is not " "
            if i in ("+-/*"): #checks if i is an element
                x = stack.pop() #assigns x to last pushed item
                y = stack.pop() #assigns y to last pushed item

                stack.push(str(eval(y + i + x))) #pushes y and x with the corresponding element

            else: #if its not an element it pushes it to the stack
                stack.push(i)
    return stack.top() #once done returns the last element in stack

P = PostFixSolver("3 4 5 + * 2 - 3 6 * +")

print(P)
