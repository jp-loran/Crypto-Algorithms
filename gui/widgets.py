from tkinter import Frame, Label



'''FRAMES'''

#Frame para las opciones de selección de algoritmo critográfico.
class FrameStudentData(Frame):
    def __init__(self, master):
        super().__init__(
            master,
            width = 699,
            height = 549,
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
            fg = 'red3',
            bg = 'gray90'
        )
        self.place(x=posx, y=posy)