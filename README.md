### How to Setup

1. Clone das Repository \
`git clone https://github.com/siebertdaniel/pb2-example.git` 

2. Installier die Dependencies 
`poetry install` 

3. Start coding 

### Szenario
Sie sind Teil der Entwicklungsabteilung der IT Enterprises GmbH.\
Für viele kleine lokale Fernsehsender sollen Wetterkarten für die tägliche Wettervorhersage erstellt werden.\
Bisher wurden diese per Hand von einzelnen Mitarbeitern der jeweiligen Fernsehsender ersellt. \
Sie sollen ein Script erstellen, welches ein Template mit Wetterdaten füllt. Die Wetterdaten bekommen Sie über eine API.\
Danach holen sich die Fernsehsender die Dateien auf einem Server der IT Enterprises ab. \
Über CLI-Argumente sollen die Städte mitgegeben werden, für welche eine Grafik erstellt werden soll.\
z.B.: \
`$ python3 script.py Hamburg Munich Москва`

Die Outputdateien sollen die Stadt und den aktuellen Tag als Dateinamen haben. \
z.B.: \
`out-Hamburg-2024-04-05.png` \
`out-Munich-2024-04-05.png` \
`out-Москва-2024-04-05.png`

### Arbeitsaufträge
- API abfragen
- Daten ins richtige Format bringen
- Template mit Daten füllen

### Genutzte Librarys
- [Pillow](https://pypi.org/project/pillow/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)