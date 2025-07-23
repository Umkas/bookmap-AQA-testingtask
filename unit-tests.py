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
        
def test_classic_decimal_bug():
    result = 0.1 + 0.2
    assert result != 0.3, f"expected floating point inaccuracy, but got exact match: {result}"        

def test_decimal_with_tolerance():
    result = -4.3 + 3.4
    assert abs(result - (-0.9)) < 1e-9, f"wxpected approx -0.9, got {result}"
    
def test_float_without_leading_zero():
    """
    check that Python treat .56 as 0.56
    """
    assert .56 == 0.56, "Python should treat .56 as 0.56"
    assert type(.56) is float, "Expected type float for .56"    
    
def run_all():
    """   
    test_addition()
    test_decimals_w_point()
    test_subtraction()
    test_multiplication()
    test_division()
    test_division_by_zero()
    test_string_operand()
    test_symbol_operand()
    test_classic_decimal_bug()
    test_decimal_with_tolerance()
    test_float_without_leading_zero()
    print("All tests passed successfully.")
    """
    tests = [
        test_addition,
        test_decimals_w_point,
        test_subtraction,
        test_multiplication,
        test_division,
        test_division_by_zero,
        test_string_operand,
        test_symbol_operand,
        test_classic_decimal_bug,
        test_decimal_with_tolerance,
        test_float_without_leading_zero,
    ]
    
    failed = []
    passed = 0

    for test in tests:
        try:
            test()
            print(f"[PASS] {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"[FAIL] {test.__name__} — {e}")
            failed.append(test.__name__)
        except Exception as e:
            print(f"[ERROR] {test.__name__} — {type(e).__name__}: {e}")
            failed.append(test.__name__)

    print("\n--- Test summary ---")
    print(f"passed: {passed}")
    print(f"failed: {len(failed)}")

    if failed:
        print("failed tests:")
        for name in failed:
            print(f" - {name}")
        exit(1)  
    else:
        print("all tests passed successfully.") 

if __name__ == "__main__":
    run_all()