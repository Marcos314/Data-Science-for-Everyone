### Listas em Python

        [a, b, c]
  
        alturas = [1.73, 1.68, 1.71, 1.89]

#### Listas de listas

        alturas_familia = [
            ["Marcos", 1.65],
            ["Wanderson", 1.72],
            ["Washington", 1.65],
            ["Maria", 1.62]]


####  Acessando Listas

        fam = ["liz",1.73, "emma",1.68, "mom", 1.71, "dad",1.89]
    
        fam[6]
        Output: 'dad'

        fam[-1]
        Output: 1.89

#### Fatiamento de Listas (Slicing)
        
        [   start     :    end    ]
           inclusive     exclusive

        fam[3:5]
        Output: [1.68, 'mom']

#### Manipulando Listas

* Adicionando, atualizando e removendo elementos de uma lista

        #Create the areas list and make some changes
        areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

        #Add poolhouse data to areas, new list is areas_1
        areas_1 = areas + ["poolhouse", 24.5]

        #Add garage data to areas_1, new list is areas_2
        areas_2 = areas_1 + ["garage", 15.45]

        ---------------------------- #  ----------------------------
        #Create the areas list
        areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

        #Correct the bathroom area
        areas[9] = 10.50

        #Change "living room" to "chill zone"
        areas[4] = "chill zone"

        ---------------------------- #  ----------------------------

        Por fim, você também pode remover elementos de sua lista. Você pode fazer isso com a deldeclaração:

        x = ["a", "b", "c", "d"]
        del(x[1])

### Funções e pacotes

