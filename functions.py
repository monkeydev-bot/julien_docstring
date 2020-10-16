def add(a, b):
    """
    add two arguments .
    AI-generated by Ponicode.
    """
    return a + b

def scalar_product(v1, v2):
    """
    compute the product of two vectors .
    AI-generated by Ponicode.
    """
    assert len(v1) == len(v2)
    scalar_product = sum(v1[i]*v2[i] for i in range(len(v1)))
    return scalar_product
