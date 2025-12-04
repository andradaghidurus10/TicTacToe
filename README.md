Joc Tic-Tac-Toe în Python

Un joc simplu de X și 0 scris în Python, unde utilizatorul joacă împotriva calculatorului.
Programul rulează în consolă și folosește o interfață text pentru afișarea tablei de joc.

 Caracteristici
	•	Jucătorul este X
	•	Calculatorul este O
	•	Mutările sunt validate (nu poți pune pe un loc ocupat)
	•	Tabla este afișată după fiecare mutare
	•	Sunt detectate toate situațiile:
	  •	Jucătorul câștigă
	  •	Calculatorul câștigă
	  •	Egalitate
	•	Programul folosește rânduri și coloane pentru a calcula pozițiile
	•	Cod organizat pe funcții (castigator, tabla_plina, afisare_placa etc.)

Exemplu tabelă de joc

Așa arată tabla în terminal:

+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+


Cum rulezi jocul?
	1.	Asigură-te că ai instalat Python 3.10+
	2.	Descarcă fișierul joc_nou_tic-tac-toe.py
	3.	Rulează din terminal:

python joc_nou_tic-tac-toe.py

	4.	Introdu poziția unde vrei să pui X

Calculatorul răspunde automat.

Structura proiectului
 ticTacToe
 ├── joc_nou_tic-tac-toe.py
 └── README.md

Funcții importante

- afisare_placa(board)

Afișează tabla de joc cu separatoare.

- castigator(board, simbol)

Verifică dacă X sau O a făcut o linie câștigătoare.

- tabla_plina(board)

Verifică dacă jocul s-a terminat în egalitate.

Posibile îmbunătățiri (pentru viitor)
	•	Alegerea nivelului de dificultate: ușor / mediu / greu
	•	Mutări inteligente pentru calculator (Minimax)
	•	Interfață grafică în Tkinter
	•	Sistem de scor (mai multe runde)

Autor

Andrada Ghiduruș
