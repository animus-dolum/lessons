hours = sorted(input().split(), key=int)
especially_happy_minutes = input().split()

sorted_hours = sorted(map(int, hours))
sorted_strings = sorted(especially_happy_minutes, key=int)

for i in sorted_hours:
    if len(str(i)) == 1:
        for m in sorted_strings:
            sum_i = sum(int(digit) for digit in str(i))
            sum_m = sum(int(digit) for digit in str(m))

            if sum_i != sum_m:
                if len(str(m)) == 1:
                    print(*{f"0{i}:0{m}"})
                else:
                    print(*{f"0{i}:{m}"})
    else:
        for k in sorted_strings:
            sum_i = sum(int(digit) for digit in str(i))
            sum_m = sum(int(digit) for digit in str(k))

            if sum_i != sum_m:
                if len(str(k)) == 1:
                    print(*{f"{i}:0{k}"})
                else:
                    print(*{f"{i}:{k}"})
