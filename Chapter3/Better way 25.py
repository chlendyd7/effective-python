def safe_division(number, divisor,
                  ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division(1.0, 10**500, True, False)
print(result)

result = safe_division(1.0, 0, False, True)
print(result)

def safe_division_b(number, divisor,
                    ignore_overflow=False,       # 변경
                    ignore_zero_division=False): # 변경
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division_b(1.0, 10**500, ignore_overflow=True)
print(result)

result = safe_division_b(1.0, 0, ignore_zero_division=True)
print(result)

assert safe_division_b(1.0, 10**500, True, False) == 0


def safe_division_c(number, divisor, *,         # 변경
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# safe_division_c(1.0, 10**500, True, False)

result = safe_division_c(1.0, 0, ignore_zero_division=True)
assert result == float('inf')