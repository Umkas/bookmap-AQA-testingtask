# bookmap-AQA-testingtask
# arithmetic unit-tests in Python

## goal
Write unit tests for +, -, * and / operations on numbers
 Tests has to run on Linux command line
 Test can be written in: Bash, Python, Java or Kotlin
 Can be used any form of communication with tested
software
	using directly if your language allows
	using some interposes communication if needed
 Find the limits of given software
 Check error reporting
 
## covered opations
Addition `2 + 3 == 5`
Subtraction `10 - 7 == 3`
Multiplication `4 * 5 == 20`
Division `9 / 2 == 4.5`

## edge cases and errors catching
 **floating point precision loss**:
  - `-4.3 + 3.4` gives `-0.899999...`, not exactly `-0.9`
  - `0.1 + 0.2` is not exactly `0.3`
 **division by zero*:
  - `1 / 0` raises `ZeroDivisionError`
 **invalid operand types**:
  - `"abc" + 1` raises `TypeError`
  - `"1" + 1` raises `TypeError`
 **alternative decimal notation**:
  - `.56` is treated as `0.56` by Python and is of type `float`

## tests 
 test_addition()              -Tests integer addition
 test_decimals_w_point()      -Float sum with visible precision loss
 test_subtraction()           -Simple subtraction
 test_multiplication()        -Integer multiplication
 test_division()              -Float division
 test_division_by_zero()      -Checks `ZeroDivisionError`
 test_string_operand()        -Adding string + int → `TypeError`
 test_symbol_operand()        -Adding str-digit + int → `TypeError`
 test_classic_decimal_bug()   -Demonstrates `0.1 + 0.2 != 0.3`
 test_decimal_with_tolerance() -Float comparison using a tolerance (`1e-9`)
 test_float_without_leading_zero() -Verifies `.56 == 0.56` and is `float`

## how to run
 install Pithin3
 
 - option with Bash:
 chmod +x run.sh
 ./run.sh

 - option to run Python script directly:
 python unit-tests.py
