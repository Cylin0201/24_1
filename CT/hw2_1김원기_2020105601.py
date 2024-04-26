data = [35, 48, 3, 4, 50, 43, 7, 19, 9, 23,
15, 13, 11, 37, 12, 18, 25, 16, 8, 20,
27, 22, 10, 24, 17, 38, 29, 46, 21, 30,
40, 32, 44, 33, 1, 36, 14, 26, 39, 31,
31, 42, 6, 31, 45, 28, 47, 2, 49, 5]

#(1) 최대값과 그 위치(인덱스, 0..49)를 출력한다.
max_value = data[0]
max_index = 0
for i in range(1, len(data)):
    if (max_value < data[i]):
        max_value, max_index = data[i], i
print("최대값은 {0} 그 위치는 {1}".format(max_value, max_index))
    

#(2) 짝수의 개수를 출력한다.
cnt_even = 0
for i in range(len(data)):
    if not (data[i] % 2):
        cnt_even += 1
print("짝수의 갯수는", cnt_even)

#(3) 3의 배수가 되는 숫자들의 개수를 출력한다.
cnt_3 = 0
for i in range(len(data)):
    if not (data[i] % 3):
        cnt_3 += 1
print("3의 배수의 갯수는", cnt_3)