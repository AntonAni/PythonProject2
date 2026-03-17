first_variable = int(input('a = ', ))    # запрашиваем первый коэффициент
second_variable = int(input('b = ', ))    # запрашиваем второй коэффициент
third_variable = int(input('c = ',))    # запрашиваем третий коэффициент

# решение по сокращенной формуле, т.к. b - четное
if first_variable!= 0 and second_variable % 2 == 0 and third_variable!= 0:
    k = second_variable / 2
    d1 = k ** 2 - first_variable * third_variable
    root_1 = (-k + d1 ** 0.5) / first_variable
    root_2 = (-k - d1 ** 0.5) / first_variable

    print('так как коэффициент b - четное число, решаем по сокращенной формуле')
    print(f'Первый корень = {root_1}')
    print(f'Второй корень = {root_2}')


# решение уравнения при с = 0
if first_variable != 0 and third_variable== 0 and second_variable != 0:
    print(f'корень уравнения равен либо нулю, либо {-second_variable / first_variable}')


# решение уравнения при b = 0 и c = 0
if first_variable != 0 and second_variable== 0 and third_variable == 0:
    print(f'корни уравнения равны нулю, first_variable * x ** 2 = 0')


# решение полного уравнения
if first_variable != 0 and second_variable % 2 != 0 and third_variable != 0:
    d = second_variable ** 2 - 4 * first_variable * third_variable
    if d > 0:
        root_1 = (-second_variable + d ** 0.5) / (2 * first_variable)
        print(f'Дискриминант равен: {d}')
        print(f'Первый корень равен: {round(root_1, 2)}')
        root_2 = (-second_variable - d ** 0.5) / (2 * first_variable)
        print(f'Второй корень равен: {round(root_2, 2)}')
    elif d < 0:
        print(f'так как дискриминант меньше нуля и равен: {d}')
        print('действительных корней нет') 
    else:
        k = -second_variable / (2 * first_variable)
        print(f'уравнение имеет один корень: {k}')
        if first_variable != 0 and third_variable != 0 and second_variable == 0:

        # решение уравнения при b = 0
            if (- third_variable / first_variable) >= 0:
                root_1 = ( -third_variable / first_variable ) ** 0.5
                print(f'первый корень равен: {root_1}')
                root_2 = (-1) * (( -third_variable / first_variable ) ** 0.5)
                print(f'второй корень равен: {root_2}')
        if ( - third_variable / first_variable ) < 0:
            print(f' -third_variable / first_variable = : {-third_variable / first_variable}, '
                  f'т.е. < 0, поэтому действительных корней нет')
