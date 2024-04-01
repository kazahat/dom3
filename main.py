class User:
    def __init__(self, id, name, level):
        self.__id = id
        self.name = name
        self.level = level

        self.users = []

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id


class Admin(User):
    def __init__(self, id, name, level):
        super().__init__(id, name, 'admin')

    def add_user(self, id, name, level):
        self.users.append({'id': id, 'name': name, 'level': level})

    def remove_user(self, id):
        for user in self.users:
            if user['id'] == id:
                self.users.remove(user)

    def print_user(self):
        for user in self.users:
            print(f"Сотрудник:{user['id']} Имя:{user['name']} Уровень:{user['level']}")






a = Admin(0, 'Артем', 'admin')
a.add_user(1, 'Иван','user')
a.add_user(2, 'Петр','user')
a.add_user(3, 'Сидор','user')

a.print_user()
a.remove_user(2)
a.print_user()
a.set_id(3)
print(a.get_id())







