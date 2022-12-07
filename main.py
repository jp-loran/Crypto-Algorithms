from Crypto.Random import get_random_bytes
import crypto_algorithms as crypto
import performance as pf
import json
from tkinter import PhotoImage, Tk
from gui.widgets import ButtonStart, FrameStudentData, LabelLogo, LabelStudentData
from PIL import Image, ImageTk

#TEST VECTOR
key = get_random_bytes(32) #256 bits  
plaintext = b'Attack at dawn'

result=json.loads(pf.measure(crypto.chacha20, plaintext, key))
print(result)

#Se crea ventana principal.
window = Tk()
window.title('Criptografía')
window.geometry('700x570+300+100')
window.resizable(False, False)
frame_sd = FrameStudentData(window)
imagen = ImageTk.PhotoImage(Image.open('./gui/images/fi.png'))
LabelLogo(frame_sd, imagen)
LabelStudentData(frame_sd, 'UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO', 14, 89, 175)
LabelStudentData(frame_sd, 'FACULTAD DE INGENIERÍA', 14, 206, 205)
LabelStudentData(frame_sd, 'CRIPTOGRAFÍA', 14, 265, 235)
LabelStudentData(frame_sd, 'PROYECTO FINAL', 14, 255, 265)
LabelStudentData(frame_sd, 'INTEGRANTES', 14, 270, 315)
LabelStudentData(frame_sd, 'REYES GONZÁLEZ AGUSTÍN ÓSCAR', 12, 185, 355)
LabelStudentData(frame_sd, 'REYES GONZÁLEZ AGUSTÍN ÓSCAR', 12, 185, 390)
LabelStudentData(frame_sd, 'REYES GONZÁLEZ AGUSTÍN ÓSCAR', 12, 183, 425)
photo = PhotoImage(file = './gui/images/key_start.png')
photoimage = photo.subsample(3, 3)
ButtonStart(frame_sd, 'Iniciar', None, photoimage, 285, 500)

window.mainloop()