# PROG2 Spielprojekt

## Team

| Name | Matrikelnummer | FH-Mail |
|------|----------------|---------|
| Florian Zielke | 951907 | florian.zielke@stu.haw-kiel.de |
| Johanna Wieber | 952178 | johanna.wieber@stu.haw-kiel.de |

## Spielidee

Die konkrete Spielidee wurde im Team noch abgestimmt.
Geplant ist das Spiel "Sokoban"

Aufgabenverteilung?!
Zur Aufteilung, damit main.py nicht Kraut und Rüben wird, sollten wir alle Parts ob Level oder Spieler, Kisten etc. in Dateien auslagern. Die können wir mit game.py alle einfach miteinander verbinden bzw. einbinden.

Beispiel der Dateien:
Für Sokoban würde ich erstmal diese .py-Dateien anlegen:

main.py
game.py
player.py
level.py
box.py
settings.py

main.py
Soll man anscheinend Bauen damit Startet einfach nur das Spiel. Einstiegspunkt.

game.py
Damit verbinden wir alles miteinander. Game-Loop, Updates, Zeichnen, Übergabe zwischen Player und Level.

player.py
Alles was den Spieler betrifft wie Position, Bewegung, Animationen.

level.py
Alles rund um das Spielfeld herum was damit zusammen hängt. Map, Wände, Ziele, freie Felder, später Kollisionen.

box.py
Kisten separat, damit wir das Verhalten nicht in player oder level quetschen müssen?! ggf später andere Sorten noch ergänzen

settings.py (Hab ich mir noch nicht angeschaut)
Soll anscheinend wichtig sein für Fenstergröße, Tilegröße, FPS.

Florian

player.py
Bewegungslogik
Johanna

level.py
Kollisionsprüfung
offen: Assets finden

Kisten und und und
