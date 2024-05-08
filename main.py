class Server:
    def __init__(self):
        self.users = {}

    def AddUser(self, name, password):
        self.users[name] = password

    def __delitem__(self, key):
        del self.users[key]


if __name__ == "__main__":
    server = Server()
    server.AddUser("Vasya", "0110")
    server.AddUser("Petya", "012345678")
    server.AddUser("Kirill", "18273146")
    del server["Petya"]
    print(server.users)