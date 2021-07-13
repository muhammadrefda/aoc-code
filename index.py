range_of, range_up_to = 357253,892943

solution = 0
for password in range(range_of, range_up_to):
    text = str(password)
    double = False
    for x in range(5):
        if text[x] == text[x+1]:
            double = True
    increasing = True
    for x in range(5):
        if text[x] > text[x+1]:
            increasing = False
    if double and increasing: solution += 1

print(solution)