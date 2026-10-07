def positive_negative(a):
    if a > 0:
        return "Positive"
    elif a < 0:
        return "Negative"
    else:
        return "Zero"


print("positive or negative number",positive_negative(10))