# PROG2 Spielprojekt

## Team

| Name | Matrikelnummer | FH-Mail |
|------|----------------|---------|
| Florian Zielke | 951907 | florian.zielke@stu.haw-kiel.de |
| Johanna Wieber | 952178 | johanna.wieber@stu.haw-kiel.de |

## Spielidee

Titel: Blob Adventure

Unser Spiel soll im Stil von klassischen Sokoban- und Pushy-Spielen ein 2D-Levelspiel werden, bei dem der Spieler eine kleine Figur (Blob) durch verschiedene Level manövriert bis hin zum Ausgang. 
Auf dem Weg dorthin müssen verschiedene Hindernisse oder Aufgaben erledigt werden, zum Beispiel das Aktivieren von Schaltern, bewegen von Kisten oder das richtige Platzieren von Objekten um zum Ausgang zu gelangen. 
Dabei soll jedes Level andere Schwierigkeiten und Überraschungen bereithalten. Je nachdem wie gut das umsetzbar ist könnten Ideen sein: 

- Ein Dunkel-Level, in denen nur der Bereich um den Blob mit Taschenlampe sichtbar ist
- Schalter, auf die eine Kiste geschoben werden muss, damit die Tür offen bleibt
- Unsichtbar-Level, Blob ist unsichtbar und man sieht nur seine Aktionen
- Rutsch-Level, Blob bewegt sich nicht mehr Kästchenweise, sondern Bewegung läuft automatisch und flüssig weiter
- Telepotations- oder Farbfelder, Schlüssel- und Schlossfelder oder ähnliches 


main.py
Startet einfach nur das Spiel

game.py
Damit verbinden wir später alles miteinander. Game-Loop, Zeichnen, Übergabe zwischen Player und Level.

player.py
Alles was den Spieler betrifft wie Position, Bewegung, Animationen.

level.py
Alles rund um das Spielfeld herum was damit zusammen hängt. Map, Wände, Ziele, freie Felder, später Kollisionen.

box.py
Kisten separat, damit wir das Verhalten nicht in player oder level quetschen müssen?! ggf später andere Sorten noch ergänzen

settings.py 
Fenstergröße, Tilegröße, FPS.

