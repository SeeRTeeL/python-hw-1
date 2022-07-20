# Ініцілізовано функцію, напишіть в тілі функції логіку яка
# перевірить певне число на те чи воно парне або непарне.

# Функція приймає на вхід будь яке число і виводить в консоль строку типу 'Число Х є парним'.
# Наприклад:
#   oddOrEven(1) - > 'Число Х є непарним'
#   oddOrEven(20) - > 'Число Х є парним'
# Можна додавати свої тести за прикладом. Потрібно врахувати обробку можливих помилок.
import sys


def oddOrEven(num):
    try:
        (num % 2) == 0
    except TypeError:
        print('Аргументом має бути число')
        sys.exit()

    if (num % 2) == 0:
        print('Число Х є парним')
    else:
        print('Число Х є непарним')


oddOrEven(1)  # 'Число Х є непарним'
oddOrEven(20)  # 'Число Х є парним'
