class User:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._level = 'user'

        self.users = []

    def get_id(self):
        return self._id
    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_level(self):
        return self._level
    def set_level(self, level):
        self._level = level


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._level = 'admin'


    def add_user(self, user_list, user,):
        user_list.append(user)
        print(f"Пользователь  добавлен")
        print(user_list)

    def remove_user(self, user_list, user):
        user_list.remove(user)



users = []
admin = Admin(1, 'Vasya')
user1 = User(1, 'Petya')


print(user1.get_name())
admin.add_user(users, user1)




