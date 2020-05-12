import hangman
import reversegam
import tictactoeModificado
import os
import json
import PySimpleGUI as sg

def main(args):
	sigo_jugando = True
	while sigo_jugando:
	
		layout = [
		[sg.Text('Ingrese su Nombre')],
		[sg.Input(key = "1")],
		[sg.Button("Enviar"), sg.Button("Exit") ] ]
     
		window = sg.Window("Bienvenido/a", layout)
		
		nombreJugador = "No se ingreso un jugador"
		
		while True:
			event, values = window.Read()

			if event in (None, 'Exit'):
				break

			if event == 'Enviar':
				nombreJugador = values["1"]
			window.close()
	
	
		layout1 = [
				[sg.Text("Elegí qué juego queres jugar")],
				[sg.Radio("Ahorcado", "RADIO1"),
				sg.Radio('TicTacToe', "RADIO1"),
				sg.Radio('Otello', "RADIO1"),
				sg.Radio("Salir", "RADIO1")],
				[sg.Button("Enviar"), sg.Button("Exit") ] ]
	
		window = sg.Window("A continuación, el menú de juegos disponibles", layout1)
				
		event, juegoElegido = window.Read()

		window.close()
		
		jugadorJugo = "No jugo"
		
		if event in (None, 'Exit'):
			sigo_jugando = False			
		if event == 'Enviar':	
		
		
		
			if juegoElegido[0] == True:
				hangman.main()
				jugadorJugo = "Ahorcado"
			elif juegoElegido[1]  == True:
				tictactoeModificado.main()
				jugadorJugo= "TicTacToe"
			elif juegoElegido[2] == True:
				reversegam.main()
				jugadorJugo = "Otello"
			elif juegoElegido[3] == True:
				sigo_jugando = False

			
        
		agregarDatos = [{"nombre": nombreJugador, "jugo": jugadorJugo}]
		if os.path.exists("jugadores.txt"):
			archivo=open ("jugadores.txt","r+")
			datos = json.load(archivo)
			datos.append(agregarDatos)
			archivo.seek(0)
			json.dump(datos,archivo)
		else:
			archivo = open("jugadores.txt" , "x")
			json.dump(agregarDatos,archivo)
		archivo.close()	
	
		jugador = open ("jugadores.txt", "r")
		datos = json.load(jugador)
		print(json.dumps(datos))
		jugador.close()
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))    				

    
