class AnalyzerLL1:

    def __init__(self, noTerminals, initial, productions):
        self.noTerminals = noTerminals
        self.initial = initial
        self.productions = productions

    def SearchFirst(self, noTerminal):
        # Lista que se retornara con los Primeros de cada NoTerminal
        firstList = []
        # Recorre la gramatica buscando las producciones que coincidad con el NoTerminal
        for production in self.productions:
            p = production
            if p[0] == noTerminal:
                # Divide las producciones de ese NoTerminal
                productionList = p[1].split(" ")
                # Añade a la lista de primeros validando que no se haya agregado antes
                # Si el primer termino de los antes separados es lambda
                if productionList[0] == "λ":
                    # Si en la lista de primeros no esta lambda lo añade
                    if not firstList.__contains__(productionList[0]):
                        firstList.append(productionList[0])

                else:
                    # En el caso de que sea un Terminal se añade a lista
                    if not self.noTerminals.__contains__(productionList[0]):
                        if not firstList.__contains__(productionList[0]):
                            firstList.append(productionList[0])
                    # En el caso de que sea un NoTerminal se hace una busqueda de sus primeros
                    # mediante recursion
                    else:
                        aux = self.SearchFirst(productionList[0])
                        for item in aux:
                            if not firstList.__contains__(item):
                                firstList.append(item)
        # Una vez evaluada todos los primeros de ese NoTerminal se retorna la lista con su Primeros
        return firstList

    def SearchNext(self, noTerminal):
        # Lista que se retornara con los siguientes del NoTerminal evaludado
        nextList = []
        # Recorre la gramatica para buscar al NoTerminal
        for production in self.productions:
            p = production
            # Separa los elementos que coincidan
            productionList = p[1].split(" ")
            # Verifica si el NoTerminal esta en la produccion
            # Se añade cada siguiente de cada NoTerminal a la lista verificando que no se repita
            if noTerminal == self.initial and not nextList.__contains__("$"):
                # Entra con el NoTerminal inicial y se añade el $
                nextList.append("$")
            else:
                if productionList.__contains__(noTerminal):
                    # Busca la posicion del NoTerminal
                    index = productionList.index(noTerminal)
                    # Verifica si esta en la ultima posicion
                    if index < len(productionList)-1:
                        # Si el siguiente item es un NoTerminal se llama al metodo buscar primeros
                        # para añadirlos a la lista
                        if self.noTerminals.__contains__(productionList[index + 1]):
                            first = self.SearchFirst(productionList[index + 1])
                            for item in first:
                                # Si el item evaluado es lambda
                                if item == "λ":
                                    # Se añaden los siguientes del NoTerminal haciendo un llamado al SearchNext
                                    nextAux = self.SearchNext(
                                        productionList[index + 1])
                                    for aux in nextAux:
                                        # Verifica que en la lista retornada al llamar SearchNext
                                        # no se repita elemento para agregarlo
                                        if not nextList.__contains__(aux):
                                            nextList.append(aux)
                                else:
                                    # Si no es lambda el item osea un Terminal se añade verificando que no este
                                    # ya desde antes
                                    if not nextList.__contains__(item):
                                        nextList.append(item)
                        else:
                            # Si el elemento que sigue es un Terminal se añade sin repetir
                            if not nextList.__contains__(productionList[index + 1]):
                                nextList.append(productionList[index + 1])
                    else:
                        # Si el elemento que sigue es lambda se llama a SearchNext para agregar los siguientes del
                        # NoTerminal evaluado
                        if p[0] != noTerminal:
                            auxNext = self.SearchNext(p[0])
                            for item in auxNext:
                                if not nextList.__contains__(item):
                                    nextList.append(item)
        # Retorna la lista de los siguientes del NoTerminal evaluado
        return nextList

    def PredictionSet(self, production):
        cp = []
        productionList = production.split(" ")
        if productionList[0] == "λ":
            auxNext = self.SearchNext(production[0])
            cp = cp+auxNext
        else:
            if self.noTerminals.__contains__(productionList[0]):
                auxFirst = self.SearchFirst(productionList[0])
                cp = cp+auxFirst
            else:
                cp.append(productionList[0])
        return cp

    def VerifyLL1(self):
        self.ll1 = True
        for item in self.noTerminals:
            newList = []
            for prod in self.productions:
                if prod[0] == item:
                    listCP = self.PredictionSet(prod[1])
                    for cp in listCP:
                        if newList.__contains__(cp):
                            self.ll1 = False
                        newList.append(cp)
        if not self.ll1:
            return "No es LL1"
        return "Es LL1"
