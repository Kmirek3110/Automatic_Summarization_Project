import xml.etree.ElementTree as ET
import os


class XmlParser:

    def __init__(self, directory):
        self.directory = directory

    def parse_data_xml(self, filepath):
        
        tree = ET.parse(filepath)
        root = tree.getroot()

        content = root.find("body").text
        summaries = root.find("summaries")

        extracted_summaries = []
        abstract_summaries = []

        for child in summaries:
            
            type = child.attrib['type']
            body = child.find("body")

            if type == "extract":
                extracted_summaries.append(body.text)
            elif type == "abstract":
                abstract_summaries.append(body.text)
            
        
        return content, extracted_summaries, abstract_summaries
    
    def get_dictonary_data(self):

        parsed_files = []

        for filename in os.listdir(self.directory):
            fullpath = self.directory + "/" + filename
            if filename.endswith(".xml"):
                f_parsed = self.parse_data_xml(fullpath)
                parsed_files.append(f_parsed)
            else:
                continue

        return parsed_files
    