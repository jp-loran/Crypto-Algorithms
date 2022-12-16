import crypto_algorithms as crypto
import performance as pf
import json
from tkinter import * #PhotoImage, Tk_
from tkinter import messagebox #PhotoImage, Tk_
from tkinter import ttk
from gui.widgets import ButtonStart, FrameStudentData, LabelLogo, LabelStudentData
from PIL import Image, ImageTk

#TEST VECTOR
default_key = b'?D(G+KbPdSgVkYp3s6v9y$B&E)H@McQf' #256 bits  
default_plaintext = b'Attack at dawn'



#Se crea ventana principal.
window = Tk()

def run_algorithm(selection, key=default_key, plaintext=default_plaintext):
  if(selection == "Algoritmos Simétricos"):
    result_chacha= json.loads(pf.measure(crypto.chacha20, key, plaintext))
    result_aes_ebc= json.loads(pf.measure(crypto.aes_ebc, key, plaintext))
    result_aes_cbc= json.loads(pf.measure(crypto.aes_cbc, key, plaintext))
    return [result_chacha, result_aes_ebc, result_aes_cbc]
  elif(selection == "Algoritmos Hash"):
    result_sha_384= json.loads(pf.measure(crypto.sha_384, plaintext))
    result_sha_512= json.loads(pf.measure(crypto.sha_512, plaintext))
    result_sha3_384= json.loads(pf.measure(crypto.sha3_384, plaintext))
    result_sha3_512= json.loads(pf.measure(crypto.sha3_512, plaintext))
    return [result_sha_384, result_sha_512, result_sha3_384, result_sha3_512]
  elif(selection == "Algoritmos Asimétricos"):
    print("")

  
def place_algorithm_info(window, combo, key, vector):
  selection = combo.get()
  vector = vector.get().encode('utf8')
  key = key.get().encode('utf8') 

  if(selection == "Algoritmos Simétricos"):

    if(vector == b'' or key == b''):
      result = run_algorithm(selection)
    else:
      result = run_algorithm(selection,key,vector)


    Label(window, text="CHACHA20", font = ('Helvetica', 10, 'bold')).place(x=40, y=140)
    Label(window, text="Resultado: "+ result[0]['result']).place(x=40, y=160)
    Label(window, text="Tiempo de ejecución: "+ str("%.5f" % result[0]['time'])+ " segundos").place(x=40, y=180)
    Label(window, text="Memoria utilizada: "+ str(result[0]['current_memory'])+ " bytes").place(x=40, y=200)
    Label(window, text="Máximo pico de memoria: "+ str(result[0]['peak_memory'])+ " bytes").place(x=40, y=220)

    Label(window, text="AES-EBC", font = ('Helvetica', 10, 'bold')).place(x=40, y=260)
    Label(window, text="Resultado: "+ result[1]['result']).place(x=40, y=280)
    Label(window, text="Tiempo de ejecución: "+ str("%.5f" % result[1]['time'])+ " segundos").place(x=40, y=300)
    Label(window, text="Memoria utilizada: "+ str(result[1]['current_memory'])+ " bytes").place(x=40, y=320)
    Label(window, text="Máximo pico de memoria: "+ str(result[1]['peak_memory'])+ " bytes").place(x=40, y=340)

    Label(window, text="AES-CBC", font = ('Helvetica', 10, 'bold')).place(x=40, y=380)
    Label(window, text="Resultado: "+ result[2]['result']).place(x=40, y=400)
    Label(window, text="Tiempo de ejecución: "+ str("%.5f" % result[2]['time'])+ " segundos").place(x=40, y=420)
    Label(window, text="Memoria utilizada: "+ str(result[2]['current_memory'])+ " bytes").place(x=40, y=440)
    Label(window, text="Máximo pico de memoria: "+ str(result[2]['peak_memory'])+ " bytes").place(x=40, y=460)


  elif(selection == "Algoritmos Hash"):

    if(vector == b''):
      result = run_algorithm(selection)
    else:
      result = run_algorithm(selection,None,vector)

    Label(window, text="SHA 384", font = ('Helvetica', 10, 'bold')).place(x=40, y=140)
    Label(window, text="Resultado: "+ result[0]['result']).place(x=40, y=160)
    Label(window, text="Tiempo de ejecución: "+ str("%.5f" % result[0]['time'])+ " segundos").place(x=40, y=180)
    Label(window, text="Memoria utilizada: "+ str(result[0]['current_memory'])+ " bytes").place(x=40, y=200)
    Label(window, text="Máximo pico de memoria: "+ str(result[0]['peak_memory'])+ " bytes").place(x=40, y=220)

    Label(window, text="SHA 512", font = ('Helvetica', 10, 'bold')).place(x=40, y=260)
    Label(window, text="Resultado: "+ result[1]['result']).place(x=40, y=280)
    Label(window, text="Tiempo de ejecución: "+ str("%.5f" % result[1]['time'])+ " segundos").place(x=40, y=300)
    Label(window, text="Memoria utilizada: "+ str(result[1]['current_memory'])+ " bytes").place(x=40, y=320)
    Label(window, text="Máximo pico de memoria: "+ str(result[1]['peak_memory'])+ " bytes").place(x=40, y=340)

    Label(window, text="SHA3 384", font = ('Helvetica', 10, 'bold')).place(x=40, y=380)
    Label(window, text="Resultado: "+ result[2]['result']).place(x=40, y=400)
    Label(window, text="Tiempo de ejecución: "+ str("%.5f" % result[2]['time'])+ " segundos").place(x=40, y=420)
    Label(window, text="Memoria utilizada: "+ str(result[2]['current_memory'])+ " bytes").place(x=40, y=440)
    Label(window, text="Máximo pico de memoria: "+ str(result[2]['peak_memory'])+ " bytes").place(x=40, y=460)

    Label(window, text="SHA3 512", font = ('Helvetica', 10, 'bold')).place(x=40, y=500)
    Label(window, text="Resultado: "+ result[3]['result']).place(x=40, y=520)
    Label(window, text="Tiempo de ejecución: "+ str("%.5f" % result[3]['time'])+ " segundos").place(x=40, y=540)
    Label(window, text="Memoria utilizada: "+ str(result[3]['current_memory'])+ " bytes").place(x=40, y=560)
    Label(window, text="Máximo pico de memoria: "+ str(result[3]['peak_memory'])+ " bytes").place(x=40, y=580)

  elif(selection == "Algoritmos Asimétricos"):
    print("")
  

def show_instructions():
  data=""" 
  1. Select the algorithm family you want to test
  2. For symmetric algorithms yo must type a vector to encrypt and a 256-bit key (32 characters) 
  3. For hash algorithms there is no need to type any kind  of key 
  4. Once you have filled the necessary fields, you can press the enter button
  5. In case you leave any field empty, the program will take as input the default information decided by the developers

  Default vector: Attack at dawn 
  Default key: ?D(G+KbPdSgVkYp3s6v9y$B&E)H@McQf 
  """

  messagebox.showinfo(message=data, title='Instructions')

def open_algorithms():
  window.destroy()
  newWindow=Tk()
  newWindow.title("Algoritmos Criptográficos")
  newWindow.geometry('950x650')
  Label(newWindow, text="Seleccione la familia de algoritmos que desee comparar").place(x=40, y=50)

  Label(newWindow, text="Comparación de algoritmos", font = ('Helvetica', 13, 'bold')).place(x=250, y=10)

  algorithms= ttk.Combobox(
    state="readonly",
    values=["Algoritmos Simétricos","Algoritmos Hash","Algoritmos Asimétricos"]
  )
  algorithms.place(x=40, y=80)
  
  Label(newWindow, text="Vector = ").place(x=200, y=80)
  vectorField= Entry(newWindow)
  vectorField.place(x=250, y=80)

  Label(newWindow, text="Llave = ").place(x=390, y=80)
  keyField= Entry(newWindow)
  keyField.place(x=440, y=80)

  enterButton = ttk.Button(text="ENTER", command=lambda: place_algorithm_info(newWindow, algorithms,  keyField,vectorField))
  enterButton.place(x=37, y=110)

  instButton = ttk.Button(text="INSTRUCTIONS", command=show_instructions)
  instButton.place(x=125, y=110)




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
LabelStudentData(frame_sd, 'ALVAREZ LORAN JUAN PABLO', 12, 185, 355)
LabelStudentData(frame_sd, 'PALACIOS DIEGO OCTAVIO', 12, 185, 390)
LabelStudentData(frame_sd, 'REYES GONZÁLEZ AGUSTÍN ÓSCAR', 12, 183, 425)
photo = PhotoImage(file = './gui/images/key_start.png')
photoimage = photo.subsample(3, 3)
ButtonStart(frame_sd, 'Iniciar', open_algorithms, photoimage, 285, 500)

window.mainloop()

