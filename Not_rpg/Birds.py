class Bird():
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size


    def describe(self, full = False):
        return f"Размер птицы {self.name} - {self.size}"


class Parrot(Bird):
    def __init__(self, name, size, color) -> None:
        super().__init__(name, size)
        self.color = color
    
    def describe(self, full=False):
        if full == False:
            return super().describe(full)
        else:
            return (f"Попугай {self.name} - заметная птица, окрас её перьев - {self.color}, а размер - {self.size}. "
                    "Интересный факт: попугаи чувствуют ритм, а вовсе не бездумно двигаются под музыку. "
                    "Если сменить композицию, то и темп движений птицы изменится.")
    
    def repeat(phrase):
        return f"Попугай {self.name} говорит: {phrase}."


class Penguin(Bird):
    def __init__(self, name, size, genus) -> None:
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full=False):
        if full == False:
            return super().describe(full)
        else:
            return (f"Размер пингвина {self.name} из рода {self.genus} - {self.size}." 
                    "Интересный факт: однажды группа геологов-разведчиков похитила пингвинье яйцо "
                    "и их принялась преследовать вся стая, не пытаясь, впрочем, при этом нападать. "
                    "Посовещавшись, похитители вернули прицам яйцо, и те отстали.")

    def swimming(self):
        return f"Пингвин {self.name} плавает со средней скоростью 11 км/ч"

kesha = Parrot('Ара', "средний", "Красный")
kowalski = Penguin('Королевский', "большой", "Aptenodutes")