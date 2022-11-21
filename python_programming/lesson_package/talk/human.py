from lesson_package.tool import utils


def sing():
    return utils.say_twice('sing')


def cry():
    return 'cry'


if __name__ == '__main__':
    print(sing())
    print(cry())



