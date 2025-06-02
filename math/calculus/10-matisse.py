def poly_derivative(poly):
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None

    derivative = [i * poly[i] for i in range(1, len(poly))]

    return derivative if any(derivative) else [0]
