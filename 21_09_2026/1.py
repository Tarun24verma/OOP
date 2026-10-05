class credit:
    def __init__(self, name, bankname, __password):
        self.name=name
        self.bankname=bankname
        self.__password=__password

user1=credit('tarun', 'sbi', 111)
print(user1.name)