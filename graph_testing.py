
def isNumber(input_values):
    seq = [_ for _ in input_values.split(',')]
    for item in seq:
        if not isinstance(item, (int, float)):
            return False
    return True


input_values = "1,2,3,4,5"

if isNumber(input_values):
    print(f"{input_values} is a number")
else:
    print(f"{input_values} is not a number")

