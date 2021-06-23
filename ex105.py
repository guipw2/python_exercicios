def grade(* note, sit=False):
    '''
    -> Function to analyze grades and situations of several students.
    :param note: one or more student grades (accepts several)
    :param sit: optional value, indicating whether or not to add the situation
    :return: dictionary with various information about the class situation
    '''
    dc = dict()
    dc['total'] = len(note)
    dc['highest grade'] = min(note)
    dc['lowest grade'] = max(note)
    dc['average'] = f"{sum(note) / len(note):.2f}"
    if sit:
        if sum(note) / len(note) < 5:
            dc['situation'] = 'BAD'
        elif 5 <= sum(note) / len(note) < 7:
            dc['situation'] = 'REASONABLE'
        else:
            dc['situation'] = 'GOOD'
    return print(f'{dc}')


grade(10, 5.5, 8, 7, sit=True)
