def first_task(first_number,second_number):
    summ = 0
    for i in range(first_number+1,second_number):
        summ += i
    return summ


print(first_task(1,5))


def second_task(fist_number,second_number):
    summ = 0
    for i in range(fist_number,second_number+1):
        if i % 2 == 0:
            summ += i
    return summ


print(second_task(1,100))


def third_task(string):
    for i in string:
        print(i)


third_task('abcd')


def fourth_task(numbers_list):
    new_list = []
    if isinstance(numbers_list, list):
        for i in numbers_list:
            if isinstance(i, int) and i % 2 == 0:
                new_list.append(i)
        return new_list
    else:
        return 0


test_list_1 = [1,2,3,4,5,6,7,8,9,10]


print(fourth_task(test_list_1))


def fifth_task(str_list):
    new_list = []
    if isinstance(str_list,list):
        for i in str_list:
            if isinstance(i,str):
                if i[0].isupper():
                    new_list.append(i)

        return new_list

    else: return 0


test_list_2 = ['abd','Avc','fff','fFf','FFF']

print(fifth_task(test_list_2))


def sixth_task(str_list):
    new_list = []
    if isinstance(str_list,list):
        for i in str_list:
            if isinstance(i, str) and 'Python ' in i:
                new_list.append(i)
        return new_list
    else: return 0

test_list_3 = ['py','pit','python here','Python but uppercase','Pythonn','1 Python 2']
print(sixth_task(test_list_3))


