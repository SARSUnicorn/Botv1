import random



def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'kim jest przełożony':
        return 'Przełożonym jest żołnierz lub osoba nie będąca żołnierzem, któremu na mocy przepisów prawa, rozkazu, polecenia lub decyzji podporządkowano żołnierza (podwładnego), uprawniona do wydawania rozkazów, poleceń służbowych podwładnym żołnierzom lub osobom nie będącym żołnierzami i kierowania ich czynnościami służbowymi'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'saperka':

        return "Nie saperka tylko łopatka piechoty, a teraz wypierdalać kopać okop"

    if p_message == 'kto to jest przełożony':
        return "Przełożonym jest żołnierz lub osoba nie będąca żołnierzem, któremu na mocy przepisów prawa, rozkazu, polecenia lub decyzji podporządkowano żołnierza (podwładnego), uprawniona do wydawania rozkazów, poleceń służbowych podwładnym żołnierzom lub osobom nie będącym żołnierzami i kierowania ich czynnościami służbowymi"
    if p_message == 'do kawalerii wstąpić chciałem':

        return "długo kochanie swoje prosić musiałem"

    if p_message == 'słuchaj kotku nie martw się':
        return "Bo w kawalerii wcale nie jest źle"

    if p_message == 'sokół, śmigło to jest to':
        return "Dwóch pilotów obsługuje go" 
