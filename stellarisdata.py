class StellarisDataLibrary():
    def __init_(self):
        print("Stellaris Data Library Loaded")
        self.traits = {
            "Adapative" : {
                "Habitability" : 10,
                "Excludes" : ["ExtremlyAdaptive", "Nonadaptive", "Robust"],
                "tooltip" : "This species is highly adaptive when it comes to foreign environments.",
                "cost" : 2,
            },
            "ExtremlyAdaptive" : {
                "Habitability" : 20,
                "Excludes" : ["Adaptive", "Nonadaptive", "Robust"],
                "tooltip" : "This species is remarkably adept at adapting to any foreign environment.",
                "cost" : 4,
            },
            "Agarian" : {
                "JobFoodProduction" : 15,
                "tooltip" : "This species has a deep connection to the land and make expert farmers and gardeners.",
                "cost" : 2,
            },
            "Charismatic" : {
                "JobAmenityProduction": 20,
                "Excludes" : ["Repugnant"],
                "tooltip" : "Members of this species have a special charisma and are generally considered pleasant to be around.",
                "cost" : 2,
            },
            "Communal" : {
                "PopHousingUsage" : -10,
                "Excludes" : ["Solitary", "Nerve", "Stapled"],
                "tooltip" : "Members of this species are highly communal and quite used to living in close proximity to others.",
                "cost" : 1,
            },
            "Conformists" : {
                "GoverningEthicsAttraction" : 30,
                "Excludes" : ["Deviants", "Hive-Minded"],
                "tooltip" : "These people always seek consensus and are more likely to conform to the government ethics.",
                "cost" : 2,
            },
            "Conservationist" : {
                "PopConsumerGoodsUpkeep" : -10,
                "Excludes" : ["Wasteful", "Hive-Minded"],
                "tooltip" : "Members of this species believes that resources must be conserved and recycled.",
                "cost" : 1,
            },
            "Enduring" : {
                "LeaderLifeSpan" : 20,
                "Excludes" : ["Venerable", "Fleeting"],
                "tooltip" : "Lifespans in this species are unusually long.",
                "cost" : 1,
            },
            "Venerable" : {
                "LeaderLifeSpan" : 80,
                "Excludes" : ["Enduring", "Fleeting"],
                "tooltip" : "This species can grow to an age that commands dignity and respect.",
                "cost" : 4,
            },
            "Industrious" : {
                "JobMineralProduction" : 15,
                "tooltip" : "Members of this species are known for their diligence and hard-working nature, always going above and beyond.",
                "cost" : 2,
            },
            "Ingenious" : {
                "JobEnergyProduction" : 15,
                "tooltip" : "Members of this species are good at 'thinking outside the box' and know how to maximize the efficiency of their infrastructure and power grids.",
                "cost" : 2,
            },
            "Intelligent": {
                "JobEngineeringResearchProduction" : 10,
                "JobPhysicsResearchProduction" : 10,
                "JobSocietyResearchProduction" : 10,
                "Excludes" : ["Erudite","Nerve","Stapled","Uplifted(EnigmaticCache)","SomewhatUplifted"],
                "tooltip" : "This species is highly intelligent and enjoys fast technological progress.",
                "cost" : 2,
            },
            "NaturalEngineers" : {
                "JobEngineeringResearchProduction" : 15,
                "Excludes" : ["NaturalPhysicists", "NaturalSociologists","Nerve","Stapled"],
                "tooltip" : "Members of this species have a natural inclination towards engineering and the material sciences.",
                "cost" : 1,
            },
            "NaturalPhysicists" : {
                "JobPhysicsResearchProduction" : 15,
                "Exlcudes" : ["NaturalEngineers","NaturalSociologists","Nerve","Stapled"],
                "tooltip" : "Members of this species have a natural inclination towards theoretical physics and astral phenomena.",
                "cost" : 1,
            },
            "NaturalSociologists" : {
                "JobSocietyResearchProduction" : 15,
                "Exlcudes" : ["NaturalEngineers","NaturalPhysicists","Nerve","Stapled"],
                "tooltip" : "Members of this species have a natural inclination towards sociology and biological studies.",
                "cost" : 1,
            },
            "Nomadic" : {
                "ImmigrationPopGrowth" : 15,
                "ResettlementCost" : -25,
                "Excludes" : ["Sedentary"],
                "tooltip" : "This species has a nomadic past, and it's members often think nothing when relocating to another world.",
                "cost" : 1,
            },
            "QuickLearners" : {
                "LeaderExperienceGain" : 25,
                "Excludes" : ["SlowLearners"],
                "tooltip" : "Members of this species are quick to learn from experiences.",
                "cost" : 1,
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
                "cost" : -1,
            },
            "Nonadaptive" : {
                "Habitability" : -10,
                "Excludes": ["Adaptive", "ExtremelyAdaptive", "Robust"],
                "tooltip" : "This species does not adapt well to foreign environments.",
                "cost" : -2,
            },
            "Quarrelsome": {
                "JobUnityProduction" : -10,
                "Excludes" : "Traditional",
                "tooltip" : "While not inherently distrustful, members of this species are often socially combative.",
                "cost" : -1,
            },
            "Repugnant" : {
                "JobAmenityProduction" : -20,
                "Excludes" : ["Charismatic"],
                "tooltip" : "The physical appearance and customs of this species are considered offensive to others and few appreciate them as neighbors.",
                "cost" : -2,
            },
            "Sedentary" : {
                "ImmigrationPopGrowth" : -15,
                "ResettlementCost" : 25,
                "Excludes" : ["Normadic"],
                "tooltip" : "This species has a sedentary past, and it's members are reluctant to migrate away from where they grew up.",
                "cost" : -1,
            },
            "SlowBreeders" : {
                "GrowthSpeed" : -10,
                "Excludes" : ["RapidBreeders", "Fertile"],
                "tooltip" : "This species reproduces at a slow rate, lowering population growth.",
                "cost" : -2,
            },
            "SlowLearners" : {
                "LeaderExperienceGain" : -25,
                "Excludes" : ["QuickLearners"],
                "tooltip" : "Members of this species are slow to learn from their experiences.",
                "cost" : -1,
            },
            "Solitary" : {
                "PopHousingUsage" : 10,
                "Excludes" : ["Communal", "Nerve", "Stapled"],
                "tooltip" : "Members of this species tend to be solitary and territorial, often becoming agitated in crowded conditions.",
                "cost" : -1,
            },
            "Wasteful" : {
                "PopConsumerGoodsUpkeep" : 10,
                "Excludes" : ["Conservationist", "Hive-Minded"],
                "tooltip" : "Members of this species seemingly have no concept of frugality and are prone to useless consumption.",
                "cost" : -1,
            },
            "Weak" : {
                "ArmyDamage" : -20,
                "WorkerOutput" : -2,
                "Excludes" : ["Strong", "VeryStrong"],
                "tooltip" : "Members of this species are physically weaker than average, making them poor fighters on the ground.",
                "cost" : -1,
            },
        }
        self.lithoidtraits = {
            "Lithoid" : {
                "PopGrowthSpeed" : -25,
                "Habitability" : 50,
                "ArmyHealth" : 50,
                "LeaderLifeSpan" : 50,
                "FoodIsMinerals" : True,
                "tooltip" : "This species has silicon based biology, and consumes minerals rather than food. They are tougher than traditional organics, and have slower metabolisms, making them long lived but slow to reproduce.",
                "cost" : 0,
            },
            "GaseousByproducts" : {
                "PopExoticGasProduction" : 0.01,
                "Excludes" : ["ScintillatingSkin","VolatileExcretions"],
                "tooltip" : "The metabolic porcesses of this species cause regular venting of gases useful to industry.",
                "cost" : 2,
            },
            "ScintillatingSkin" : {
                "PopRareCrystalProduction" : 0.01,
                "Excludes" : ["GaseousByproducts", "VolatileExcretions"],
                "tooltip" : "The outermost layer of this species is studded with sparkling crystals and gemstones that ocasionally flake off.",
                "cost" : 2,
            },
            "VolatileExcretions" : {
                "PopVolatileMoteProduction" : 0.01,
                "Excludes" : ["GaseousByproducts", "ScintillatingSkin"],
                "tooltip" : "The highly compressed spoor created by this species is unstable and contains an unbelievable amount of power.",
                "cost" : 2,
            },
        }
        self.specialtraits = {
            "Uplifted": {
                "tooltip" : "This species was uplifted from a primitive origin, and it's members are happier when living on planets belonging to their benefactor.",
                "cost" : 0,
                "req" : ["Epigenetic Triggers"],
            },
            "Self-Modified" : {
                "tooltip" : "Members of this offshoot species have spontaneously altered their genetic makeup to give themselves an advantage.",
                "cost" : 0,
                "req" : ["A New Species event"],
            },
            "Bioadaptability" : {
                "Habitability" : 5,
                "tooltip" : "This species has been modified to be slightly more adaptive and can now better endure harsh climates.",
                "req" : ["Speed Demon - Green Solution"],
                "cost" : 0,
            },
            "Limited Regeneration" : {
                "ArmyDamage" : 10,
                "LeaderLifeSpan" : 10,
                "tooltip" : "This species has been modified to heal faster, making them more dangeorus in battle and somewhat longer-lived in general.",
                "cost" : 0,
                "req" : ["Speed Demon - Blue Solution"],
            },
            "Social Pheromones" : {
                "PopHousingUsage" : -5,
                "tooltip" : "This species has been modified to be more social and accepting of crowded conditions.",
                "cost" : 0,
                "req" : ["Speed Demon - Red Solution"],
            },
            "Cybernetic" : {
                "ArmyDamage" : 10,
                "Habitability" : 20,
                "LeaderLifeSpan" : 40,
                "cost" : 0,
                "tooltip" : "This species has embraced cybernetics on such a scale that its members may be considered cyborgs. They routinely replace their organic body parts with more advanced mechanical versions.",
                "req" : ["The Flesh Is Weak", "Driven Assimiliator","Fallen Empire - Keepers of Knowledge"],
            },
            "Psionic" : {
                "JobEnergyProduction" : 10,
                "ResearchOutput" : 10,
                "Happiness" : 5,
                "tooltip" : "All members of this species possess powerful psionic abilities. They typically communicate with each other through telepathy.",
                "cost" : 0,
                "req" : ["Mind Over Matter","DLC-Utopia"],
            },
            "Serviles" : {
                "req" : ["Syncretic Species", "DLC-Utopia"],
                "Happiness" : 10,
                "JobResourceProduction" : 10,
                "EmployRulerSpecialist" : False,
                "EmployLeader" : False,
                "tooltip" : "This species evolved alongside a second, more advanced species. Never particulary intelligent to begin with, selective breeding forphysical prowess and docility has reduced them to servile proles.",
                "cost" : 1,
                "Excludes" : ["Intelligent", "Erudite", "Natural Physicists", "Natural Sociologists", "Natural Engineers"],
            },
            "Hive-Minded" : {
                "NoHappiness" : True,
                "req" : ["Hive-Mind","DLC-Utopia"],
                "cost" : 0,
                "tooltip" : "This species is made up of semi-autonomous individuals slaved to a single, unfathomably vast consciousness.",
            },
            "Survivor" : {
                "LeaderLifeSpan" : 10,
                "TombworldHabitability" : 70,
                "req" : ["Post-Apocalyptic Species", "DLC-Apocalypse"],
                "cost" : 0,
                "tooltip" : "This species has survived the horrors of a nuclear apocalypse. Their capacity for thriving in the most inhospitable circumstances should not be understimated.",
            },
            "Docile Livestock" : {
                "PopGrowthSpeed" : 30,
                "JobEnergyProduction" : -50,
                "JobUnityProduction" : 10,
                "JobEngineeringResearchProduction" : -75,
                "JobPhysicsResearchProduction" : -75,
                "JobSocietyResearchProduction" : -75,
                "EmployRulerSpecialist" : False,
                "EmployLeader" : False,
                "NoHappiness" : True,
                "req" : ["Wild Eukaryotes Event Species", "DLC-Distant Stars"],
                "cost" : 1,
                "Excludes" : ["Intelligent", "Erudite", "Natural Physicists", "Natural Sociologists","Natural Engineers"],
                "tooltip" : "Docile and delicious, this species has had its higher brain functions genetically altered to create a kind of harmless livestock that can care for itself, without the pesky need for social interaction or self-determination.",
            },
            

        },