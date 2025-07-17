def bubble_sort(numbers: list[float]) -> list[float]:
    """버블 정렬 알고리즘을 사용하여 숫자 리스트를 오름차순으로 정렬"""
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def main():
    try:
        # 사용자로부터 입력 받기
        user_input = input("숫자들을 입력해주세요: ").strip()
        
        # 빈 입력 체크
        if not user_input:
            print("Invalid input.")
            return
        
        # 공백으로 분리하여 문자열 리스트 생성
        input_list = user_input.split()
        numbers = []
        
        # 각 입력값을 float로 변환
        for item in input_list:
            try:
                num = float(item)
                numbers.append(num)
            except ValueError:
                print("Invalid input.")
                return
        
        # 버블 정렬로 정렬
        sorted_numbers = bubble_sort(numbers)

        # 문자열들을 저장할 빈 리스트 생성
        string_list = []
        
        # sorted_numbers에서 하나씩 꺼내서 처리
        for num in sorted_numbers:
            
            # 문자열로 변환
            str_num = "<" + str(num) + ">"
            
            # 리스트에 추가
            string_list.append(str_num)
        
        # 공백으로 이어서 하나의 문자열로 만들기
        joined_string = " ".join(string_list)
        
        result = "Sorted: " + joined_string
        
        print(result)
        
    except Exception:
        print("Invalid input.")


if __name__ == "__main__":
    main()
