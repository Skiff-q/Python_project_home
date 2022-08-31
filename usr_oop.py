

class User:
    count = 0

    def __init__(self, name, login, password):
        self._name = name
        self._login = login
        self._password = password
        if self.__class__ == User:
            User.count += 1

    def show_info(self):
        return f'name: {self._name}, login: {self._login}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        print('Cannot be changed')

    @property
    def password(self):
        prt = "Can't watch"
        return prt

    @password.setter
    def password(self, value):
        if len(value) >= 5:
            self._password = value
        else:
            print('Short password')


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self._role = role
        if self.__class__ == SuperUser:
            SuperUser.count += 1

    def show_info(self):
        return super().show_info() + f', role: {self._role}'

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value


user1 = User(name='Alex', login='alexis', password='12345')
user2 = User(name='Georgex', login='georg', password='aa12345')
user3 = User(name='Richard', login='rich', password='1EE@2345')
admin = SuperUser(name='John', login='jonny', password='12dfa45', role='admin')

print()