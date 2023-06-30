def display_progress(s, t):
    progress = "-" * s
    progress = progress[: t - 1] + "+" + progress[t:]
    return progress


s = int(input())
t = int(input())

result = display_progress(s, t)
print(result)
