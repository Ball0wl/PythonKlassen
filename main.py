class BauplanAutoKlasse():
    """ Klasse zum Erstellen von Autos, dies ist ein hilftext.
    """

    def __init__(self, marke, farbe, baujahr, kmstand=0, sitze=4):
        self.marke = marke
        self.farbe = farbe
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.sitze = sitze
        self.dauergarage = 0

    def hupen(self, anzahl=3):
        print(anzahl * "tuuU")

    def steht_garage(self, dauer):
        print(self.marke, "steht in der Garage. ", dauer, "Minuten ")
        self.dauergarage += dauer
        print(self.marke, "Steht insgesamt seit: ", self.dauergarage, " Minuten")


auto_audi = BauplanAutoKlasse("Audi", "Rot", 1999, 143000, 5)
auto_bmw = BauplanAutoKlasse("BMW", "Silber", 2009)
auto_mercedes = BauplanAutoKlasse("Mercedes", "Schwarz", 2014, 4)

auto_bmw.steht_garage(60)
auto_audi.steht_garage(30)

auto_bmw.hupen()
auto_audi.hupen()

print("Marke:", auto_audi.marke, "Farbe", auto_audi.farbe, "Baujahr", auto_audi.baujahr, auto_audi.kmstand, "km",
      "Sitze", auto_audi.sitze)
print("Marke:", auto_bmw.marke, "Farbe", auto_bmw.farbe, "Baujahr", auto_bmw.baujahr, auto_bmw.kmstand, "km", "Sitze",
      auto_bmw.sitze)
print("Marke:", auto_mercedes.marke, "Farbe", auto_mercedes.farbe, "Baujahr", auto_mercedes.baujahr, auto_mercedes.kmstand, "km", "Sitze",
      auto_mercedes.sitze)
