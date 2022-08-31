class BauplanAutoKlasse():
    """ Klasse zum Erstellen von Autos, dies ist ein hilftext.
    """

    def __init__(self, marke, farbe, baujahr, kmstand, sitze):
        self.marke = marke
        self.farbe = farbe
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.sitze = sitze


auto_audi = BauplanAutoKlasse("Audi", "rot", 1999, 143000, 5)

print("Marke:", auto_audi.marke, "Farbe", auto_audi.farbe, "Baujahr", auto_audi.baujahr, auto_audi.kmstand, "km", "Sitze", auto_audi.sitze)
