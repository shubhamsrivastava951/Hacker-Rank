def gradingStudents(grades):
    #
    # Write your code here.
    #
    new_grades = [] 
    for g in grades:
        r = g%5
        if g < 38:
            pass 
        else:
            if r > 2:
                g = g + ( 5-r )
        new_grades.append(g)
    return new_grades 