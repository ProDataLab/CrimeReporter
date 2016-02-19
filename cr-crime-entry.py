import xml.etree.ElementTree as et
import datetime
import sys, os



class CrimeReporter(object):
    
    def __init__(self):
        self.filepath = os.curdir + '/crime-reporter.xml'
        self.tree = None
        self.root = None
        self.crime = None

    
    def end_program(self):
        if self.tree:
            self.tree.write(self.filepath, encoding='UTF-8')
        sys.exit()
        
        
    def getDB(self):
        if os.path.exists(self.filepath):
            self.tree = et.parse(self.filepath)
            self.root = self.tree.getroot()
        else:
            self.root = et.Element('Crimes')
            self.tree = et.ElementTree(self.root)


    def run(self):
        next = False
        proceed = ''
        self.getDB()

        while len(proceed) == 0:
            print ''
            proceed = raw_input("Welcome to the Crime Reporter database. Would like to enter a crime [Y/N]: ").upper()
            if proceed == 'Y':
                pass
            elif proceed == 'N':
                self.end_program()
            else:
                print 'Please enter Y for YES or N for NO'
                proceed == ''
                continue
        
            proceed = ''
        
            while not next:

                print ''
                q1 = raw_input("What type of crime are you reporting?\n  Please select [A/B/C] A) Auto Theft B) Vandelism C) Assault: ").upper()
                
                self.crime = et.SubElement(self.root, 'Crime')
                
                self.crime.set('datetime', datetime.datetime.now().strftime("%d/%m/%y %H:%M"))

                
                if q1 == 'A':
                    self.crime.set('type', 'Auto Theft')
                    next = True
                elif q1 == 'B':
                    self.crime.set('type', 'Vandelism')
                    next = True
                elif q1 == 'C':
                    self.crime.set('type', 'Assault')
                    next = True
                else:
                    print "Please enter A or B or C"
                    print ""
            
            next = False
            
            if self.crime.attrib['type'] == 'Auto Theft':
                owner_name = et.SubElement(self.crime, "owner_name")
                owner_name.text = raw_input("What is the name of the vehicle owner: ")
                
                vehicle_make = et.SubElement(self.crime, 'vehicle_make')
                vehicle_make.text = raw_input("What is the vehicle make: ")
                
                vehicle_model = et.SubElement(self.crime, 'vehicle_model')
                vehicle_model.text = raw_input("What is the vehicle model: ")
                
                vehicle_year = et.SubElement(self.crime, 'vehicle_year')
                vehicle_year.text = raw_input("What year was the vehicle made: ")
                
                vehicle_color = et.SubElement(self.crime, 'vehicle_color')
                vehicle_color.text = raw_input("What is the color of the vehicle: ")
                
                location = et.SubElement(self.crime, 'location')
                location.text = raw_input("What was the last location of the vehicle: ")
                
                witness = et.SubElement(self.crime, 'witness')
                witness = raw_input("Name of witness (leave blank for none): ")
                
                
            elif self.crime.attrib['type'] == 'Vandelism':
                property_type = et.SubElement(self.crime, 'property_type')
                property_type.text = raw_input("What type of property was vandelized: ")
                
                description = et.SubElement(self.crime, 'description')
                description.text = raw_input("Describe the damage: ")
                
                estimated_cost = et.SubElement(self.crime, 'estimated_cost')
                estimated_cost.text = raw_input("What is the estimated cost of damage: ")
                
                witness_name = et.SubElement(self.crime, 'witness_name')
                witness_name.text = raw_input("Name of witness (leave blank for none): ")
                
                
                
                
            elif self.crime.attrib['type'] == 'Assault':
                victim_name = et.SubElement(self.crime, 'victim_name')
                victim_name.text = raw_input("What is the name of the victim: ")
                
                assailant_name = et.SubElement(self.crime, 'assailant_name')
                assailant_name.text = raw_input("What is the name of the assailant: ")
                
                injury = et.SubElement(self.crime, 'injury')
                injury.text = raw_input("Describe the injury: ")
                
                weapon = et.SubElement(self.crime, 'weapon') 

                weapon.text = raw_input('What type of weapon was used: ')
                
                





if __name__ == '__main__':
    
    cr = CrimeReporter()
    cr.run()

























