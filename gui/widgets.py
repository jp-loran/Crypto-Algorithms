from tkinter import LEFT, Button, Frame, Label


'''BUTTONS'''

class ButtonStart(Button):
    def __init__(self, master, text, event, image, posx, posy):
        super().__init__(
            master,
            text = text,
            command = event,
            cursor = 'hand2',
            width = 100,
            relief = 'groove',
            bd = 1,
            bg='steel blue',
            fg = 'white',
            font = ('verdana', 12, 'bold'),
            activeforeground = 'white',
            activebackground = 'gray50',
            image = image, 
            compound = LEFT
        )
        self.place(x=posx, y=posy)
        self.cambiar_boton(self, 'gray90', 'white')
    
    #Función para cambiar las propiedades de los botones.
    def cambiar_boton(self, boton, colorletra, colorLetra2):
        boton.bind('<Enter>', func = lambda e: boton.config(foreground=colorletra))
        boton.bind('<Leave>', func = lambda e: boton.config(foreground=colorLetra2))



'''FRAMES'''

#Frame para las opciones de selección de algoritmo critográfico.
class FrameStudentData(Frame):
    def __init__(self, master):
        super().__init__(
            master,
            width = 699,
            height = 569,
            relief = 'groove',
            bd = 1,
            bg='gray90',
            )
        self.place(x=0, y=0)

'''LABELS'''

class LabelStudentData(Label):
    def __init__(self, master, text, fontsize, posx, posy):
        super().__init__(
            master = master,
            text = text,
            font = ('Verdana', fontsize, 'bold'),
            fg = 'black',
            bg = 'gray90'
        )
        self.place(x=posx, y=posy)

#Label para logo de Santander del menú principal.
class LabelLogo(Label):
    def __init__(self, padre, imagen):
        super().__init__(
                padre,
                image = imagen,
                relief = 'groove',
                bd = 0,
                bg = 'gray90'
            )
        self.place(x=285, y=10)