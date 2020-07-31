def convert(num, base, change): # base진수로 된 num을 change진수로 변환. 단 16진수는 불가능.
    multiplier, result = 1, 0
    while num > 0:
        result += num % change * multiplier
        multiplier *= base
        num = num // change
    return result

def test_convert():
    try:
        assert(convert(1111, 2, 10) == 15)
        assert(convert(1111, 8, 10) == 585)
        assert(convert(9, 10, 2) == 1001)
        print("test finish!")
    except: print("test error!")

if __name__ == "__main__":
    test_convert();
