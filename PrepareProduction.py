class PrepareProduction:

    def __init__(self, noTerminals, initial, productions):
        self.noTerminals = noTerminals
        self.initial = initial
        self.productions = productions

    def DeleteRecursionLeft(self):

        currentNoTerminal = self.initial  # S

        productionNew = []
        sameNoTerminal = False
        productionEmpty = []

        for production in self.productions:
            newProduction = []
            p = production
            aux = p[1].split(" ")

            if currentNoTerminal != p[0]:
                if sameNoTerminal == True:
                    productionEmpty.append("λ")
                    productionNew.append(productionEmpty)
                    productionEmpty = []

                currentNoTerminal = p[0]
                sameNoTerminal = False

            if aux[0] == p[0]:
                if sameNoTerminal == False:
                    productionEmpty.append((p[0]+"'"))
                sameNoTerminal = True
                newProduction.append((p[0]+"'"))

                prod = ""
                for idx, item in enumerate(aux):
                    if idx == 0:
                        prod = aux[idx+1]
                    else:
                        if idx == len(aux)-1:
                            prod = prod+" "+p[0]+"'"
                        else:
                            prod = prod+" "+aux[idx+1]
                            
                newProduction.append(prod)
                productionNew.append(newProduction)

            else:
                if sameNoTerminal == True:
                    index = self.productions.index(p)
                    st = p[1]+" "+p[0]+"'"
                    self.productions[index][1] = st
                    if p[0] == self.initial:
                        productionNew.insert(0, self.productions[index])
                    else:
                        #para ordenar primero P y luego P'
                        productionNew.insert(index, self.productions[index])
                else:
                    productionNew.append(p)

        if sameNoTerminal == True:
            productionEmpty.append("λ")
            productionNew.append(productionEmpty)
            productionEmpty = []
        return productionNew
