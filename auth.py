with open('auth.txt', encoding='utf-8') as file:
    email, password, name = map(lambda x: x.split()[-1], file.readlines())