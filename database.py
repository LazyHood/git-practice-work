class DatabaseManager:
    def __init__(self):
        self.connection = None
    
    def connect(self):
        print('Подключение к БД')
