class StellarisDataLibraryCivics():
    def __init_(self):
        print("Stellaris Data Library.Civics Loaded")
        self.Civics = {
            "AgarianIdyll" : {
                "ProductionDistrictHousing" : 1,
                "CityDistrictHousing" : -1,
                "FarmersProduceAmentities" : 2,
                "DisableArcologyAscensionPerk" : True,
                "req" : ["Pacifist", "Fanatic-Pacifist"],
                "Excludes" : ["SyncreticEvolution", "SlaverGuilds", "Post-Apocalyptic"],
                "tooltip" : "A simple and peaceful life can often be the most rewarding. This agarian society has to a large extent, managed to avoid large-scale urbanization."
            },
            "AristocraticElite" : {
                "GovernorlevelCap" : 1,
                "CapitalBuildingAdministratorJobsBecomeNobleJobs" : True,
                "NobleEstates" : True,
                "req" : ["Oligarchic", "Imperial"]
            }
        }