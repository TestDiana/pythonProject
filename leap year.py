С = int(input())
if (С % 4 == 0) and (С % 100 != 0):
    print("Високосный")
elif С % 400 == 0:
    print("Високосный")
else:
    print("Обычный")
