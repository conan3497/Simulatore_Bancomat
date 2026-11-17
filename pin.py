

# - JSON serve per leggere e scrivere dati strutturati in formato JSON
# - os serve per interagire con il sistema operativo (per esempio controlla se il file esiste)

import json #Importo la libreia json 
import os #Serve per controllare se il file esiste già

#funzione per json (in prova al momento)
# Legge saldo, PIN e storico dal file JSON all'avvio del programma
def carica_dati():
   #se il file esiste, leggo il saldo e il pin (controlla se il file esiste)
   if os.path.exists("conto.json"):
      with open("conto.json", "r", encoding="utf-8") as file:
         dati=json.load(file) #converte il contenuto del file JSON
         print("Dati caricati del file JSON con successo")

         #Restituisce i tre valori al programma principale
         return dati ["saldo"], dati ["pin"], dati.get("movimenti",[])
   else:
      #se il file non esiste, alla prima configurazione, uso il valori di default
      print("Nessun file trovato. Creo un nuovo conto con i dati predefiniti") 
      #return 2000.00, 4869
      saldo=2000.00
      pin=4869
      movimenti_iniziali=[]
      #Crea il file JSOn con i dati iniziali
      salva_dati(saldo,pin,movimenti_iniziali)
      return saldo, pin, movimenti_iniziali
   

def salva_dati(saldo, pin, movimenti): #Salva saldo, PIN e lista movimenti dentro il file JSON
   #creo i dati da salvare
   dati={
      "saldo": saldo,
      "pin": pin,
      "movimenti": movimenti
   }  

   #Apre o crea il file in modalità scrittura ("w"), sovrascrivendo i vecchi dati
   #File JSON
   with open ("conto.json","w", encoding="utf-8") as file:
      json.dump(dati,file,indent=4) #L'indent=4 rende il file leggibile
   print("Dati di saldo e PIN salvati nel file JSON")   
     

# Funzioni delle operazioni

def visualizza_saldo (saldo): #Mostra a schermo il saldo formatattato con 2 cifre decimali .2f
   print(f"\n Il tuo saldo attuale è: {saldo:.2f} €\n")

def effettua_deposito (saldo,movimenti):
   #Gestisce il versamento di denaro,  e aggiorna saldo e storico  controlla i fondi in numero con la virgola (float)

   
   print ("\n DEPOSITO")
   importo=float (input("quanto vuoi depositare"))

   # Controllo 1: Verifico che l'importo sia maggiorre di zero
   if importo <=0:
      print("\n importo non valido")
   # Controllo 2: verfica che ci siano abbastanza soldi sul conto   
   elif importo > saldo:
      print(f"\n Fondi insufficienti saldo: {saldo:.2f}€\n")   
   else:
      # Somma che l'importo al saldo attuale
      saldo +=importo    #aggiunge il saldo
      print ("\n soldi depositati con successo")
      print ("\n hai depositato",  importo)
      print ("\n nuovo saldo disponibile", saldo)

      #Registra l'operazione nella lista dello storico dei movimenti          
      movimenti.append(f"Deposito: +{importo:.2f} € (Saldo residuo: {saldo:.2f} €)")
   return saldo #restituisce il saldo aggiornato

def effettua_prelievo(saldo,movimenti):
    # Gestisce il prelievo, controlla i fondi e aggiorna saldo e storico
    print ("\n PRELIEVO")
    
    #Chiede l'importo all'utente e converte in numero in virgola mobile (float)
    importo=float (input("quanto vuoi prelevare?"))
    if importo <=0:
      print("\n importo non valido")

      # Controllo: Verfica che ci siano abbastanza soldi sul conto
    elif importo > saldo: 
      print("fondi insufficienti")
    else:
      saldo -= importo #Sottrae l'importo prelevanto dal saldo locale
      print("\n Prelievo effettuato con successo")
      print("\n Hai prelevat: ", importo)
      print("\n Nuovo saldo disponibile", saldo)
                
      movimenti.append(f"Prelievo: +{importo:.2f} € (Saldo residuo: {saldo:.2f} €)")
    return saldo #restituisce il nuovo saldo al programma principale e aggiorna la variabile

def Storico(movimenti): #Stampa tutti i movimenti registrati
    
    print("\n STORICO MOVIMENTI")
    # Controlla se la lista è vuota
    if len(movimenti)==0:
      print("Nessuna operazione registrata")
    else:
      #stampo tutti i movimenti memorizzati nella variabile movimenti
     for movimento in movimenti:
      print (movimento)
      print()

def cambio_pin (pin_corretto): #Permette di cambiare il pin attuale
   vecchio_pin=int(input("Inserisci il tuo pin:"))
      # controlla che l'utente conosca il PIN attuale
   if vecchio_pin == pin_corretto:
    nuovo_pin=int(input("Inserisci il nuovo pin"))
    conferma_pin=int(input("Conferma il nuovo pin"))
    #confronto il nuovo pin con quello nuovo
    if nuovo_pin==conferma_pin:
                     
     pin_corretto=nuovo_pin
     print("\nPIN modificato con successo")

   return pin_corretto #restituisce il nuovo pin al programma principlale

def salva_estratto_conto (movimenti, saldo): #Genera una ricevuta tipo "scontrino" in formato TXT
   with open("Estratto conto.txt","w", encoding="utf-8") as file:
               file.write("ESTRATTO CONTO DEL BANCOMAT")

               if len(movimenti) == 0:
                  file.write("Nessuna operazione effettuata in questa sessione")
               else:
                  for movimento in movimenti:
                     # Scrive ogni movimento su una nuovo riga del file di testo
                     file.write(movimento + "\n")

                     # scrive il riepilogo finala fuori dal ciclo for
               file.write(f"\n Saldo finale disponibile: {saldo:.2f} €\n")

               print("File 'estratto_conto.txt' salvato sul comuter")    
    



# all'avvio, recupera i dati salvati dal file JSON (o crea quelli iniziali)
saldo, pin_corretto, movimenti=carica_dati()

accesso= False
tentativi=3 # Variabile per gestire i tentativi di accesso

#movimenti= []

while tentativi >0:

    pin=int(input("Inserisci il pin"))   

    if pin == pin_corretto:
       print("Accesso consentito")
       accesso=True
       break #interrompe il ciclo se il PIN è giusto

    else:
     tentativi-=1 # Scala un tentativo
   
    if tentativi >0:
           print ("accesso negato ti rimangono questi tentativi", tentativi)
    else:
        print("carta bloccata")

# Menu interrattivo
if accesso:
  uscita=False

  # Il menù continua a ripetersi finche 'uscira' non diventa True
  while not uscita:
          print(" MENU BANCOMAT")
          print("1. Visualizza saldo")
          print("2 Deposita Soldi")
          print("3. Preleva Soldi")
          print("4 Visualizzazzione Storico Movimenti")
          print("5.Cambio Pin")
          print("6.Esci")

          scelta=input("Scegli un'opzione")

          if scelta== "1":
            visualizza_saldo(saldo)

          elif scelta== "2":
             saldo=effettua_deposito(saldo, movimenti)
             
          elif scelta =="3":
             saldo =effettua_prelievo(saldo, movimenti)
            
          elif scelta == "4":
             Storico(movimenti)
             
          elif scelta == "5":
              # Chiama la funzione e salva l'eventuale nuovo PIN nella veriabile 'pin_corretto'
              pin_corretto = cambio_pin(pin_corretto)
                  
          elif scelta == "6":
            print("\nArrivederci! Attendi sto salvando il tuo estratto conto sun file")
            # Salva lo stato nel file JSOn per la prossima sessione
            salva_dati(saldo, pin_corretto, movimenti)#salva stato del json

            #creazione e scrittura del file di testo TXT
            salva_estratto_conto(movimenti, saldo)
                     
            uscita = True  # Fa terminare il ciclo del menu
          else:
            print("\nScelta non valida. Inserisci un numero da 1 a 6.\n")

# Questo input finale evita che la finestra si chiuda di colpo su Windows
input("\nPremi Invio per chiudere il programma...")