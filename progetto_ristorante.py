import datetime
import random
# ----------------------------------------------------------------------------------------
print("Benvenuti al ristorante 'Da Tiepo'")
print("ORARI : Tutti i giorni dalle 12 alle 23")
print()
# ----------------------------------------------------------------------------------------

class Ristorante:
    def __init__(self):
        self.l_tavoli = [[0,"disponibile",5,"non_fumatori"],
                    [1,"occupato",2,"non_fumatori","Maria","3482568994"],
                    [2,"disponibile",4,"fumatori"],
                    [3,"disponibile",7,"non_fumatori"],
                    [4,"occupato",3,"fumatori","Andrea","3482568995"],
                    [5,"disponibile",4,"non_fumatori"],
                    [6,"disponibile",7,"fumatori"],
                    [7,"occupato",9,"non_fumatori","Angelo","3482568992"],
                    [8,"disponibile",8,"fumatori"],
                    [9,"disponibile",2,"non_fumatori"]
                        ]

        self.l_camerieri = [["Piero", 8],
                            ["Sandro", 2],
                            ["Ciro", 1],
                            ]

        self.l_primi_piatti = [["Spaghetti alle Vongole", 15],
                               ["Fettuccine al Pomodoro", 8.50],
                               ["Ravioli al Branzino", 4],
                               ["Tortelli Burro e Salvia",7.50],
                               ["Cappellacci di Zucca", 6]
                               ]

        self.l_antipasti = [["Selezione di Salumi", 14],
                            ["Tartare al Limone", 8],
                            ["Carpaccio di Ricciola", 12],
                            ["Cocktail di Gamberi", 7],
                            ["Caprese", 5]
                            ]

        self.l_dolci = [["Semifreddo al Mascarpone", 9],
                        ["Torta del Giorno", 9],
                        ["Crepes con Nutella", 6],
                        ["Sorbetto al Limone", 4],
                        ]

        self.ordinati = []

        self.conto = 0

        self.posti = 0
        
# - MENU ----------------------------------------------------------------------------------
    def menu(self):
        print()
        
    #Menu Principale
        print("Ha/Avete Prenotato? "),print()
        self.prenotazione_conferma = int(input("[1 - si] [2 - no] : "))

        if self.prenotazione_conferma == 1:
            persona.accedi()
        if self.prenotazione_conferma == 2:
            persona.prenota()
        if self.prenotazione_conferma > 2 or self.prenotazione_conferma < 1:
            print()
            print("Comando Non Riconosciuto")
            
# - ACCEDI AL TAVOLO ----------------------------------------------------------------------
    def accedi(self):
        print()
        
    #Controllo Presenza prenotazione e stampa Menu
        conferma_nome = input("Venga inserito il nome per la verifica : ")
        conferma_numero = int(input("Venga inserito il numero del tavolo per la conferma : "))

        ind_portata = 0 #Indice per stampa estetica
        ind_quantita = 0 #Indice di scorrimento
        ind = conferma_numero #Indice per controllo (IMP)
    
        try:
            if self.l_tavoli[ind][1] == "occupato":
            
                if self.l_tavoli[ind][4] != conferma_nome or self.l_tavoli[ind][0] != conferma_numero:
                    print()
                    print("Sembra che la sua prenotazione non sia presente, riprovi!")
            
                if self.l_tavoli[ind][4] == conferma_nome and self.l_tavoli[ind][0] == conferma_numero:
                    self.posti = self.l_tavoli[ind][2] #Set self.posti per ciclo ordini
                    print()
                    print("Prenotazione verificata e confermata"),print()
                    print("               ** MENÚ **"),print()
            
                    print("--------------- ANTIPASTI ------------"),print()
                    for portata in self.l_antipasti:
                        print(ind_portata,"-",portata[0],portata[1],"€"),print()
                        ind_portata += 1

                    print("--------------- PRIMI ---------------"),print()
                    ind_portata = 0
                    for portata in self.l_primi_piatti:
                        print(ind_portata,"-",portata[0],portata[1],"€"),print()
                        ind_portata += 1

                    print("--------------- DOLCI ---------------"),print()
                    ind_portata = 0
                    for portata in self.l_dolci:
                        print(ind_portata,"-",portata[0],portata[1],"€"),print()
                        ind_portata += 1

                    print("               ** TIPOLOGIA PIATTO **")
                    print(" 1 - Antipasti","\n","2 - Primi Piatti","\n","3 - Dolci","\n","4 - Fine"),print()

                #Input Ordine basato su numero di posti
                    for ordine in range (self.posti): 
                        tipologia_piatto = int(input("Seleziona il tipo di piatto che vuole essere ordinato : "))
            
                        if tipologia_piatto == 1:
                            print()
                            print("Hai selezionato ANTIPASTI"),print()
                            ordinazione = int(input("Cosa si vuole ordinare? : "))
                            quantita = int(input("Quante se ne vogliono ordinare? : "))
                            print("HAI SELEZIONATO : ",self.l_antipasti[ordinazione][0]),print()
                            self.ordinati.append(self.l_antipasti[ordinazione])
                            
                        #Per evitare che ordinato uno stesso piatto la quantita si duplichi all'interno della lista
                            if len(self.ordinati[ind_quantita]) < 3:
                                self.ordinati[ind_quantita].append(quantita)
                                ind_quantita += 1

                        if tipologia_piatto == 2:
                            print()
                            print("Hai selezionato PRIMI PIATTI"),print()
                            ordinazione = int(input("Cosa si vuole ordinare? : "))
                            quantita = int(input("Quante se ne vogliono ordinare? : "))
                            print("HAI SELEZIONATO : ",self.l_primi_piatti[ordinazione][0]),print()
                            self.ordinati.append(self.l_primi_piatti[ordinazione])
                
                            if len(self.ordinati[ind_quantita]) < 3:
                                self.ordinati[ind_quantita].append(quantita)
                                ind_quantita += 1

                        if tipologia_piatto == 3:
                            print()
                            print("Hai selezionato DOLCI"),print()
                            ordinazione = int(input("Cosa si vuole ordinare? : "))
                            quantita = int(input("Quante se ne vogliono ordinare? : "))
                            print("HAI SELEZIONATO : ",self.l_dolci[ordinazione][0]),print()
                            self.ordinati.append(self.l_dolci[ordinazione])
                            
                            if len(self.ordinati[ind_quantita]) < 3:
                                self.ordinati[ind_quantita].append(quantita)
                                ind_quantita += 1

                        if tipologia_piatto == 4:
                            break

                        if tipologia_piatto > 4 or tipologia_piatto < 1:
                            print()
                            print("Comando Non valido")
                            print()

                    print()

                    ind_scontrino = 0 #indice di scorrimento
                    print("               ** SCONTRINO **")
                    print()
                    for j in self.ordinati:
                        somma_moltiplicata = (self.ordinati[ind_scontrino][1]) * self.ordinati[ind_scontrino][2]
                        print(self.ordinati[ind_scontrino][0],self.ordinati[ind_scontrino][1],"€ x",self.ordinati[ind_scontrino][2],"porzioni","=",somma_moltiplicata,"€")
                        self.conto += somma_moltiplicata
                        ind_scontrino += 1
                    
                    print()
                    print("CONTO TOTALE : ",self.conto,"€")
                    print("Serviti dal cameriere : ",random.choice(self.l_camerieri[0]))


                #Ripristino stato tavolo
                    self.l_tavoli[ind][1] = "disponibile"
                    self.l_tavoli[ind].remove(self.l_tavoli[ind][4]) #Prima il nome
                    self.l_tavoli[ind].remove(self.l_tavoli[ind][4]) #Poi il numero
                    
            else:
                print()
                print("Il tavolo selezionato NON ha subito PRENOTAZIONI!")
            
        except IndexError:
            print()
            print("Il tavolo selezionato NON é ESISTENTE!")
            
# - PRENOTAZIONE -------------------------------------------------------------------------            
    def prenota(self):
        current_time = datetime.datetime.now()
        giorno_corrente = current_time.day
        print()
        print("Tavoli Disponibili : ")

    #Controllo Disponbilitá tavoli con stampa
        ind = 0 #Indice di scorrimento
        for i in self.l_tavoli:
            if self.l_tavoli[ind][1] == "disponibile":
                print(self.l_tavoli[ind])
                ind += 1
            
            elif self.l_tavoli[ind][1] == "occupato":
                ind += 1
            
        print()

    #Input dati per prenotazione
        print("               ** PRENOTAZIONE **")
        print()
        nome = str(input("Inserisci Nome : "))
        numero_tel = int(input("Inserisci numero di telefono [senza spazi] : "))
        while len(str(numero_tel)) != 10:
            print()
            print("Numero Non Accettabile, il telefono deve essere di 10 numeri"),print()
            numero_tel = int(input("Inserisci numero di telefono [senza spazi] : "))
            
        giorno = int(input("Inserisci giorno in cui si vuole prenotare [non oltre 31] : "))
        while True:
            if giorno > 31:
                print()
                print("Giorno Non Accettabile"),print()
            if giorno < giorno_corrente:
                print()
                print("Non é una macchina del tempo, oggi é il :",giorno_corrente,"seleziona il giorno stesso o successivo"),print()
            if giorno <= 31 and giorno >= giorno_corrente:
                break
            giorno = int(input("Inserisci giorno in cui si vuole prenotare [non oltre 31] : "))


            
        ora = int(input("Inserisci ora in cui si vuole prenotare [non oltre 23] : "))
        while True:
            if ora > 23:
                print()
                print("Ora Non Accettabile, il ristorante non rimane aperto dopo le 23"),print()
            if ora < 12:
                print()
                print("Ora Non Accettabile, il ristorante apre alle 12"),print()
            if ora <= 23 and ora >= 12:
                break
            ora = int(input("Inserisci ora in cui si vuole prenotare [non oltre 23] : "))
            
        n_persone = int(input("Inserisci per quante persone si vuole prenotare : "))
        fumatori = int(input("É richiesta la possibilitá di fumare? [1 - si] [2 - no] : "))
        n_tavolo = int(input("Inserisci il numero del tavolo tra quelli mostrati precedentemente : "))
    
        print()

    #Conversione Int - Str
        if fumatori == 2:
            fumatori = "non_fumatori"
        else:
            fumatori = "fumatori"

    #Verifica Disponibilitá tavolo
        ind = n_tavolo 
        if self.l_tavoli[ind][1] == "disponibile" and self.l_tavoli[ind][2] >= n_persone:
            if fumatori != self.l_tavoli[ind][3]:
                print("Attenzione!, La selezione tra le caratteristiche del tavolo e quelle dell'utente non corrispondono!"),print()
                continua_fumatori = int(input("Continuare ugualmente? [1 - si] [2 - no] : "))
                print()

                if continua_fumatori == 1:
                    self.l_tavoli[ind].append(nome)
                    self.l_tavoli[ind].append(numero_tel)
                    self.l_tavoli[ind][1] = "occupato"
                    print("TAVOLO",self.l_tavoli[ind],"É stato SELEZIONATO"),print()
                    self.posti = n_persone
                    
                    print("               ** RIEPILOGO DATI **"),print()
                    print(" NOME : ",nome,"\n","NUMERO TELEFONO : ",numero_tel,"\n","GIORNO : ",giorno,"\n","ORE : ",ora,"\n","NUMERO_PERSONE : ",n_persone,"\n","FUMATORI : ",fumatori)

                else:
                    print("Attenzione la prenotazione non é andata a buon fine, riprovare!")
            else:
                self.l_tavoli[ind].append(nome)
                self.l_tavoli[ind].append(numero_tel)
                self.l_tavoli[ind][1] = "occupato"
                print("TAVOLO",self.l_tavoli[ind],"É stato SELEZIONATO"),print()
                self.posti = n_persone
                
                print("               ** RIEPILOGO DATI **"),print()
                print(" NOME : ",nome,"\n","NUMERO TELEFONO : ",numero_tel,"\n","GIORNO : ",giorno,"\n","ORE : ",ora,"\n","NUMERO_PERSONE : ",n_persone,"\n","FUMATORI : ",fumatori)

        if self.l_tavoli[ind][1] == "disponibile" and self.l_tavoli[ind][2] < n_persone:
            print("Il tavolo selezionato non ha la capacitá richiesta, riprovare!")


# - MAIN ---------------------------------------------------------------------------------
persona = Ristorante()
persona.menu()

while True:
    print()
    continua = int(input("Continuare? [1 - si] [2 - no] : "))
    if continua == 1:
        persona.menu()
    else:
        print()
        print("Grazie per aver utilizzato il programma")
        break
# ----------------------------------------------------------------------------------------
    
