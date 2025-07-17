def bubble_sort(numbers):
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
        user_input = input().strip()
        
        # 빈 입력 체크
        if not user_input:
            print("Invalid input.")
            return
        
        # 공백으로 분리하여 숫자 리스트 생성
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
        
        # 결과 출력 (float 형태로)
        result = "Sorted: " + " ".join(str(float(num)) for num in sorted_numbers)
        print(result)
        
    except Exception:
        print("Invalid input.")

if __name__ == "__main__":
    main()
