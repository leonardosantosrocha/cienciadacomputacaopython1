def fatorial(n):
    if n < 0:
        return 0
    i = f = 1
    while i <= n:
        f *= i
        i += 1
    return f

def test_fatorial_0():
    assert fatorial(0) == 1

def test_fatorial_1():
    assert fatorial(1) == 1

def test_fatorial_negativo():
    assert fatorial(-10) == 0

def test_fatorial_4():
    assert fatorial(4) == 24

def test_fatorial_5():
    assert fatorial(5) == 120