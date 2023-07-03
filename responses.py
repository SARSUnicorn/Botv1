import random

def handle_response(message) -> str:
	p_messgae = message.lower()

	if p_message == 'kim jest przelozony':
		return 'Przełożonym jest żołnierz lub osoba nie będąca żołnierzem, któremu na mocy przepisów prawa, rozkazu, polecenia lub decyzji podporządkowano żołnierza (podwładnego), uprawniona do wydawania rozkazów, poleceń służbowych podwładnym żołnierzom lub osobom nie będącym żołnierzami i kierowania ich czynnościami służbowymi.'

	if p_message == 'roll':
		return str(random.randint(1, 6))

	if p_messgae == 'bottom':
		return "`There is a reason why he is a bottom`"
	