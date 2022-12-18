def calculate_investment_value(initial_value, percent_age, years):
    result = initial_value * (1 + percent_age / 100) ** years
    return result