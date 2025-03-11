# case-study #2
# Developers: Limanova E., Ponasenko K.

import ru_local as ru


def main():
    '''
    Main function.
    :return: None
    '''

    quantity_x = int(input(ru.QUANTITY_X))
    quantity_y = int(input(ru.QUANTITY_Y))
    price_x = int(input(ru.PRICE_X))

    if ((4 * quantity_x - quantity_y) <
            (2 * quantity_x + quantity_y)):
        mrs = abs(4 / (-1))
    else:
        mrs = abs(2 / 1)

    price_y = price_x / mrs
    income = (price_x * quantity_x +
              price_y * quantity_y)
    incline = -(price_x / price_y)

    print(f'{ru.PRICE_Y} — {price_y} {ru.MEASURE}')
    print(f'{ru.INCOME} {income} {ru.MEASURE}')
    print(f'{ru.INCLINE} ({quantity_x}, {quantity_y}) — {incline}')


if __name__ == '__main__':
    main()
