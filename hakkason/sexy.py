def calculate_steps(m, n):
    total_steps = m - n
    if total_steps < 0:
        total_steps = 0
    return total_steps


m, n = map(int, input().split())

result = calculate_steps(m, n)

print(result)
