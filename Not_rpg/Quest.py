import datetime as dt

# Объявите класс Quest с методами и свойствами.
class Quest():

    def __init__(self, name, description, goal, start_time = None, end_time = None) -> None:
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = start_time
        self.end_time = end_time


    def accept_quest():
        if self.end_time != None:
            return "С этим испытанием вы уже справились."
        self.start_time = dt.datetime.now().time().strftime('%H:%M:%S')
        return f"Начало {self.name} положено"


    def pass_quest(start_time):
        if self.start_time == None:
            return "Нельзя завершить то, что не имеет начала!"
        end_time = dt.datetime.now().time().strftime('%H:%M:%S')
        completition_time = end_time - start_time
        return (f"Квест {self.name} окончен. Время выполнения квеста: "
                f"{completition_time}")

   
    def __str__(self) -> str:
        if self.start_time != None and self.end_time == None:
            return f"Цель квеста {self.name} - {self.goal}. Квест выполняется."
        elif self.start_time != None and self.end_time != None:
            return f"Цель квеста {self.name} - {self.goal}. Квест завершен."
        else:
            return f"Цель квеста {self.name} - {self.goal}."


# В этих переменных содержатся значения, которые нужно передать
# в качестве аргументов в экземпляр класса Quest.
quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники'
quest_description = '''
В древнем лесу Кодоборье растут ягоды — пиксельника.
Они нужны для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

# Создайте экземпляр класса Quest.
new_quest = Quest(quest_name, quest_description, quest_goal)
print(new_quest)