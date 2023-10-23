class Telebot:
    def __init__(self):
        self.state = "ожидание"

    def process_command(self, command):
        if self.state == "ожидание":
            if command == "начать":
                print("Телебот начал выполнение команды.")
                self.state = "выполнение команды"
            else:
                print("Телебот в режиме ожидания. Введите 'начать', чтобы начать выполнение команды.")
        elif self.state == "выполнение команды":
            if command == "завершить":
                print("Телебот завершил выполнение команды.")
                self.state = "ожидание"
            else:
                print(f"Выполняется команда: {command}")

# Пример использования
telebot = Telebot()
telebot.process_command("начать")

# telebot.process_command("Выполнить задачу")
# telebot.process_command("завершить")
print(telebot.state)




if __name__ == "__main__":
    print("start")