from Crypto.Random import get_random_bytes
import crypto_algorithms as crypto
import performance as pf
import json
from tkinter import Tk
from gui.widgets import FrameStudentData, LabelStudentData

#TEST VECTOR
key = get_random_bytes(32) #256 bits  
plaintext = b'Attack at dawn'

result=json.loads(pf.measure(crypto.chacha20, plaintext, key))
print(result)

#Se crea ventana principal.
window = Tk()
window.title('Criptografía')
window.geometry('700x550+300+100')
window.resizable(False, False)
frame_sd = FrameStudentData(window)
label_sd1 = LabelStudentData(frame_sd, 'UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO', 16, 55, 10)
label_sd2 = LabelStudentData(frame_sd, 'FACULTAD DE INGENIERÍA', 16, 190, 40)
label_sd3 = LabelStudentData(frame_sd, 'CRIPTOGRAFÍA', 16, 255, 70)
window.mainloop()