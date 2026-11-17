# Simulatore_Bancomat

Un semplice simulatore di bancomat da terminale, scritto in Python.
Permette di gestire un conto con PIN, saldo e storico dei movimenti.

## ✨ Funzionalità

- Accesso protetto da PIN (3 tentativi disponibili)
- Visualizzazione del saldo
- Deposito e prelievo di denaro, con controlli sull'importo
- Storico dei movimenti della sessione
- Cambio del PIN
- Salvataggio automatico dei dati in `conto.json`
- Generazione dell'estratto conto in formato `.txt`

## 🛠️ Requisiti

- Python 3.x
- Nessuna libreria esterna (usa solo `json` e `os`, già incluse in Python)

## 🚀 Come si usa

1. Clona o scarica il repository
2. Avvia il programma da terminale:
   ```bash
   python "nome_programma".py
   ```
3. Al primo avvio viene creato un conto con saldo **2000,00 €** e PIN **4869**

## 📁 File del progetto

- `bancomat.py`: codice sorgente
- `conto.json`: dati del conto (creato automaticamente) 
- `Estratto conto.txt`: estratto conto generato all'uscita 

## 📚 Cosa ho imparato

Questo progetto mi ha permesso di esercitarmi con funzioni, cicli `while`, gestione dei file, il formato JSON e la gestione degli input dell'utente.

## 🔮 Possibili miglioramenti

- Cifrare il PIN invece di salvarlo in chiaro
- Gestire meglio gli input non numerici
- Separare il codice in più file (interfaccia, logica, dati)

## 📄 Licenza

Progetto didattico
