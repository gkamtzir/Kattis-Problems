import operator, math, sys

number_of_test_cases = int(sys.stdin.readline())

operators = ['*', '//', '+', '-']

for i in range(number_of_test_cases):

    n = int(sys.stdin.readline())
    
    results = []

    for operator_i in operators:
        for operator_j in operators:
            for operator_k in operators:
                string = '4 ' + operator_i + ' 4 ' + operator_j + ' 4 ' + operator_k + ' 4'
                result = math.floor(eval(string))
                string += ' = ' + str(result)
                string = string.replace('//', '/')
                results.append({
                    'result': result,
                    'string': string
                    })
    found = False

    for result in results:
        if result['result'] == n:
            found = True
            print(result['string'])
            break

    if not found:
        print('no solution')
