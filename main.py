class DentalBranch:
    def __init__(self, address, phone, manager):
        self.address = address
        self.phone = phone
        self.manager = manager
        self.staffList = []
        self.serviceList = []

    def addStaff(self, staff):
        self.staffList.append(staff)

    def addService(self, service):
        self.serviceList.append(service)

    def bookAppointment(self, patient, service):
        appointment = Appointment(patient, service)
        # Logic to schedule appointment
        print(f"Appointment scheduled for {patient.firstName} {patient.lastName} for {service.name}.")

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

    def perform_task(self, task):
        print(f"{self.role} {self.firstName} {self.lastName} performing {task}.")


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

    def bookAppointment(self, branch, service):
        branch.bookAppointment(self, service)
        appointment = Appointment(self, service)
        self.appointmentList.append(appointment)


class Appointment:
    def __init__(self, patient, service):
        self.patient = patient
        self.service = service


class VAT:
    @staticmethod
    def apply_vat(bill):
        vatRate = 0.05
        vat = bill * vatRate
        return vat