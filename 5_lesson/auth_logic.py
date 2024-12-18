from functools import wraps
users = {
    'test': 'qweasdzxc',
    'top1User': 'qweqwe',
    'badMonkey': 'ewqdsazxc',
    'qwe': 'qwe'
}

current_user = None


def auth(func):
    @wraps(func)
    def inner(*args, **kwargs):
        global current_user

        if current_user:
            return func(*args, **kwargs)

        while True:
            login = input("Enter the login: ")
            if login in users and users[login] is not None:
                user_password = users[login]
                break
            else:
                print(f"The user {login} not exist.")
                login = None
        while True:
            password = input("Enter the password: ")
            if password == user_password:
                current_user = (login, password)
                break
            else:
                password = None

        return func(*args, **kwargs)

    return inner


@auth
def command():
    print("I'm bussines logic")


command()
command()
