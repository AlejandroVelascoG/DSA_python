# Python 3.7

# 	Parse from json format into csv format
# 	It creates "cooperacion.csv"

print("Importing libraries...")
import json
#import numpy as np
import pandas as pd
print("Done!")


######################################################
# Data parsing begins here...
######################################################

N = input("How many data_lgc*.json files are to be parsed?: ")
End = int(N)

indices = []      # Saves the numbers that correspond to data_lgc*.json in folder
D_Frames = []     # Saves the dataframes created for performance from each file

for i in range(1, int(End) + 1):
	print('Trying to open file ' + 'data_lgc' + str(i) + '.json')
	try:
		f = open('data_lgc' + str(i) + '.json', 'r')
		print("OK!")
		f.close()
		indices.append(str(i))
	except:
		print("No good! No indice " + str(i))

# Listas con datos
pareja = []
jugador = []
stage = []
ronda = []
experticia = []
rotulo = []
mensajeRecibido = []
rightWrong = []
objetoSolicitado = []

supreme = [pareja, jugador, stage, ronda, experticia, rotulo, mensajeRecibido, rightWrong, objetoSolicitado]

for counter in indices:
	# Opens json file with data from experiment and uploads it into Data
	data_archivo = 'data_lgc' + counter + '.json'
	with open(data_archivo) as data_file:
		Data = json.load(data_file)
	data_file.close()

	# --------------------------------------------------
	# Processing information of players performance
	# --------------------------------------------------

	# Finding dyad
	Players = []
	for d in Data:
		if d[u'player'] not in Players:
			Players.append(d[u'player'])

	print("Lista de jugadores: ", Players)
	assert(len(Players) == 2), "Error: Pareja no contiene numero exacto de jugadores!"

	dyadName = str(Players[0][:5]) + '-' + str(Players[1][:5])
	print("Dyad name: ", dyadName)

	for d in Data:
		try:
			print("Reading line with recibido data...", len(d[u'Respuesta']))
			p = d[u'player']
			s = d[u'stage'][u'stage']
			r = d[u'stage'][u'round']
			siNo = d[u'Respuesta'][0]
			# perro = d[u'Respuesta'][1]
			contador = int(d[u'Respuesta'][2])
			print("Tupla: ", (p, s, r, contador))
			dictRecibido[(p, s, r, contador)] = siNo

		except:
			print("No respuesta. Skip!")

	for d in Data:
		try:
			print("Reading line with comunicacion data...", len(d[u'Comunicacion']))
			# print('Intentando...')
			pareja.append(dyadName)
			jugador.append(d[u'player'])
			s = d[u'stage'][u'stage']
			stage.append(s)
			r = d[u'stage'][u'round']
			ronda.append(r)
			experticia.append(d[u'Raza'])
			rotulo.append(d[u'Comunicacion'][0])
			objetoSolicitado.append(d[u'Comunicacion'][1])

			# comprobacion de que el mensaje enviado fue de la experticia

			if d[u'Raza'] == 'hound':
				if (d[u'Comunicacion'] == 'A' or d[u'Comunicacion'] == 'C'):
					print('Good hound!')
				else:
					print('Bad hound!')
			if d[u'Raza'] == 'terrier':
				if (d[u'Comunicacion'] == 'B' or d[u'Comunicacion'] == 'D'):
					print('Good terrier!')
				else:
					print('Bad terrier!')


			Sups.append(d[u'Comunicacion'][2])
			contador = d[u'Comunicacion'][3]
			Contador.append(contador)
			if Players[0] == d[u'player']:
				p = Players[1]
			else:
				p = Players[0]
			print("Tupla: ", (p, s, r, contador))
			try:
				o = dictRecibido[(p, s, r, contador)]
				mensajeRecibido.append(o)
			except:
				print("No response!")
				mensajeRecibido.append('-')
		except:
			print("No comunicacion. Skip!")

for i in supreme:
	print(len(i))

dict = {
	'Dyad': pareja,
	'Player': jugador,
	'Stage': stage,
	'Round': ronda,
	'Expertise': experticia,
	'Posicion Preguntado': objetoSolicitado,
	'Asked': rotulo,
	'Answered': mensajeRecibido,
	# 'Correctness': rightWrong
}
data = pd.DataFrame.from_dict(dict)

archivo = 'cooperacion.csv'
data.to_csv(archivo, index=False)
print("Data saved to ", archivo)
