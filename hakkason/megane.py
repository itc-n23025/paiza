def find_middle_number(N, numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    middle_index = (N + 1) // 2
    middle_number = sorted_numbers[middle_index - 1]
    return middle_number


N = int(input())
numbers = list(map(int, input().split()))

middle_number = find_middle_number(N, numbers)

print(middle_number)
