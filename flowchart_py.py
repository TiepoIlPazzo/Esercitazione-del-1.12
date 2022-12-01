print("RIPRODUZIONE FLOWCHART VERIFICA IN PYTHON")
print("--------------------------------------------------")
print()

print("Controllo ingredienti nel magazzino...")
ingredienti = int(input("Sono presenti gli ingredienti? [1 - SI] [2 - NO] : "))
print()

ristoranti = ["pesce da Gianni","Pizzeria portami via","Ristorante la baita","trattoria dalla nonna"]
piatti = ["insalata","pizza surgelata","panino tonno e cipolla","cestini di mozzarella","crostini con gorgonzola e mirtilli"]
piatti_asporto = ["piadina pomodoro mozzarella e prosciutto","ramen","lumache alla francese","tortellini al brodo"]
cont = 1
cont_2 = 1

if ingredienti == 1:
    print("I Piatti disponibili sono: ")
    for i in piatti:
        print(cont,")",i)
        cont += 1
    print()
    soddisfatto = int(input("Il cliente é soddisfatto? [1 - SI] [2- NO]: "))
    print()
    
    if soddisfatto == 1:
        piatto_scelto = int(input("Seleziona il piatto desiderato: "))
        while True:
            if piatto_scelto > len(piatti):
                piatto_scelto = int(input("piatto non esistente, Seleziona il piatto desiderato: "))
            print()
            print("Il piatto selezionato sta venendo preparato attendere.")
            print("Il piatto é pronto e sta per essere servito")
            break
        
    elif soddisfatto == 2:
        print("Nessun piatto soddisfa il cliente, ecco una lista di ristoranti nelle vicinanze...")
        print()
        for i in ristoranti:
            print(i,"\n")
    print("----- FINE ----- ")

if ingredienti == 2:
    mangiare_in_albergo = int(input("Il cliente é ancora disposto a mangiare in albergo? [1 - SI] [2- NO]: "))
    print()
    if mangiare_in_albergo == 1:
        print("Seleziona uno dei piatti che verrá ordinato...")
        print()
        print("I Piatti disponibili sono: ")
        for i in piatti_asporto:
            print(cont_2,")",i)
            cont_2 += 1
        print()
        piatto_scelto = int(input("Seleziona il piatto desiderato: "))
        print()
        while True:
            if piatto_scelto > len(piatti_asporto):
                piatto_scelto = int(input("piatto non esistente, Seleziona il piatto desiderato: "))
            print()
            print("Piatto selezionato, l'ordine arriverá entro 30 minuti")
            break
    if mangiare_in_albergo == 2:
        print("Il cliente non é piú disposto a rimanere, ecco una lista di ristoranti nelle vicinanze...")
        print()
        for i in ristoranti:
            print(i,"\n")
    print("----- FINE ----- ")
        
