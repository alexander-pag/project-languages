from tkinter import font, ttk
from tkinter import *
from PrepareProduction import *
#from Colors import *
from AnalyzerLL1 import *
#import os

#os.system("")


class Interface:
    def __init__(self, gui):
        self.window = gui
        self.window.title("Analyzer LL1 with Python v1.0")


        # =========== Ver gramatica inicial sin aplicar recursion izquierda ============
        def Gramatica1():
            self.productions = [["S", "S + P"], ["S", "P int"],
                                ["P", "P * C"], ["P", "¿ K ?"],
                                ["K", "K amd"], ["K", "( C )"],
                                ["T", "len P"], ["T", "from T P"],
                                ["C", "C id"], ["C", "5.0"], ["C", "asus"]]
            """
            S-> S + P | P int
            P-> P * C | ¿ K ?
            K-> K amd | ( C )
            T-> len P | from T P
            C-> C id | 5.0 | asus
            """
            self.noTerminals = ["S", "P", "K", "T", "C"]

            self.initial = "S"

            s = ttk.Style()
            s.theme_use('clam')

            # Configura los estilos de la cabecera de la tabla
            s.configure('Treeview.Heading', background="#ff6961")

            tree = ttk.Treeview(frame, column=("c1", "c2"),
                                show='headings', height=15)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="No Terminal")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Produccion")
            for item in self.productions:
                tree.insert('', "end", text="1", values=(item[0], [item[1]]))
            tree.place(x=0, y=5)


        # =========== Realizar recursion izquierda a la gramatica ============
        def RecursionGramatica1():
            self.result = PrepareProduction.DeleteRecursionLeft(
                PrepareProduction(self.noTerminals, self.initial, self.productions))
            s = ttk.Style()
            s.theme_use('clam')

            # Configura los estilos de la cabecera de la tabla
            s.configure('Treeview.Heading', background="#77dd77")

            tree = ttk.Treeview(frame, column=("c1", "c2"),
                                show='headings', height=15)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="No Terminal")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Produccion")
            self.newNoTerminals = []
            for res in self.result:
                if not self.newNoTerminals.__contains__(res[0]):
                    # Agrega a una nueva lista los nuevos NoTerminales
                    self.newNoTerminals.append(res[0])
                    # Values son las propiedades que se mostraran en la tabla
                tree.insert('', "end", text="1", values=(res[0], [res[1]]))
            tree.place(x=0, y=5)


        # ============ Encontrar los primeros de cada no terminal ==============
        def PrimerosGramatica1():
            self.firstList = []
            # Por verificar 
            for nT in self.newNoTerminals:
                f1 = AnalyzerLL1.SearchFirst(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), nT)
                self.firstList.append(f1)
            """
            r1 = AnalyzerLL1.SearchFirst(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "S")
            self.firstList.append(r1)
            r2 = AnalyzerLL1.SearchFirst(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "S'")
            self.firstList.append(r2)
            r3 = AnalyzerLL1.SearchFirst(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "P")
            self.firstList.append(r3)
            r4 = AnalyzerLL1.SearchFirst(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "P'")
            self.firstList.append(r4)
            r5 = AnalyzerLL1.SearchFirst(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "K")
            self.firstList.append(r5)
            r6 = AnalyzerLL1.SearchFirst(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "K'")
            self.firstList.append(r6)
            r7 = AnalyzerLL1.SearchFirst(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "C")
            self.firstList.append(r7)
            r8 = AnalyzerLL1.SearchFirst(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "T")
            self.firstList.append(r8)
            r9 = AnalyzerLL1.SearchFirst(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "C'")
            self.firstList.append(r9)
            """
            s = ttk.Style()
            s.theme_use('clam')

            # Configura los estilos de la cabecera de la tabla
            s.configure('Treeview.Heading', background="#fdfd96")

            tree = ttk.Treeview(frame, column=("c1", "c2"),
                                show='headings', height=15)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="No Terminal")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Primeros")
            for idx, item in enumerate(self.firstList):
                    # Values son las propiedades que se mostraran en la tabla
                tree.insert('', "end", text="1", values=(
                    # Muestra el NoTerminal y su produccion
                    self.newNoTerminals[idx], [item]))
            tree.place(x=0, y=5)


        # =========== Encontrar los siguientes de cada NoTerminal ============
        def SiguientesGramatica1():
            self.nextList = []
            # Por validar
            for nT in self.newNoTerminals:
                s1 = AnalyzerLL1.SearchNext(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), nT)
                self.nextList.append(s1)
            """
            s1 = AnalyzerLL1.SearchNext(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "S")
            self.nextList.append(s1)
            s2 = AnalyzerLL1.SearchNext(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "S'")
            self.nextList.append(s2)
            s3 = AnalyzerLL1.SearchNext(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "P")
            self.nextList.append(s3)
            s4 = AnalyzerLL1.SearchNext(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "P'")
            self.nextList.append(s4)
            s5 = AnalyzerLL1.SearchNext(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "K")
            self.nextList.append(s5)
            s6 = AnalyzerLL1.SearchNext(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "K'")
            self.nextList.append(s6)
            s7 = AnalyzerLL1.SearchNext(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "C")
            self.nextList.append(s7)
            s8 = AnalyzerLL1.SearchNext(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "T")
            self.nextList.append(s8)
            s9 = AnalyzerLL1.SearchNext(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result), "C'")
            self.nextList.append(s9)
            """
            s = ttk.Style()
            s.theme_use('clam')

            # Configura la cabecera de la tabla
            s.configure('Treeview.Heading', background="#84b6f4")

            tree = ttk.Treeview(frame, column=("c1", "c2"),
                                show='headings', height=15)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="No Terminal")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Siguientes")
            for idx, item in enumerate(self.nextList):
                tree.insert('', "end", text="1", values=(
                    self.newNoTerminals[idx], [item]))
            tree.place(x=0, y=5)


        # ============ Buscar conjunto prediccion de la gramatica ============
        def ConjuntoPredGramatica1():
            s = ttk.Style()
            s.theme_use('clam')

            # Configura los estilos de la cabecera de tabla
            s.configure('Treeview.Heading', background="#F0B66B")

            tree = ttk.Treeview(frame, column=("c1", "c2"),
                                show='headings', height=15)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="No Terminal")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Conjunto Prediccion")

            # Inserta los datos a la tabla
            for item in self.result:
                cp = AnalyzerLL1.PredictionSet(AnalyzerLL1(
                    self.newNoTerminals, self.initial, self.result), item[1])
                tree.insert('', "end", text="1", values=(item[0], [cp]))

            tree.place(x=0, y=5)

        def GenerarTabla():
            # Mostrara la tabla de NoTerminales y Terminales
            # Por ahora solo analiza si la gramatica es apta para LL1
            f2 = AnalyzerLL1.VerifyLL1(AnalyzerLL1(
                self.newNoTerminals, self.initial, self.result))
            print(f2)


        # ================ Contenedor para los botones ================
        frameBtn = LabelFrame(self.window, text="Botones",
                              font=("Arial", 15), background="#d8af97")
        frameBtn.place(x=110, y=5, width=205, height=280)


        # ================ Contenedor para las tablas ================
        frame = LabelFrame(self.window, text="Tablas",
                           font=("Arial", 15), background="#ecd6c0")
        frame.place(x=10, y=290, width=408, height=360)


        # =========== Botones para manipular la interfaz ==============
        btn_font = font.Font(family="Roboto Cn", size=11)
        Button(frameBtn, text="Ver Gramatica", font=btn_font, background="#ffffeb",
               command=Gramatica1).place(x=0, y=5, width=200, height=35)
        Button(frameBtn, text="Aplicar Recursion", font=btn_font, background="#ffffeb",
               command=RecursionGramatica1).place(x=0, y=45, width=200, height=35)
        Button(frameBtn, text="Aplicar Primeros", font=btn_font, background="#ffffeb",
               command=PrimerosGramatica1).place(x=0, y=85, width=200, height=35)
        Button(frameBtn, text="Aplicar Siguientes", font=btn_font, background="#ffffeb",
               command=SiguientesGramatica1).place(x=0, y=125, width=200, height=35)
        Button(frameBtn, text="Conjunto Prediccion", font=btn_font, background="#ffffeb",
               command=ConjuntoPredGramatica1).place(x=0, y=165, width=200, height=35)
        Button(frameBtn, text="Generar Tabla", font=btn_font, background="#ffffeb",
               command=GenerarTabla).place(x=0, y=205, width=200, height=35)


# ======== Inicializa la interfaz en Tkinter =========
if __name__ == "__main__":
    gui = Tk()
    gui.geometry("425x650")
    gui.configure(bg="#d8af97")
    app = Interface(gui)
    gui.mainloop()
