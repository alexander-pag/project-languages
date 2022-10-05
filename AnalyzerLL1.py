class AnalyzerLL1:

    def __init__(self, noTerminals, initial, productions):
        self.noTerminals = noTerminals
        self.initial = initial
        self.productions = productions

    def SearchFirst(self, noTerminal):   
        firstList = []
        for production in self.productions:
            p = production
            if p[0] == noTerminal:
                productionList = p[1].split(" ")
                if productionList[0] == "λ":
                    if not firstList.__contains__(productionList[0]):
                        firstList.append(productionList[0])
                else:
                    if not self.noTerminals.__contains__(productionList[0]):
                        if not firstList.__contains__(productionList[0]):
                            firstList.append(productionList[0])
                    else:
                        aux = self.SearchFirst(productionList[0])
                        for item in aux:
                            first = item
                            if not firstList.__contains__(first):
                                firstList.append(first)
 
        return firstList
