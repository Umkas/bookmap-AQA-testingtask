# bookmap-AQA-testingtask
## Arithmetic Unit Tests in Python

### Goal
This project verifies basic arithmetic operations using Python as both the testing and calculation tool.  
The tests are implemented manually without any testing framework to keep them simple and terminal-friendly.

---

### Covered Operations
- **Addition**: `2 + 3 == 5`  
- **Subtraction**: `10 - 7 == 3`  
- **Multiplication**: `4 * 5 == 20`  
- **Division**: `9 / 2 == 4.5`

---

### Edge Cases and Error Handling

#### Floating point precision loss:
- `-4.3 + 3.4` gives `-0.899999...`, not exactly `-0.9`
- `0.1 + 0.2` is not exactly `0.3`

#### Division by zero:
- `1 / 0` raises `ZeroDivisionError`

#### Invalid operand types:
- `"abc" + 1` raises `TypeError`
- `"1" + 1` raises `TypeError`

#### Alternative decimal notation:
- `.56` is treated as `0.56` by Python and is of type `float`

---

### Tests

| Function                             | Description                                      |
|--------------------------------------|--------------------------------------------------|
| `test_addition()`                    | Tests integer addition                           |
| `test_decimals_w_point()`            | Float sum with visible precision loss            |
| `test_subtraction()`                 | Simple subtraction                               |
| `test_multiplication()`              | Integer multiplication                           |
| `test_division()`                    | Float division                                   |
| `test_division_by_zero()`            | Checks `ZeroDivisionError`                       |
| `test_string_operand()`              | Adding string + int → `TypeError`                |
| `test_symbol_operand()`              | Adding str-digit + int → `TypeError`             |
| `test_classic_decimal_bug()`         | Demonstrates `0.1 + 0.2 != 0.3`                  |
| `test_decimal_with_tolerance()`      | Float comparison using a tolerance (`1e-9`)      |
| `test_float_without_leading_zero()`  | Verifies `.56 == 0.56` and is of type `float`    |

---

### How to Run

#### Option 1: via Bash
```bash
chmod +x run.sh
./run.sh
```
#### Option 2: via Bash
python unit-tests.py