def validate_resident_number(resident_number):
    if len(resident_number) != 13:
        return False  # 주민등록번호는 13자리여야 합니다.

    # 주민등록번호에서 '-'를 제거합니다.
    resident_number = resident_number.replace("-", "")

    # 주민등록번호의 앞 12자리와 마지막 1자리를 나눠서 저장합니다.
    first_12_digits = resident_number[:12]
    last_digit = int(resident_number[12])

    # 주민등록번호의 첫 자리는 성별 및 외국인 여부를 나타냅니다.
    first_digit = int(first_12_digits[0])

    # 성별 및 외국인 여부 체크
    if not (1 <= first_digit <= 8):
        return False

    # 각 자리에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 곱하고 모두 더합니다.
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    weighted_sum = sum(int(digit) * weight for digit, weight in zip(first_12_digits, weights))

    # 11로 나눈 나머지를 구합니다.
    remainder = weighted_sum % 11

    # 11에서 나머지를 뺍니다.
    subtracted = 11 - remainder

    # 계산 결과와 주민등록번호의 마지막 자리를 비교하여 유효성을 판단합니다.
    if subtracted == last_digit:
        return True
    elif subtracted == 10 and last_digit == 0:
        return True
    else:
        return False

# 주민등록번호를 입력 받습니다.
resident_number = input("주민등록번호를 입력하세요 (예: 123456-1234567): ")

if validate_resident_number(resident_number):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
