def test_addition():
    assert 2 + 3 == 5, "2 + 3 must be 5"
    
def test_decimals_w_point():
#    assert -4.3 + 3.4 == -0.9, " -4.3 + 3.4 must be -0.9 "
    assert abs((-4.3 + 3.4) - (-0.9)) < 1e-9, "-4.3 + 3.4 must be -0.9"
    
def test_subtraction():
    assert 10 - 7 == 3, "10 - 7 must be 3"

def test_multiplication():
    assert 4 * 5 == 20, "4 * 5 must be 20"

def test_division():
    assert 9 / 2 == 4.5, "9 / 2 must be 4.5"

def test_division_by_zero():
    try:
        _ = 1 / 0
        assert False, "expected ZeroDivisionError"
    except ZeroDivisionError:
        pass  

def test_string_operand():
    try:
        _ = "abc" + 1
        assert False, "expected TypeError when adding str and int"
    except TypeError:
        pass
        
def test_symbol_operand():
    try:
        _ = "1" + 1
        assert False, "expected TypeError when adding str-digit and int"
    except TypeError:
        pass        

def run_all():
    test_addition()
    test_decimals_w_point()
    test_subtraction()
    test_multiplication()
    test_division()
    test_division_by_zero()
    test_string_operand()
    test_symbol_operand()
    print("All tests passed successfully.")

if __name__ == "__main__":
    run_all()