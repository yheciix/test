from lesson_package.tool import utils


def sing():
    return utils.say_twice('wowwow')


def cry():
    return 'bowbow'


if __name__ == '__main__':
    print(sing())
    print(cry())