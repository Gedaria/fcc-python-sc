def arithmetic_arranger(problems, show_answers=False):
    from re import match, search

    problems_length = len(problems)

    if problems_length > 5:
        return "Error: Too many problems."
    if problems_length == 0:
        return "Error: there is no input or the input is not a list"

    problems_stripped = []

    for prob in problems:
        expression = prob.replace(" ", "")
        problems_stripped.append(expression)

    del problems

    for prob in problems_stripped:
        if match(r"^[0-9]{1,4}[+\-][0-9]{1,4}$", prob):
            continue
        if match(r"^[0-9]{1,4}[+\-*/][0-9]{1,4}$", prob):
            return "Error: Operator must be '+' or '-'."
        if match(r"^[0-9]+[+\-*/][0-9]+$", prob):
            return "Error: Numbers cannot be more than four digits."
        if search(r"[^0-9+\-*/]", prob):
            return "Error: Numbers must only contain digits."
        return "Invalid Format"

    # prepare a list that will have the num1, operator, num2, and equal_line_length
    # this will be used to print out the expressions horizontally

    problems_tuple = []
    for problem in problems_stripped:
        expressions = match(r"(\d{1,4})([+\-])(\d{1,4})", problem).groups()
        problems_tuple.append(expressions)

    # loop to parse each tuple prob in the list and print out the expression in an organized way

    problems_tuple_for_printing = []

    for prob_tuple in problems_tuple:
        # assign num1, num2, and the operator to the strings in the tuple
        num1, operator, num2 = prob_tuple
        # conditional statements to determine the length of the spacing
        if len(num1) > len(num2):
            num1_spaces = 2
            num2_spaces = len(num1) - len(num2) + 1
        elif len(num1) < len(num2):
            num1_spaces = len(num2) - len(num1) + 2
            num2_spaces = 1
        else:
            num1_spaces, num2_spaces = 2, 1

        # conditional statement to determine the length of the equal line
        line_length = len(num1) + 2 if len(num1) > len(num2) else len(num2) + 2

        # conditional statement to determine result based on operator
        result = int(num1) + int(num2) if operator == "+" else int(num1) - int(num2)

        # determine the number of spacing for the result
        result_spacing = line_length - len(str(result))

        # make a tuple containing the info
        # needed to print the expressions horizontally
        tuple_for_printing = (
            num1,
            operator,
            num2,
            num1_spaces,
            num2_spaces,
            line_length,
            result_spacing,
            result,
        )

        # put the tuple into a list
        problems_tuple_for_printing.append(tuple_for_printing)

    output_lines = []

    list_counter = 0
    for prob_info in problems_tuple_for_printing:
        output_lines.append(" " * prob_info[3] + prob_info[0])
        if list_counter < problems_length - 1:
            output_lines.append("    ")
            list_counter += 1

    output_lines.append("\n")

    list_counter = 0
    for prob_info in problems_tuple_for_printing:
        output_lines.append(prob_info[1] + " " * prob_info[4] + prob_info[2])
        if list_counter < problems_length - 1:
            output_lines.append("    ")
            list_counter += 1

    output_lines.append("\n")

    list_counter = 0
    for prob_info in problems_tuple_for_printing:
        output_lines.append("-" * prob_info[5])
        if list_counter < problems_length - 1:
            output_lines.append("    ")
            list_counter += 1

    if show_answers:
        output_lines.append("\n")
        list_counter = 0
        for prob_info in problems_tuple_for_printing:
            output_lines.append(" " * prob_info[6] + str(prob_info[7]))
            if list_counter < problems_length - 1:
                output_lines.append("    ")
                list_counter += 1

    return "".join(output_lines)
