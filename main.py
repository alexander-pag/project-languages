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
noTerminals = ["S", "P", "K", "C"]
# ??
z = []
# S
initial = "S"

result = PrepareProduction.DeleteRecursionLeft(
    PrepareProduction(noTerminals, initial, productions))


r1 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "S")
r2 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "P")
r3 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "P'")
r4 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "S'")
r5 = AnalyzerLL1.SearchFirst(AnalyzerLL1(noTerminals, initial, result), "C")


print("S", r1)
print("P", r2)
print("P'", r3)
print("S'", r4)
print("C", r5)

for res in result:
    #imprimir por consola la gramatica con colores para diferenciar NOTERMINALES y TERMINALES
    print(Colors.CYAN + "{}".format(res[0]), Colors.RED + "->", Colors.PURPLE + "{}".format(res[1]))