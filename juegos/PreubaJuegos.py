import PySimpleGUI as sg
import hangman
import reversegam
import tictactoeModificado

sigo_jugando = True
while sigo_jugando:
	

	layout = [
			[sg.Text("Elegi con que juego queres jugar")],
			[sg.Radio("Ahorcado", "RADIO1"),
			sg.Radio('TicTacToe', "RADIO1"),
			sg.Radio('Otello', "RADIO1"),
			sg.Radio("Salir", "RADIO1")],
			[sg.Button("Enviar"), sg.Button("Exit") ] ]
	
	window = sg.Window("Ventana", layout)
		
	event, x = window.Read()

	window.close()
	if event in (None, 'Exit'):
		sigo_jugando = False			
	if event == 'Enviar':		
		if x[0] == True:
			hangman.main()
		elif x[1]  == True:
			tictactoeModificado.main()
		elif x[2] == True:
			reversegam.main()
		elif x[3] == True:
			sigo_jugando = False




