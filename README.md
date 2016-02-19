Introduction
============

Crime Reporter consists of two programs to demonstrate the usage of the XML data and file format (version 1.0) to both store and transfer data amongst the programs. According to Wikipedia[1], XML is what is called a markup language[2] that defines a set of rules for encoding documents in a format that is both human readable and machine readable. It is an open standard[3] defined by a specification[4] from a W3C commitee[5].


Program Description
===================

The two programs are written in the Python[6] programming language and use the built-in XML DOM library called 'etree'[7]. The first program is called 'cr-crime-entry.py' and is a data entry system using a command line interface to ask the user a series of questions that aid in entering a crime and its details. This data is stored into XML format and written to a file called 'crime-reporter.xml'. The second program is called 'cr-report-generator.py'. It utilizes the XML data stored from 'crime-entry.py' to generate a simple report of all crime data that has been entered and stored. The programs can be run from the command terminal using the command 'python cr-crime-entry.py' or 'python cr-report-generator.py'


Program Functionality
=====================

Here, presented first, is a snippet showing the interface of the crime-entry program that the user will encounter:

::

    Welcome to the Crime Reporter database. Would like to enter a crime [Y/N]: Y

    What type of crime are you reporting?
      Please select [A/B/C] A) Auto Theft B) Vandelism C) Assault: B
    What type of property was vandelized: Automobile
    Describe the damage: Broken Windshield
    What is the estimated cost of damage: 500.00
    Name of witness (leave blank for none): Jane Austin

This will produce an XML file called 'crime-reporter.xml'

:: 

    <?xml version='1.0' encoding='UTF-8'?>
    <Crimes>
      <Crime datetime="19/02/16 07:51" type="Vandelism">
        <property_type>Automobile</property_type>
        <description>Broken windshield</description>
        <estimated_cost>500.00</estimated_cost>
        <witness_name>Jane Austin</witness_name>
      </Crime>
    </Crimes>

The cr-crime-entry.py program can be continued to enter more crimes which will produce a list of crimes. When, finished the user can exit the system at which time the information will be written the the xml file.

::

    Welcome to the Crime Reporter database. Would like to enter a crime [Y/N]: N
    

A user can then generate a report to the command line, by calling 'python cr-report-generator.py' on the command line. This report utilizes the information entered into 'cr-crime-entry' and stored in 'crime-reporter.xml'.

:: 

    ############################################
    Date: 19/02/16 07:51
    Type: Vandelism
        property_type: Automobile
        description: Broken windshield
        estimated_cost: 500.00
        witness_name: Jane Austin

    #################################
    Date: 19/02/16 07:59
    Type: Auto Theft
        owner_name: Bob Jones
        vehicle_make: Jaguar
        vehicle_model: XJ6
        vehicle_year: 2015
        vehicle_color: Red
        location: London Bridge
        witness: None




[1] https://en.wikipedia.org/wiki/XML
[2] https://en.wikipedia.org/wiki/Markup_language
[3] https://en.wikipedia.org/wiki/Open_standard
[4] http://www.w3.org/TR/REC-xml
[5] https://en.wikipedia.org/wiki/World_Wide_Web_Consortium
[6] https://www.python.org
[7] https://docs.python.org/2/library/xml.etree.elementtree.html
