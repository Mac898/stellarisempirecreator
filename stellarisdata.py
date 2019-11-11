class StellarisDataLibrary():
    def __init_():
        print("Stellaris Data Library Loaded")

    self.traits = {
        "Adapative" : {
            "Habitability" : 10,
            "Excludes" : ["ExtremlyAdaptive", "Nonadaptive", "Robust"]
        },
        "ExtremlyAdaptive" : {
            "Habitability" : 20,
            "Excludes" : ["Adaptive", "Nonadaptive", "Robust"]
        },
        "Agarian" : {
            "JobFoodProduction" : 15
        },
        "Charismatic" : {
            "JobAmenityProduction": 20,
            "Excludes" : ["Repugnant"]
        },
        "Communal" : {
            "PopHousingUsage" : -10,
            "Excludes" : ["Solitary", "Nerve", "Stapled"]
        },
        "Conformists" : {
            "GoverningEthicsAttraction" : 30,
            "Excludes" : ["Deviants", "Hive-Minded"]
        },
        "Conservationist" : {
            "PopConsumerGoodsUpkeep" : -10,
            "Excludes" : ["Wasteful", "Hive-Minded"]
        },
        "Enduring" : {
            "LeaderLifeSpan" : 20,
            "Excludes" : ["Venerable", "Fleeting"]
        },
        "Venerable" : {
            "LeaderLifeSpan" : 80,
            "Excludes" : ["Enduring", "Fleeting"]
        },
        "Industrious" : {
            "JobMineralProduction" : 15
        },
        "Ingenious" : {
            "JobEnergyProduction" : 15
        },
        "Intelligent": {
            "JobEngineeringResearchProduction" : 10,
            "JobPhysicsResearchProduction" : 10,
            "JobSocietyResearchProduction" : 10,
            "Excludes" : ["Erudite","Nerve","Stapled","Uplifted(EnigmaticCache)","SomewhatUplifted"]
        },
        "NaturalEngineers" : {
            "JobEngineeringResearchProduction" : 15,
            "Excludes" : ["NaturalPhysicists", "NaturalSociologists","Nerve","Stapled"]
        },
        "NaturalPhysicists" : {
            "JobPhysicsResearchProduction" : 15,
            "Exlcudes" : ["NaturalEngineers","NaturalSociologists","Nerve","Stapled"]
        },
        "NaturalSociologists" : {
            "JobSocietyResearchProduction" : 15,
            "Exlcudes" : ["NaturalEngineers","NaturalPhysicists","Nerve","Stapled"]
        },
        "Nomadic" : {
            "ImmigrationPopGrowth" : 15,
            "ResettlementCost" : -25,
            "Excludes" : ["Sedentary"]
        },
        "QuickLearners" : {
            "LeaderExperienceGain" : 25,
            "Excludes" : ["SlowLearners"]
        },
        "RapidBreeders" : {
            "GrowthSpeed" : 10,
            "Excludes" : ["Fertile","SlowBreeders"],
            "tooltip" : "This species reproduces at a very rapid rate, increasing population growth.",
            "cost" : 2
        },
        "Resilient" : {
            "ArmyDamage" : 50,
            "DefenseArmy": True,
            "tooltip" : "Members of this species are physiologically resilient and will fight like enraged brood mothers to defend their worlds.",
            "cost" : 1
        },
        "Strong" : {
            "ArmyDamage" : 20,
            "WorkerOutput" : 2,
            "Excludes" : ["VeryStrong","Weak"],
            "tooltip" : "Members of this species possess great physical strength, making them formidable fighters on the ground.",
            "cost" : 1
        },
        "VeryStrong" : {
            "ArmyDamage" : 40,
            "WorkerOutput" : 5,
            "Excludes" : ["Strong", "Weak"],
            "tooltip" : "Members of this species possess a strength that almost defies the laws of physics.",
            "cost" : 3
        },
        "Talented" : {
            "LeaderLevelCap" : 1,
            "tooltip" : "Members of this species are born with a natural aptitude.",
            "cost" : 1
        },
        "Thrifty" : {
            "JobTradeValue" : 25,
            "tooltip": "Members of this species are instinctively economical and are always looking to make a good profit, whatever corners need cutting.",
            "cost" : 2
        },
        "Traditional" : {
            "JobUnityProduction" : 10,
            "Excludes" : ["Quarrelsome"],
            "tooltip" : "Certain aspects of this species' cognition makes it predisposed to especially value historical precedence and group unity.",
            "cost" : 1
        },
        "Decadent" : {
            "WorkerHapiness" : -10,
            "SlaveHapiness" : -10,
            "tooltip" : "This species believes that whenever there is hard work that needs doing, that work is always best done by somebody else.",
            "cost" : -1
        },
        "Deviants" : {
            "GoverningEthicsAttraction" : -15,
            "Excludes" : ["Conformists", "Hive-Minded"],
            "tooltip" : "These people are rebellious in natura nd constantly try to challenge the status-quo.",
            "cost" : -1
        },
        "Fleeting" : {
            "LeaderLifespan" : -10,
            "Excludes" : ["Venerable", "Enduring"],
            "tooltip" : "Time is fleeting for this species. What they lack in longevity, they make up in other ways.",
            "cost" : -1
        }
        "Nonadaptive" : {
            "Habitability" : -10
            "Excludes": ["Adaptive", "ExtremelyAdaptive", "Robust"]
            "tooltip" : "This species does not adapt well to foreign environments."
            "cost" : -2
        }
        "Quarrelsome": {
            "JobUnityProduction" : -10
            "Excludes" : "Traditional"
            "tooltip" : "While not inherently distrustful, members of this species are often socially combative."
            "cost" : -1
        }
        "Repugnant" : {
            "JobAmenityProduction" : -20
            "Excludes" : ["Charismatic"]
            "tooltip" : "The physical appearance and customs of this species are considered offensive to others and few appreciate them as neighbors."
            "cost" : -2
        }
        "Sedentary" : {
            "ImmigrationPopGrowth" : -15
            "ResettlementCost" : 25
            "Excludes" : ["Normadic"]
            "tooltip" : "This species has a sedentary past, and it's members are reluctant to migrate away from where they grew up."
            "cost" : -1
        }
        "SlowBreeders" : {
            "GrowthSpeed" : -10
            "Excludes" : ["RapidBreeders", "Fertile"]
            "tooltip" : "This species reproduces at a slow rate, lowering population growth."
            "cost" : -2
        }
        "SlowLearners" : {
            "LeaderExperienceGain" : -25
            "Excludes" : ["QuickLearners"]
            "tooltip" : "Members of this species are slow to learn from their experiences."
            "cost" : -1
        }
        "Solitary" : {
            "PopHousingUsage" : 10
            "Excludes" : ["Communal", "Nerve", "Stapled"]
            "tooltip" : "Members of this species tend to be solitary and territorial, often becoming agitated in crowded conditions."
            "cost" : -1
        }
        "Wasteful" : {
            "PopConsumerGoodsUpkeep" : 10
            "Excludes" : ["Conservationist", "Hive-Minded"]
            "tooltip" : "Members of this species seemingly have no concept of frugality and are prone to useless consumption."
            "cost" : -1
        }
        "Weak" : {
            "ArmyDamage" : -20
            "WorkerOutput" : -2
            "Excludes" : ["Strong", "VeryStrong"]
            "tooltip" : "Members of this species are physically weaker than average, making them poor fighters on the ground."
            "cost" : -1
        }
    }
    self.lithoidtraits = {
        "Lithoid" : {
            "PopGrowthSpeed" : -25
            "Habitability" : 50
            "ArmyHealth" : 50
            "LeaderLifeSpan" : 50
            "FoodIsMinerals" : True
            "tooltip" : "This species has silicon based biology, and consumes minerals rather than food. They are tougher than traditional organics, and have slower metabolisms, making them long lived but slow to reproduce."
        }
        "GaseousByproducts" : {
            "PopExoticGasProduction" : 0.01
            "Excludes" : ["ScintillatingSkin","VolatileExcretions"]
            "tooltip" : "The metabolic porcesses of this species cause regular venting of gases useful to industry."
        }
        "ScintillatingSkin" : {
            "PopRareCrystalProduction" : 0.01
            "Excludes" : ["GaseousByproducts", "VolatileExcretions"]
            "tooltip" : "The outermost layer of this species is studded with sparkling crystals and gemstones that ocasionally flake off."
        }
        "VolatileExcretions" : {
            "PopVolatileMoteProduction" : 0.01
            "Excludes" : ["GaseousByproducts", "ScintillatingSkin"-]
            "tooltip" : "The highly compressed spoor created by this species is unstable and contains an unbelievable amount of power."
        }
    }
    self.specialtraits = {
        "Uplifted": {
            "tooltip" : "This species was uplifted from a primitive origin, and it's members are happier when living on planets belonging to their benefactor."
        }
    }