def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        value = add(a, b)
        for i in range(4, 6):
            value = add(value, i)
        return(value)

    return(sub(a, b))
