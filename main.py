from enum import Enum

class StaffRole(Enum):
    MANAGER = 'Manager'
    RECEPTIONIST = 'Receptionist'
    HYGIENTIST = 'Hygienist'
    DENTIST = 'Dentist'

class ServiceType(Enum):
    CLEANING = 'Cleaning'
    IMPLANTS = 'Implants'
    CROWNS = 'Crowns'
    FILLINGS = 'Fillings'

class DentalBranch:
    def __init__(self, address, phone, manager):
        self.address = address
        self.phone = phone
        self.manager = manager
        self.staffList = []
        self.serviceList = []
    
    # Setters and Getters 
    def getAddress(self):
        return self._address

    def setAddress(self, value):
        self._address = value

    def getPhone(self):
        return self._phone

    def setPhone(self, value):
        self._phone = value

    def getManager(self):
        return self._manager

    def setManager(self, value):
        self._manager = value
    
    # Behaviors
    def addStaff(self, staff):
        self.staffList.append(staff)

    def addService(self, service):
        self.serviceList.append(service)

    def bookAppointment(self, patient, service):
        appointment = Appointment(patient, service)
        # Logic to schedule appointment
        print(f"Appointment scheduled for {patient.firstName} {patient.lastName} for {service.name.value}.")

    def checkout(self, patient):
        bill = 0
        for appointment in patient.appointmentList:
            bill += appointment.service.cost
        vat = VAT.apply_vat(bill)
        total = bill + vat
        receipt = f"Total bill: {bill}, VAT: {vat}, Total: {total}"
        print(receipt)


class Staff:
    def __init__(self, firstName, lastName, id, role):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.role = role
    
    # Setters and getters
    def getFirstName(self):
        return self._firstName

    def setFirstName(self, value):
        self._firstName = value

    def getLastName(self):
        return self._lastName

    def setLastName(self, value):
        self._lastName = value

    def getId(self):
        return self._id

    def setId(self, value):
        self._id = value

    def getRole(self):
        return self._role

    def setRole(self, value):
        self._role = value

    # Behavior
    def performTask(self, task):
        print(f"{self.role} {self.firstName} {self.lastName} performing {task.name.value}.")


class Manager(Staff):
    pass


class Receptionist(Staff):
    pass


class Hygienist(Staff):
    pass


class Dentist(Staff):
    pass


class Service:
    def __init__(self, name, cost, duration):
        self.name = name
        self.cost = cost
        self.duration = duration
    
    # Setters and Getters
    def getName(self):
        return self._name

    def setName(self, value):
        self._name = value

    def getCost(self):
        return self._cost

    def setCost(self, value):
        self._cost = value

    def getDuration(self):
        return self._duration

    def setDuration(self, value):
        self._duration = value

    
    # Behaviors
    def add_service(self, service):
        # Logic to add service
        pass

    def remove_service(self, service):
        # Logic to remove service
        pass


class Cleaning(Service):
    pass


class Implants(Service):
    pass


class Crowns(Service):
    pass


class Fillings(Service):
    pass


class Patient:
    def __init__(self, firstName, lastName, id):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.appointmentList = []

    # Setters and Getters
    def setFirstName(self, firstName):
        self._firstName = firstName
    
    def getFirstName(self):
        return self._firstName
    
    def setLastName(self, lastName):
        self._lastName = lastName
    
    def getLastName(self):
        return self._lastName
    
    def setId(self, id):
        self._id = id
    
    def getId(self):
        return self._id
  
    def getAppointments(self):
        return self._appointmentList
    
    # Behavior
    def bookAppointment(self, branch, service):
        branch.bookAppointment(self, service)
        appointment = Appointment(self, service)
        self.appointmentList.append(appointment)


class Appointment:
    def __init__(self, patient, service):
        self.patient = patient
        self.service = service
    
     # Setters and Getters
    def setPatient(self, patient):
        self._patient = patient

    def getPatient(self):
        return self._patient

    def setService(self, service):
        self._service = service
    
    def getService(self):
        return self._service


class VAT:
    @staticmethod
    def apply_vat(bill):
        vatRate = 0.05
        vat = bill * vatRate
        return vat
    

# Test cases

# Create a dental branch and add staff, services, and patients
manager = Manager("Arthur", "Diniz", 1, StaffRole.MANAGER)
branch = DentalBranch("123 Main Street", "555-1234", manager)
receptionist = Receptionist("Shanzila", "Ahmed", 2, StaffRole.RECEPTIONIST)
hygienist = Hygienist("Sohazur", "Islam", 3, StaffRole.HYGIENTIST)
dentist = Dentist("Sohibjon", "Avgonov", 4, StaffRole.DENTIST)
branch.addStaff(manager)
branch.addStaff(receptionist)
branch.addStaff(hygienist)
branch.addStaff(dentist)
cleaning = Cleaning(ServiceType.CLEANING, 50.0, 30)
branch.addService(cleaning)
branch.addService(Implants(ServiceType.IMPLANTS, 1000.0, 120))
branch.addService(Crowns(ServiceType.CROWNS, 500.0, 90))
branch.addService(Fillings(ServiceType.FILLINGS, 75.0, 45))
patient1 = Patient("Will", "Smith", 101)
patient2 = Patient("Michael", "Jackson", 102)

# Test booking an appointment for a patient
patient1.bookAppointment(branch, cleaning)
assert len(patient1.appointmentList) == 1
assert patient1.appointmentList[0].service.name == ServiceType.CLEANING
assert patient1.appointmentList[0].service.cost == 50.0

# Test adding a new service to the branch
rootCanal = Service("Root Canal", 750.0, 90)
branch.addService(rootCanal)
assert len(branch.serviceList) == 5
assert branch.serviceList[-1].name == "Root Canal"
assert branch.serviceList[-1].cost == 750.0

# Test adding a new staff member to the branch
receptionist2 = Receptionist("Alicia", "Keys", 5, StaffRole.RECEPTIONIST)
branch.addStaff(receptionist2)
assert len(branch.staffList) == 5
assert branch.staffList[-1].firstName == "Alicia"
assert branch.staffList[-1].lastName == "Keys"
assert branch.staffList[-1].role == StaffRole.RECEPTIONIST

# Test booking multiple appointments for a patient
patient2.bookAppointment(branch, Crowns(ServiceType.CROWNS, 500.0, 90))
patient2.bookAppointment(branch, Fillings(ServiceType.FILLINGS, 75.0, 45))
assert len(patient2.appointmentList) == 2
assert patient2.appointmentList[0].service.name == ServiceType.CROWNS
assert patient2.appointmentList[0].service.cost == 500.0
assert patient2.appointmentList[1].service.name == ServiceType.FILLINGS
assert patient2.appointmentList[1].service.cost == 75.0

# Test checking out a patient
branch.checkout(patient1)
branch.checkout(patient2)
# Output:
# Appointment scheduled for Will Smith for Cleaning.
# Appointment scheduled for Michael Jackson for Crowns.
# Appointment scheduled for Michael Jackson for Fillings.
# Total bill: 50.0, VAT: 2.5, Total: 52.5
# Total bill: 575.0, VAT: 28.75, Total: 603.75