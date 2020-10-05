class Film():
    nb = 1

    def __init__(self, titre, seance, places):
        self.nb = Film.nb
        self.titre = titre
        self.seance = seance
        self.places = places
        Film.nb += 1

    def __str__(self):
        return (f"Film n°{self.nb}: {self.titre} , seance de {self.seance}  de disponible) ")
