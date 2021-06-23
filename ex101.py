def vote(year):
    from datetime import date
    current = date.today().year
    age = current - year
    if age < 16:
        return f"With {age} years: DON'T VOTE "
    elif 16 <= age < 18 or age > 65:
        return f"With {age} years: OPTIONAL VOTE"
    else:
        return f"With {age} years: MANDATORY VOTE"


print(vote(int(input('What year were you born?:'))))
