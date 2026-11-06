class Title():
    #конструктор
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y =y_num
        self.appearence = True
    #методы
    def hide(self):
        self.appearence = False
        print("скрыли")
    def show(self):
        self.appearence = True
        print("проявили")  
    def print_info (self):
        print("Кнопка:", self.title)
        print("Расположение:","(",self.x,",",self.y,")")
        print("Видимость:", self.appearence)

#создай две надписи
Prorab=Title("Узнать победителя прямо сейчас!", "150", "50")
Prorok=Title("Победитель может быть только один", "150", "-100")
Prorab.print_info()
Prorok.print_info()
#скрой вторую надпись
Prorok.hide()