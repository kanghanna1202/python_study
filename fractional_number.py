from fractions import Fraction

def rounding_floats(number1, places):
    # 소수 반올림
    return round(number1, places)

def float_to_fraactions(number):
    # 소수를 분수로
    return Fraction(*number.as_integer_ratio()) # 소수 값인 number를 나누기 전 값으로 바꿈(.as_integer_ratio)

def get_denominator(number1, number2):
    # 분모 반환
    a = Fraction(number1, number2)
    return a.denominator # 분모 반환(.demoniater) == return number1

def get_numerator(number1, number2):
    # 분자 반환
    a = Fraction(number1, number2)
    return a.numerator # 분자 반환(.numerator) == return number2

def test_testing_floats():
    number1 = 1.25
    number2 = 1
    number3 = -1
    number4 = 5/4
    number5 = 6
    assert(rounding_floats(number1, number2) == 1.2) # 1.25를 소숫점 둘째 자리에서 반올림 == 1.2
    assert(rounding_floats(number1*10, number3) == 10) # 12.5를 정수에서 가장 가까운 수로 반올림 == 10
    assert(float_to_fraactions(number1) == number4) # 소수 1.25를 분수로 바꿈 == 5/4
    assert(get_denominator(number2, number5) == number5)
    assert(get_numerator(number2, number5) == number2)
    print("test finish!")

if __name__ == "__main__":
    test_testing_floats()
