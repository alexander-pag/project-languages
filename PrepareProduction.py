class PrepareProduction:

    def __init__(self, noTerminals, initial, productions):
        self.noTerminals = noTerminals
        self.initial = initial
        self.productions = productions

    def DeleteRecursionLeft(self):

        currentNoTerminal = self.initial  # S

        # Variables que se usaran para realizar la recursion izquierda
        productionNew = []
        sameNoTerminal = False
        productionEmpty = []

        for production in self.productions:
            newProduction = []
            p = production
            # Divide los elementos de p
            aux = p[1].split(" ")
            # Comprobamos si el NoTerminal que esta analizando cambio
            if currentNoTerminal != p[0]:
                if sameNoTerminal == True:
                    # Agrega el lambda al final cuando se realizo la creacion
                    # del nuevo o los nuevos NoTerminales
                    productionEmpty.append("λ")
                    productionNew.append(productionEmpty)
                    productionEmpty = []
                # Cambiamos el terminal que se va a evuluar setea a False
                # para indicar que se cambio de NoTerminal
                currentNoTerminal = p[0]
                sameNoTerminal = False

            # Se valida si el NoTerminal que se esta analizando es igual al valor incial de su produccion
            if aux[0] == p[0]:
                # Verifica si no se habia añadido antes la nueva produccion 
                if sameNoTerminal == False:
                    # Crea el nuevo NoTerminal añadiendo una '
                    productionEmpty.append((p[0]+"'"))
                # Cambia para indicar que esta en un terminal y se añade la nueva NoTerminal
                sameNoTerminal = True
                newProduction.append((p[0]+"'"))
                
                # Guardara las producciones de los nuevos NoTerminales creados
                prod = ""
                for idx, item in enumerate(aux):
                    # Omite el primer elemento ya que es donde se genera la recursion
                    if idx == 0:
                        prod = aux[idx+1]
                    else:
                        # Agrega a la ultima posicion el nuevo NoTerminal
                        if idx == len(aux)-1:
                            prod = prod+" "+p[0]+"'"
                        else:
                            prod = prod+" "+aux[idx+1]
                # Se agrega la produccion creada sin recursion 
                newProduction.append(prod)
                # Se agrega lo anterior para generar una nueva gramatica
                productionNew.append(newProduction)

            else:
                # Verifica si anteriormente en el NoTerminal habia recursion
                if sameNoTerminal == True:
                    index = self.productions.index(p)
                    # Crea una produccion para eliminar la recursion
                    st = p[1]+" "+p[0]+"'"
                    # En la posicion donde habia recursion se cambia por la nueva sin recursion
                    self.productions[index][1] = st
                    if p[0] == self.initial:
                        # Añade al inicio el NoTerminal con su produccion eliminada recursion
                        productionNew.insert(0, self.productions[index])
                    else:
                        # El nuevo NoTerminal se añade posterior al que lo genero
                        productionNew.insert(index, self.productions[index])
                else:
                    # Si la produccion no tenia recursion izquierda se añade tal y como estaba
                    productionNew.append(p)

        # Añade el lambda a la lista de producciones de los nuevos NoTerminales
        if sameNoTerminal == True:
            productionEmpty.append("λ")
            productionNew.append(productionEmpty)
            productionEmpty = []
        return productionNew
