def eye_exam():
    correct_answers = 0

    for _ in range(5):
        d, e = input().split()

        if d == e:
            correct_answers += 1

    if correct_answers >= 3:
        print("OK")
    else:
        print("NG")


eye_exam()
