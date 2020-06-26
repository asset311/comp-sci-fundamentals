
'''
8.2 Evaluate RPN expressions
A string is in RPN notation if:
 1) A single digit or a sequence of digits, prefixed with an option -, e.g. '6', '123', '-42'
 2) It is of the form "A,B, o" where A and B are RPN expressions and 'o' is one of +,-,x,/
'''
# expression = '3,4,+,2,*,1,+'
def evaluate(expression):
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y,x : x + y,
        '-': lambda y,x: x - y,
        '*': lambda y,x: x * y,
        '/': lambda y,x: int(x / y) 
    }

    intermediate_results = []

    for token in expression.split(DELIMITER):
        if token in OPERATORS:
            intermediate_results.append(
                OPERATORS[token](
                    intermediate_results.pop(),
                    intermediate_results.pop()
                )
            )
        else:   #token is a number
            intermediate_results.append(int(token))
    
    return intermediate_results[-1]

