from django.db import models


# Create your models here.
class Main(models.Model):
    RegisterNumber = models.CharField(max_length = 12, primary_key = True,unique = True )
    Name = models.CharField(max_length=50)
    
class Sem1(models.Model):

    id = models.ForeignKey(Main, primary_key = True, on_delete = models.CASCADE)
    grade = [('O','O'),('A+','A+'),('A','A'),('B+','B+'),('B','B'),('RA','Arrear')]
    EngineeringPhysics = models.CharField(max_length= 2, choices= grade)
    EngineeringMathematics = models.CharField(max_length= 2, choices= grade)
    EngineeringChemistry = models.CharField(max_length= 2, choices= grade)
    EngineeringGraphics = models.CharField(max_length= 2, choices= grade)
    CommunicativeEnglish = models.CharField(max_length= 2, choices= grade)
    ProgramSolvingAndPythonProgramming = models.CharField(max_length= 2, choices= grade)
    ProgramSolvingAndPythonProgrammingLaboratory = models.CharField(max_length= 2, choices= grade)
    PhysicsandChemistryLaboratory = models.CharField(max_length= 2, choices= grade)
    def __str__(self):
        return f"EngineeringPhysics:{self.EngineeringPhysics},EngineeringMathematics:{self.EngineeringMathematics},EngineeringChemistry:{self.EngineeringChemistry},"

class Sem2(models.Model):

    id = models.ForeignKey(Main, primary_key = True, on_delete = models.CASCADE)
    grade = [('O','O'),('A+','A+'),('A','A'),('B+','B+'),('B','B'),('RA','Arrear')]
    TechnicalEnglish = models.CharField(max_length= 2, choices= grade )
    EngineeringMathematicsII = models.CharField(max_length= 2, choices= grade)
    MaterialsScience = models.CharField(max_length= 2, choices= grade)
    BasicElectricalElectronicsandInstrumentationEngineering = models.CharField(max_length= 2, choices= grade)
    EnvironmentalScienceandEngineering = models.CharField(max_length= 2, choices= grade)
    EngineeringMechanics = models.CharField(max_length= 2, choices= grade)
    EngineeringPracticesLaboratory = models.CharField(max_length= 2, choices= grade)
    BasicElectricalElectronicsandInstrumentationEngineering = models.CharField(max_length= 2, choices= grade)
    BasicElectricalElectronicsandInstrumentationEngineeringLaboratory = models.CharField(max_length= 2, choices= grade)

class Sem3(models.Model):

    id = models.ForeignKey(Main, primary_key = True, on_delete = models.CASCADE)
    grade = [('O','O'),('A+','A+'),('A','A'),('B+','B+'),('B','B'),('RA','Arrear')]
    TransformsandPartialDifferentialEquations = models.CharField(max_length= 2, choices= grade)
    EngineeringThermodynamics = models.CharField(max_length= 2, choices= grade)
    FluidMechanicsandMachinery = models.CharField(max_length= 2, choices= grade)
    ManufacturingTechnologyI = models.CharField(max_length= 2, choices= grade)
    ElectricalDrivesandControls = models.CharField(max_length= 2, choices= grade)
    ManufacturingTechnologyLaboratoryI = models.CharField(max_length= 2, choices= grade)
    ComputerAidedMachineDrawing = models.CharField(max_length= 2, choices= grade)
    ElectricalEngineeringLaboratory = models.CharField(max_length= 2, choices= grade)
    InterpersonalSkillsListeningSpeaking = models.CharField(max_length= 2, choices= grade)

class Sem4(models.Model):

    id = models.ForeignKey(Main, primary_key = True, on_delete = models.CASCADE)
    grade = [('O','O'),('A+','A+'),('A','A'),('B+','B+'),('B','B'),('RA','Arrear')]
    StatisticsandNumericalMethods = models.CharField(max_length= 2, choices= grade )
    KinematicsofMachinery = models.CharField(max_length= 2, choices= grade)
    ManufacturingTechnologyII = models.CharField(max_length= 2, choices= grade)
    EngineeringMetallurgy = models.CharField(max_length= 2, choices= grade)
    StrengthofMaterialsforMechanicalEngineers = models.CharField(max_length= 2, choices= grade)
    ThermalEngineeringI = models.CharField(max_length= 2, choices= grade)
    ManufacturingTechnologyLaboratoryII = models.CharField(max_length= 2, choices= grade)
    StrengthofMaterialsandFluidMechanicsandMachineryLaboratory = models.CharField(max_length= 2, choices= grade)
    AdvancedReadingandWriting = models.CharField(max_length= 2, choices= grade)
class Sem5(models.Model):

    id = models.ForeignKey(Main, primary_key = True, on_delete = models.CASCADE)
    grade = [('O','O'),('A+','A+'),('A','A'),('B+','B+'),('B','B'),('RA','Arrear')]
    ThermalEngineeringII = models.CharField(max_length= 2, choices= grade )
    DesignofMachineElements = models.CharField(max_length= 2, choices= grade)
    MetrologyandMeasurements = models.CharField(max_length= 2, choices= grade)
    DynamicsofMachines = models.CharField(max_length= 2, choices= grade)
    OpenElectiveI = models.CharField(max_length= 2, choices= grade)
    KinematicsandDynamicsLaboratory = models.CharField(max_length= 2, choices= grade)
    ThermalEngineeringLaboratory = models.CharField(max_length= 2, choices= grade )
    MetrologyandMeasurementsLaboratory = models.CharField(max_length= 2, choices= grade )

class Sem6(models.Model):

    id = models.ForeignKey(Main, primary_key = True, on_delete = models.CASCADE)
    grade = [('O','O'),('A+','A+'),('A','A'),('B+','B+'),('B','B'),('RA','Arrear')]
    DesignofTransmissionSystems = models.CharField(max_length= 2, choices= grade )
    ComputerAidedDesignandManufacturing = models.CharField(max_length= 2, choices= grade)
    HeatandMassTransfer = models.CharField(max_length= 2, choices= grade)
    FiniteElementAnalysis = models.CharField(max_length= 2, choices= grade)
    HydraulicsandPneumatics = models.CharField(max_length= 2, choices= grade)
    ProfessionalElectiveI = models.CharField(max_length= 2, choices= grade)
    CADCAMLaboratory = models.CharField(max_length= 2, choices= grade)
    DesignandFabricationProject = models.CharField(max_length= 2, choices= grade)
    ProfessionalCommunication = models.CharField(max_length= 2, choices= grade )
class Sem7(models.Model):

    id = models.ForeignKey(Main, primary_key = True, on_delete = models.CASCADE)
    grade = [('O','O'),('A+','A+'),('A','A'),('B+','B+'),('B','B'),('RA','Arrear')]
    PowerPlantEngineering = models.CharField(max_length= 2, choices= grade )
    ProcessPlanningandCostEstimation = models.CharField(max_length= 2, choices= grade)
    Mechatronics = models.CharField(max_length= 2, choices= grade)
    OpenElectiveII = models.CharField(max_length= 2, choices= grade)
    ProfessionalElectiveII = models.CharField(max_length= 2, choices= grade)
    ProfessionalElectiveIII = models.CharField(max_length= 2, choices= grade)
    SimulationandAnalysisLaboratory = models.CharField(max_length= 2, choices= grade)
    MechatronicsLaboratory = models.CharField(max_length= 2, choices= grade)
    TechnicalSeminar = models.CharField(max_length= 2, choices= grade)

class Sem8(models.Model):

    id = models.ForeignKey(Main, primary_key = True, on_delete = models.CASCADE)
    grade = [('O','O'),('A+','A+'),('A','A'),('B+','B+'),('B','B'),('RA','Arrear')]
    PrinciplesofManagement = models.CharField(max_length= 2, choices= grade )
    ProfessionalElectiveIV = models.CharField(max_length= 2, choices= grade)
    ProjectWork = models.CharField(max_length= 2, choices= grade)
