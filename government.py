import math
class StellarisDataLibraryGov():
    def __init_(self):
        print("Stellaris Data Library.Gov Loaded")
        self.Democratic = {
            "Election" : "Democratic",
            "RulerTerm" : 10,
            "Changeable" : True,
            "Effects" : ["RulerMandates", "Re-Election"],
            "Excludes" : ["Authoritarian","Fanatic-Authoritarian", "Gestalt-Consciousness"],
            "tooltip" : "Democratic governments have regular elections where all citizens can vote on who should represent them."
        },
        self.Oligarchic = {
            "Election" : "Oligarchic",
            "RulerTerm" : 20,
            "Changeable" : True,
            "Effects" : ["RulerAgendas", "EmergencyElections-250Influence"],
            "Excludes" : ["Fanatic-Authoritarian", "Fanatic-Egalitarian", "Gestalt-Consciousness"],
            "tooltip" : "Oligarchic governments are ruled by a small gorup of individuals that hold all political power."
        },
        self.Dictatorial = {
            "Election" : "Oligarchic",
            "RulerTerm" : "Life",
            "Changeable" : True,
            "Effects" : ["RulerAgendas"],
            "Excludes" : ["Egalitarian", "Fanatic-Egalitarian", "Gestalt-Consciousness"],
            "tooltip" : "Dictorial governments are ruled by a single individual for life that wields absolute control over the state."
        },
        self.Imperial = {
            "Election" : "Hereditary",
            "RulerTerm" : "Life",
            "Changeable" : True,
            "Effects" : ["RulerAgendas"],
            "Excludes" : ["Egalitarian", "Fanatic-Egalitarian", "Gestalt-Consciousness"],
            "tooltip" : "Imperial governments are similiar to dictatorial ones, except that the throne is always inherited by a designated successor upon the ruler's death.",
        },
        self.HiveMind = {
            "Election" : "No",
            "RulerTerm" : "Permanent",
            "Changeable" : False,
            "Effects" : ["NoRobots", "PopGrowthSpeed+25", "UniqueCivics"],
            "Excludes" : ["Gestalt-Consciousness"],
            "req" : ["DLC-Utopia"],
            "tooltip" : "Hive Minds operate as a single organism more than as a stte. The population has no free will, and act as an extension of the Hive Mind itself - much like the limbs of a body. When cut off from the Mind, these drones become comatose and eventually wither and die. Any free individuals on planets owned by the Mind are driven away, killed, or simply treated as prey to feed the collective.",
        },
        self.MachineIntelligence = {
            "Election" : "No",
            "RulerTerm" : "Permanent",
            "Changeable" : False,
            "Effects" : ["ExtraPopsOnNewColony+1", "MiningStationOutput+10", "UniqueCivics", "SpeciesGroupMustBeMachine"],
            "Excludes" : ["Gestalt-Consciousness"],
            "req" : ["DLC-SyntheticDawn"],
            "tooltip" : "Machine Intelligences are immense artificial group minds that have been networked into a single conscious entity. Most of the actual 'population' in such an empire consists of mindless work units who preform their designated tasks without any semblance of free will. A small number of semi-autonomous agents are typically employed for more specialized tasks that benefit from some degree of independent initiative.",
        },
        self.Corporate = {
            "Election" : "Oligarchic",
            "RulerTerm" : 20,
            "Changeable" : True,
            "Effects" : ["RulerAgendas", "EmergencyElections-250Influence", "AdministrativeCapacity+20", "EmpireSprawlPenalty+50%", "UniqueCivics"],
            "Excludes" : ["Fanatic-Authoritarian", "Fanatic-Egalitarian", "Gestalt-Consciousness"],
            "req" : ["DLC-MegaCorp"],
            "tooltip" : "Corporate governments are organized as a massive commercial enteprrise that has completely supplanted the role of the state."
        }