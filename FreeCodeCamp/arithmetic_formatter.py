import operator

def arithmetic_arranger(problems, bool_v=False):
    
    #if number of problems exceeds 5, return error.
    if len(problems) > 5:
        return 'Error: Too Many Problems'
     
    #dictionary for operation values
    ops = {'+': operator.add, '-': operator.sub}
    
    #list for numerical values, operators, formatting dashes and solution.
    top = []
    calculation = []
    dash = []
    solution = []
    
    #split problem list into separate values, add to list according to appearance in formatter
    #first value at top, calculation value (operator and second value), dash set at length of longest value, solution
    
    for item in problems:
        new_item =item.split(' ')
        if new_item[1] not in ops:
            return 'Error: Operator must be "+" or "-"'
        if not new_item[0].isnumeric() or not new_item[2].isnumeric():
            return 'Error: Numbers must only contain digits'
        
        #store variable for calculating solution
        solution_input = str(ops[new_item[1]](int(new_item[0]), int(new_item[2])))                                        
        
        #store variable for length of longest value
        length = max(len(new_item[0]), len(new_item[2])) + 2
        
        top.extend(str('    ' + new_item[0].rjust(length)))
        calculation.extend('    ' + new_item[1] + str(new_item[2]).rjust(length - 1))
        dash.extend(str('-'* length).rjust(length + 4))
        solution.extend(str(solution_input.rjust(length + 4)))
    
    #join list into printable statement
    statement = [''.join(top), ''.join(calculation), ''.join(dash), ''.join(solution)]
    
    #check if solution required
    if bool_v:
        return f"{statement[0]}\n{statement[1]}\n{statement[2]}\n{statement[3]}"
    
    if not bool_v:
        return f"{statement[0]}\n{statement[1]}\n{statement[2]}"

 
arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], True)
