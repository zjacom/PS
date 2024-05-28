results = []
vowels = ["a", "e", "i", "o", "u"]

while True:
    pwd = input().strip()
    if pwd == "end":
        break
    
    vowels_flag = False
    for v in vowels:
        if v in pwd:
            vowels_flag = True
            break
    if not vowels_flag:
        results.append(f"<{pwd}> is not acceptable.")
        continue

    continuous_flag = True
    for i in range(1, len(pwd) - 1):
        if pwd[i - 1] in vowels and pwd[i] in vowels and pwd[i + 1] in vowels:
            continuous_flag = False
            break
        elif pwd[i - 1] not in vowels and pwd[i] not in vowels and pwd[i + 1] not in vowels:
            continuous_flag = False
            break
    if not continuous_flag:
        results.append(f"<{pwd}> is not acceptable.")
        continue

    flag = True
    for i in range(len(pwd) - 1):
        if pwd[i] == pwd[i + 1]:
            if pwd[i] != "e" and pwd[i] != "o":
                flag = False
                break
            
    if not flag:
        results.append(f"<{pwd}> is not acceptable.")
        continue

    results.append(f"<{pwd}> is acceptable.")

for res in results:
    print(res)