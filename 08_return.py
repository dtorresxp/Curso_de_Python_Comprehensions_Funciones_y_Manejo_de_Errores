def sum_with_range(min,max):
    print(min, max)
    sum = 0
    for x in range(min,max):
        sum += x

    return sum

result = sum_with_range(1,10)
print(result)
result_2 = sum_with_range(20,30)
print(result_2)
result_3 = sum_with_range(result,result_2)
print(result_3)