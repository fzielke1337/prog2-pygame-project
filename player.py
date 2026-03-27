#player
#Hier kommt der Spieler rein, incl der Verlinkung zu den Assets
#Der Spieler wird die Abfrage an level.py schicken. Aktuell Walls(Liste) 
#Das Level entscheidet ob der Spieler sich bewegt oder nicht bzw die Walls die geladen wurden


class Player:
    def __init__(self, x, y):                               #Konstruktor: erhält Startposition des Spielers (vom Level übergeben)
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE) #Erstellen des richtigen Players im Level mit den übergebenen werten (Körper wird erstellt) x/y level position Tile_Size körpergröße

    def move(self, dx, dy, walls):                          #Methode dx/dy übergebene Schrittweite, walls übergebene walls
        alt_x = self.rect.x                                 #speichern des alten Startpunkt vor der Bewegung in x-Richtung
        alt_y = self.rect.y                                 #speichern des alten Startpunkt vor der Bewegung in y-Richtung

        self.rect.x += dx                                   #schritt wird addiert oder subtrahiert (Bewegung Horizontal)
        self.rect.y += dy                                   #schritt wird addiert oder subtrahiert (Bewegung Vertikal)

        for wall in walls:                                  #abfrage aller Walls in dem Level
            if self.rect.colliderect(wall):                 #Wenn der Spieler(self.rect) nach der Bewegung mit einer Wall kollidiert (Liste der Walls wird abgefragt) -> als fläche also x,y und size 60x60
                self.rect.x = alt_x                         #alte x Position wieder einnehmen
                self.rect.y = alt_y                         #alte y Position wieder einnehmen
                return False                                #Bewegung nicht erlaubt -> Spieler bleibt stehen alte werte werden geladen

        return True                                         #Wenn keine kollision denn True

    def draw(self, screen, color):                          #Methode Spieler wird an der stelle gezeichnet.
        pygame.draw.rect(screen, color, self.rect)          #zeichnet auf dem bildschirm, in farbe des spielers, an der position self.rect