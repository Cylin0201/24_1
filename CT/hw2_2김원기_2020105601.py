data = [16, 10, 20, 13, 29, 22, 44, 3, 6, 100, 
27, 92, 67, 85, 21, 65, 72, 52, 67, 98, 
18, 58, 8, 98, 5, 22, 9, 50, 85, 99, 
29, 12, 1, 80, 29, 58, 84, 77, 75, 27, 
71, 19, 50, 9, 66, 84, 62, 99, 91, 23, 
36, 28, 71, 81, 89, 78, 76, 57, 63, 48, 
73, 97, 19, 89, 69, 61, 20, 57, 94, 4, 
43, 30, 91, 86, 16, 3, 41, 36, 8, 86, 
32, 38, 1, 49, 11, 1, 59, 83, 3, 82, 
92, 60, 60, 7, 68, 99, 68, 35, 32, 44]

max_window = [data[i] for i in range(10)]
max_sum = sum(max_window)
max_data = max_window.copy()

for s_cursor in range(1, len(data) - 9):
    max_window = [data[i + s_cursor] for i in range(10)]
    if max_sum < sum(max_window):
        max_sum = sum(max_window)
        max_data = max_window

print("(1) 최대 합과 데이터 구하기")
print("최대 합은 ", max_sum)  
print("최대 합의 데이터는 ", max_data)

min_window = [data[i] for i in range(10)]
min_sum = sum(min_window)
min_data = min_window.copy()

for s_cursor in range(1, len(data) - 9):
    min_window = [data[i + s_cursor] for i in range(10)]
    if min_sum > sum(min_window):
        min_sum = sum(min_window)
        min_data = min_window

print("(2) 최소 합과 데이터 구하기")
print("최소 합은 ", min_sum)  
print("최소 합의 데이터는 ", min_data)
