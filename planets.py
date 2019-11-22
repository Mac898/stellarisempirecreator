class StellarisDataLibraryPlanets():
    def __init_(self):
        print("Stellaris Data Library.Planets Loaded")
        self.Arid = {
            "80" : ["Arid"],
            "60" : ["Desert", "Savannah"],
        },
        self.Desert = {
            "80" : ["Desert"],
            "60" : ["Arid", "Savannah"],
        },
        self.Savannah = {
            "80" : ["Savannah"],
            "60" : ["Arid", "Desert"],
        },
        self.Alpine = {
            "80" : ["Alpine"],
            "60" : ["Arctic", "Tundra"],
        },
        self.Arctic = {
            "80" : ["Arctic"],
            "60" : ["Alpine", "Tundra"],
        },
        self.Tundra = {
            "80" : ["Tundra"],
            "60" : ["Alpine", "Arctic"],
        },
        self.Continental = {
            "80" : ["Continental"],
            "60" : ["Ocean", "Tropical"]
        },
        self.Ocean = {
            "80" : ["Ocean"],
            "60" : ["Continental", "Tropical"],
        },
        self.Tropical = {
            "80" : ["Tropical"],
            "60" : ["Continental", "Ocean"],
        },