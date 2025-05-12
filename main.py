from fastapi import FastAPI

app = FastAPI()
nome_lista = []

@app.get("/")
def homepage():
    return "Ciao, questa è l'homepage"

@app.get("/es1")
def hello():
    return "Hello World!"

@app.get("/es2")
def nome(nome, cognome):
    return "Ciao" + nome + cognome 

@app.post("/aggiungi-utente")
def aggiungi_utente(username):
    nome_lista.append(username)
    print(nome_lista)
    return "Utente aggiunto con successo" 

@app.get("/cerca-utente")
def cerca_utente(cerca_utente: str):
    if cerca_utente in nome_lista:
        return "l'utente è presente nella lista"
    else: 
        return "l'utente non è non presente nella lista"
    
@app.get("/totale_utenti")
def totale_utenti():
    return "Il totale degli utenti è: " + str(len(nome_lista))

@app.delete("/elimina_utente")
def elimina_utente(elimina_utente):
    if elimina_utente in nome_lista:
        nome_lista.remove(elimina_utente)
        return "L'utente è stato rimosso"
    else:
        return "Errore, utente non trovato" 


@app.get("/testo")
def analisi_testo(testo):

    from langdetect import detect

    lingua = detect(testo)

    print(f"La lingua rilevata è: {lingua}")
    return "La lingua rilevata è: " + lingua 


from textblob import TextBlob

@app.get("/frase")
def analisi_frase(frase: str):

    blob = TextBlob(frase)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        sentiment = "Positivo"
    elif sentiment < 0:
        sentiment = "Negativo"
    else: 
        sentiment = "Neutro"
    return "Il sentiment della frase è " + str(sentiment)

