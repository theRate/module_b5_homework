field = {'a1': '-', 'b1': '-', 'c1': '-',
         'a2': '-', 'b2': '-', 'c2': '-',
         'a3': '-', 'b3': '-', 'c3': '-'}


def print_field():
    print(f'   a  b  c')
    print(f'1 [{field.get("a1")}][{field.get("b1")}][{field.get("c1")}]')
    print(f'2 [{field.get("a2")}][{field.get("b2")}][{field.get("c2")}]')
    print(f'3 [{field.get("a3")}][{field.get("b3")}][{field.get("c3")}]')


def take_input(user):
    valid = False
    while not valid:
        decision = str(input(f'Куда поставим {user}? ').lower())
        letter = False
        digit = False

        for i in decision:
            if i in 'abc':
                letter = i
            if i in '123':
                digit = i

        if letter and digit:
            coordinate = letter + digit
            if field.get(coordinate) not in 'XO':
                field[coordinate] = user
                print(f'Ваш ход {letter}-{digit} принят')
                # print_field()
                valid = True
            else:
                print('Клетка уже занята, нужен другой ход')
        else:
            print('Некорректный ввод хода')


def check_win(map, user):
    def check_line(a, b, c, user):
        if map.get(a) == user and map.get(b) == user and map.get(c) == user:
            return True

    if check_line('a1', 'b1', 'c1', user) or \
            check_line('a2', 'b2', 'c2', user) or \
            check_line('a3', 'b3', 'c3', user) or \
            check_line('a1', 'a2', 'a3', user) or \
            check_line('b1', 'b2', 'b3', user) or \
            check_line('c1', 'c2', 'c3', user) or \
            check_line('a1', 'b2', 'c3', user) or \
            check_line('a3', 'b2', 'c1', user):
        return True

    return False


count = 0
while True:
    if count % 2 == 0:
        player = 'X'
    else:
        player = 'O'

    print_field()
    take_input(player)
    if check_win(field, player):
        print(f'Победили {player * 3}-ки')
        break
    count += 1
    if count >= 9:
        print_field()
        print('Ничья. Победила дружба')
        break
