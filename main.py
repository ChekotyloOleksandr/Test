import time
import random


# Використовую цей алгоритм, бо сортувати весь список заради одного значення є меньш ефективним рішенням
# А median of medians більш довгий(при перевірці)
#Використовував в основному ці 2 ресурси:
#https://en.wikipedia.org/wiki/Quickselect
#https://habr.com/ru/articles/346930/
def partition(digit_list):
    p = random.randint(0, len(digit_list) - 1)
    pivot = digit_list[p]
    left, right = [], []
    for i in range(len(digit_list)):
        if not i == p:
            if digit_list[i] > pivot:
                right.append(digit_list[i])
            else:
                left.append(digit_list[i])
    return left, pivot, right


def select_median(digit_list, k):
    (left, pivot, right) = partition(digit_list)
    if len(left) == k:
        result = pivot
    elif len(left) > k:
        result = select_median(left, k)
    else:
        result = select_median(right, k - len(left) - 1)
    return result


def main():
    start_time = time.time()

    with open('10m.txt', 'r') as file:
        digit_list = [int(line.strip()) for line in file]
    min_digit = max_digit = digit_list[0]
    sum_digits = previous_digit = max_digit
    inc_seq = dec_seq = [max_digit]
    long_inc_seq = long_dec_seq = [max_digit]

    for digit in digit_list[1:]:

        sum_digits += digit
        if min_digit > digit:
            min_digit = digit
        elif max_digit < digit:
            max_digit = digit

        if previous_digit < digit:
            inc_seq += [digit]
            if len(long_dec_seq) < len(dec_seq):
                long_dec_seq = dec_seq
            dec_seq = [digit]
        else:
            dec_seq += [digit]
            if len(long_inc_seq) < len(inc_seq):
                long_inc_seq = inc_seq
            inc_seq = [digit]

        previous_digit = digit

    median = select_median(digit_list, len(digit_list) // 2)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f'Максимальне число в файлі : {max_digit}')
    print(f'Мінімальне число в файлі : {min_digit}')
    print(f'Середнє арифметичне значення в файлі : {sum_digits / len(digit_list)}')
    print(f'Медіана в файлі : {median}')
    print(f'Найбільша послідовність чисел, яка збільшується : {long_inc_seq}.\nЇї довжина {len(long_inc_seq)}')
    print(f'Найбільша послідовність чисел, яка зменьшуется : {long_dec_seq}.\nЇї довжина {len(long_dec_seq)}')
    print("Час виконання:", execution_time, "секунд")


if __name__ == '__main__':
    main()
