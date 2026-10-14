def my_sum(arr: list[float | int]) -> float | int:
    s=0
    for n in arr:
        s+=n
    return s
print(my_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def my_avg(arr: list[float | int]) -> float | int:
    a=0
    s=0
    for n in arr:
        s+=n
        a+=1
    if a==0:
        return 0
    return s/a
print(my_avg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def my_min(arr: list[float | int]) -> float | int:
    if not arr:
        return None
    m = arr[0]
    for i in arr:
        if i < m:
            m = i
    return m
print(my_min([1, 2, 3, 4, 5]))


def my_max(arr: list[float | int]) -> float | int:
    if not arr:
        return None
    m = arr[0]
    for i in arr:
        if i > m:
            m = i
    return m
print(my_max([1, 2, 3, 4, 5])) 


def my_max_filter(arr: list[float | int], num: float | int) -> list[float | int]:
    result = []
    for i in arr:
        if i > num:
            result.append(i)
    return result
print(my_max_filter([1, 2, 3, 4, 5], 1))    


def my_len(arr: list[float | int]) -> int:
    count = 0
    for i in arr:
        count += 1
    return count
print(my_len([1, 2, 3, 4, 5]))       



