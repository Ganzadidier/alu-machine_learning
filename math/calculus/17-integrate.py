def poly_integral(poly, C=0):
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None
    if not isinstance(C, (int, float)):
        return None

    result = [C]
    for i, coeff in enumerate(poly):
        integral_coeff = coeff / (i + 1)
        # Use int if it's a whole number
        if integral_coeff.is_integer():
            integral_coeff = int(integral_coeff)
        result.append(integral_coeff)

    # Remove trailing zeros if they exist
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result
