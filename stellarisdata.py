class StellarisDataLibrary():
    def __init_():
        print("Stellaris Data Library Loaded")

    self.traits = {
        "Adapative" : {
            "Habitability" : 10
            "Excludes" : ["ExtremlyAdaptive", "Nonadaptive", "Robust"]
        }
        "ExtremlyAdaptive" : {
            "Habitability" : 20
            "Excludes" : ["Adaptive", "Nonadaptive", "Robust"]
        }
        "Agarian" : {
            "JobFoodProduction" : 15
        }
        "Charismatic" : {
            "JobAmenityProduction": 20
            "Excludes" : ["Repugnant"]
        }
        "Communal" : {
            "PopHousingUsage" : -10
            "Excludes" : ["Solitary", "Nerve", "Stapled"]
        }
        "Conformists" : {
            "GoverningEthicsAttraction" : 30
            "Excludes" : ["Deviants", "Hive-Minded"]
        }
        "Conservationist" : {
            "PopConsumerGoodsUpkeep" : -10
            "Excludes" : ["Wasteful", "Hive-Minded"]
        }
        "Enduring" : {
            "LeaderLifeSpan" : 20
            "Excludes" : ["Venerable", "Fleeting"]
        }
        "Venerable" : {
            "LeaderLifeSpan" : 80
            "Excludes" : ["Enduring", "Fleeting"]
        }
        "Industrious" : {
            "JobMineralProduction" : 15
        }
        "Ingenious" : {
            "JobEnergyProduction" : 15
        }
        "Intelligent": {
            "JobEngineeringResearchProduction" : 10
            "JobPhysicsResearchProduction" : 10
            "JobSocietyResearchProduction" : 10
            "Excludes" : ["Erudite","Nerve","Stapled","Uplifted(EnigmaticCache)","SomewhatUplifted"]
        }
        "NaturalEngineers" : {
            "JobEngineeringResearchProduction" : 15
            "Excludes" : ["NaturalPhysicists", "NaturalSociologists","Nerve","Stapled"]
        }
        "NaturalPhysicists" : {
            "JobPhysicsResearchProduction" : 15
            "Exlcudes" : ["NaturalEngineers","NaturalSociologists","Nerve","Stapled"]
        }
        "NaturalSociologists" : {
            "JobSocietyResearchProduction" : 15
            "Exlcudes" : ["NaturalEngineers","NaturalPhysicists","Nerve","Stapled"]
        }
        "Nomadic" : {
            "ImmigrationPopGrowth" : 15
            "ResettlementCost" : -25
            "Excludes" : ["Sedentary"]
        }
        "QuickLearners" : {
            "LeaderExperienceGain" : 25
            "Excludes" : ["SlowLearners"]
        }
        "RapidBreeders" : {
            "GrowthSpeed" : 10
            "Excludes" : ["Fertile","SlowBreeders"]
        }
        "Resilient" : {
            "ArmyDamage" : 50
            "DefenseArmy": True
        }
        "Strong" : {
            "ArmyDamage" : 20
            "WorkerOutput" : 2
            "Excludes" : ["VeryStrong","Weak"]
        }
        "VeryStrong" : {
            "ArmyDamage" : 40
            "WorkerOutput" : 5
            "Excludes" : ["Strong", "Weak"]
        }
        "Talented" : {
            "LeaderLevelCap" : 1
        }
        "Thrifty" : {
            "JobTradeValue" : 25
        }
        "Traditional" : {
            "JobUnityProduction" : 10
            "Excludes" : ["Quarrelsome"]
        }
        "Decadent" : {
            "WorkerHapiness" : -10
            "SlaveHapiness" : -10
        }
        "Deviants" : {
            "GoverningEthicsAttraction" : -15
            "Excludes" : ["Conformists", "Hive-Minded"]
        }
        "Fleeting" : {
            "LeaderLifespan" : -10
            "Excludes" : ["Venerable", "Enduring"]
        }
        "Nonadaptive" : {
            "Habitability" : -10
            "Excludes": ["Adaptive", "ExtremelyAdaptive", "Robust"]
        }
        "Quarrelsome": {
            "JobUnityProduction" : -10
            "Excludes" : "Traditional"
        }
        "Repugnant" : {
            "JobAmenityProduction" : -20
            "Excludes" : ["Charismatic"]
        }
        "Sedentary" : {
            "ImmigrationPopGrowth" : -15
            "ResettlementCost" : 25
            "Excludes" : ["Normadic"]
        }
        "SlowBreeders" : {
            "GrowthSpeed" : -10
            "Excludes" : ["RapidBreeders", "Fertile"]
        }
        "SlowLearners" : {
            "LeaderExperienceGain" : -25
            "Excludes" : ["QuickLearners"]
        }
        "Solitary" : {
            "PopHousingUsage" : 10
            "Excludes" : ["Communal", "Nerve", "Stapled"]
        }
        "Wasteful" : {
            "PopConsumerGoodsUpkeep" : 10
            "Excludes" : ["Conservationist", "Hive-Minded"]
        }
        "Weak" : {
            "ArmyDamage" : -20
            "WorkerOutput" : -2
            "Excludes" : ["Strong", "VeryStrong"]
        }
    }
    self.lithoidtraits = {
        "Lithoid" : {
            "PopGrowthSpeed" : -25
            "Habitability" : 50
            "ArmyHealth" : 50
            "LeaderLifeSpan" : 50
            "FoodIsMinerals" : True
        }
        "GaseousByproducts" : {
            "PopExoticGasProduction" : 0.01
            "Excludes" : ["ScintillatingSkin","VolatileExcretions"]
        }
        "ScintillatingSkin" : {
            "PopRareCrystalProduction" : 0.01
            "Excludes" : ["GaseousByproducts", "VolatileExcretions"]
        }
        "VolatileExcretions" : {
            "PopVolatileMoteProduction" : 0.01
            "Excludes" : ["GaseousByproducts", "ScintillatingSkin"-]
        }
    }