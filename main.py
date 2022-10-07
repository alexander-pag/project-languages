from PrepareProduction import *
from Colors import *
from AnalyzerLL1 import *
import os

os.system("")


#
productions = [["S", "S + P"], ["S", "P int"],
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
noTerminals = ["S", "P", "K", "T", "C"]
# ??
z = []
# S
initial = "S"

result = PrepareProduction.DeleteRecursionLeft(
    PrepareProduction(noTerminals, initial, productions))

print(Colors.YELLOW + "Gramatica ya aplicada recursion izquierda")
for res in result:
    # imprimir por consola la gramatica con colores para diferenciar NOTERMINALES y TERMINALES
    print(Colors.CYAN + "{}".format(res[0]), Colors.RED +
          "->", Colors.PURPLE + "{}".format(res[1]))


# Primeros
"""

r1 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "S")
r2 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "S'")
r3 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "P")
r4 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "P'")
r5 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "K")
r6 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "K'")
r7 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "T")
r8 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "C")
r9 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "C'")


print("S", r1)
print("S'", r2)
print("P", r3)
print("P'", r4)
print("K", r5)
print("K'", r6)
print("T", r7)
print("C", r8)
print("C'", r9)

"""

s1 = AnalyzerLL1.SearchNext(AnalyzerLL1(noTerminals, initial, result), "C")
print(s1)
