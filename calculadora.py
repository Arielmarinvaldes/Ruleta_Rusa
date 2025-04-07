import math
from tkinter import *

main_window = Tk()
main_window.title("Calculator")
main_window.geometry("290x380")
main_window.resizable(0, 0)
main_window.configure(bg='#FF9EA0')
main_window.eval(f'tk::PlaceWindow {str(main_window)} center')
Label_title = Label(main_window, text="Calculadora", bg="#FF9EA0", fg="#2c3e50", font=('Arial', 12, 'bold'))
Label_title.pack(pady=10)

canvas_result = Text(main_window, bg="#C3C8D3", height=3, width=34)
canvas_result.place(x=8, y=50)


def calcular():
    expression = canvas_result.get("1.0", END)
    try:
        result = eval(expression)
        clear_canvas()
        canvas_result.insert(END, str(result))
    except:
        clear_canvas()
        canvas_result.insert(END, "Error")


def sair():
    main_window.destroy()


def limpar():
    canvas_result.delete("1.0", END)


def clear_canvas():
    canvas_result.delete("1.0", END)


def raiz():
    try:
        resultado = math.sqrt(float(canvas_result.get("1.0", END)))
        clear_canvas()
        canvas_result.insert(END, str(resultado))
    except:
        clear_canvas()
        canvas_result.insert(END, "No hay raiz cuadrada para este número")



def porcentaje():
    try:
        resultado = float(canvas_result.get("1.0", END))
        clear_canvas()
        canvas_result.insert(END, str(resultado))
        canvas_result.insert(END, "%")
    except:
        clear_canvas()
        canvas_result.insert(END, "No hay porcentaje para este número")


btn_2 = Button(main_window, text="2", command=lambda: canvas_result.insert(END, "2"), width=5, height=2, relief="flat")
btn_3 = Button(main_window, text="3", command=lambda: canvas_result.insert(END, "3"), width=5, height=2, relief="flat")
btn_4 = Button(main_window, text="4", command=lambda: canvas_result.insert(END, "4"), width=5, height=2, relief="flat")
btn_5 = Button(main_window, text="5", command=lambda: canvas_result.insert(END, "5"), width=5, height=2, relief="flat")
btn_6 = Button(main_window, text="6", command=lambda: canvas_result.insert(END, "6"), width=5, height=2, relief="flat")
btn_1 = Button(main_window, text="1", command=lambda: canvas_result.insert(END, "1"), width=5, height=2, relief="flat")
btn_7 = Button(main_window, text="7", command=lambda: canvas_result.insert(END, "7"), width=5, height=2, relief="flat")
btn_8 = Button(main_window, text="8", command=lambda: canvas_result.insert(END, "8"), width=5, height=2, relief="flat")
btn_9 = Button(main_window, text="9", command=lambda: canvas_result.insert(END, "9"), width=5, height=2, relief="flat")
btn_0 = Button(main_window, text="0", command=lambda: canvas_result.insert(END, "0"), width=5, height=2, relief="flat")
btn_00 = Button(main_window, text="00", command=lambda: canvas_result.insert(END, "00"), width=5, height=2, relief="flat")
btn_decimal = Button(main_window, text=".", command=lambda: canvas_result.insert(END, "."), width=5, height=2)
btn_suma = Button(main_window, text="+", command=lambda: canvas_result.insert(END, "+"), width=5, height=2)
btn_resta = Button(main_window, text="-", command=lambda: canvas_result.insert(END, "-"), width=5, height=2)
btn_multiplicacion = Button(main_window, text="x", command=lambda: canvas_result.insert(END, "*"), width=5, height=2)
btn_division = Button(main_window, text="/", command=lambda: canvas_result.insert(END, "/"), width=5, height=2)
btn_pi = Button(main_window, text="π", command=lambda: canvas_result.insert(END, math.pi), width=5, height=2)
btn_borrar = Button(main_window, text="←", fg="#FF6666", command=lambda: canvas_result.delete("end-2c", "end-1c"), width=5, height=2, font=('Arial', 9, 'bold'))
btn_igual = Button(main_window, text="=", command=calcular, width=5, relief="flat", height=2, bg="#7D7DFF")
btn_limpiar = Button(main_window, text="C", command=limpar, width=5, height=2)
btn_raiz = Button(main_window, text="√", command=raiz, width=5, height=2)
btn_porcentaje = Button(main_window, text="%", command=porcentaje, width=5, height=2)
btn_salir = Button(main_window, text="Salir", command=sair, width=5, height=2, bg="#FF6666")

btn_2.place(x=120, y=160)
btn_3.place(x=170, y=160)
btn_1.place(x=70, y=160)
btn_4.place(x=70, y=210)
btn_5.place(x=120, y=210)
btn_6.place(x=170, y=210)
btn_7.place(x=70, y=260)
btn_8.place(x=120, y=260)
btn_9.place(x=170, y=260)
btn_0.place(x=120, y=310)
btn_00.place(x=70, y=310)
btn_decimal.place(x=170, y=310)
btn_suma.place(x=220, y=260)
btn_resta.place(x=220, y=210)
btn_multiplicacion.place(x=220, y=160)
btn_division.place(x=220, y=110)
btn_borrar.place(x=170, y=110)
btn_igual.place(x=220, y=310)
btn_limpiar.place(x=20, y=110)
btn_raiz.place(x=120, y=110)
btn_porcentaje.place(x=70, y=110)
btn_salir.place(x=20, y=310)
btn_pi.place(x=20, y=260)
main_window.mainloop()
