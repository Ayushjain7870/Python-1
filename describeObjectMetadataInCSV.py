import os
import csv
import xml.etree.ElementTree as ET

def convert_xml_to_csv(folder_path):
    # Initialize CSV writer
    csv_file = open('output.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    
    # Write header
    csv_writer.writerow(['fullName', 'description', 'externalId', 'label', 'length', 'required', 'trackFeedHistory', 'trackHistory', 'type', 'unique'])
    
    # Loop through XML files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            # Parse XML file
            tree = ET.parse(os.path.join(folder_path, filename))
            root = tree.getroot()
            
            # Extract data from XML
            data = {}
            for child in root:
                tag = child.tag.split('}')[1]  # Remove namespace prefix
                data[tag] = child.text
            
            # Write data to CSV
            csv_writer.writerow([data.get('fullName', ''), data.get('description', ''), data.get('externalId', ''),
                                 data.get('label', ''), data.get('length', ''), data.get('required', ''),
                                 data.get('trackFeedHistory', ''), data.get('trackHistory', ''), data.get('type', ''),
                                 data.get('unique', '')])
    
    # Close CSV file
    csv_file.close()

# Example usage
folder_path = './fields'
convert_xml_to_csv(folder_path)
