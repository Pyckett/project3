from binary_search_tree import BinarySearchTree, Node
import csv

class PatientRecord:

    def __init__(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature

    def __str__(self):
        return (f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}, BP: {self.blood_pressure}, Pulse: {self.pulse}, Temp: {self.body_temperature}")

class PatientRecordManagementSystem:

    def __init__(self):
        self.bst = BinarySearchTree()

    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        record = PatientRecord(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
        node = Node(patient_id, record)
        self.bst.insert(node)

    def search_patient_record(self, patient_id):
        return self.bst.search(patient_id)

    def delete_patient_record(self, patient_id):
        self.bst.remove(patient_id)

    def display_all_records(self):
        print("Patient Records:")
        for key, record in self.bst.inorder_traversal(self.bst.root): # for every patient in our tree print the info using in-order traversal
            print(record) # calls PatientRecord __str__()

    def build_tree_from_csv(self, file_path):
        pass

    def visualize_tree(self):
        pass

    def _add_nodes(self, dot, node):
        pass