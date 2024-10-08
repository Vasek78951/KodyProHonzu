import xml.etree.ElementTree as ET

def person_search(xml):
    root = ET.fromstring(xml)

    persons = []

    for person in root.findall('.//Ososba'):
        first_name = person.find('Jmeno').text if person.find('Jmeno').text is None else "Nezname"
        last_name = person.find('Prijmeni').text if person.find('Prijmeni').text is None else "Nezname"
        persons.append(f"{first_name} {last_name}")

    if persons:
        print("Fyzické osoby uvedené v záznamu:")
        for p in persons:
            print(p)
    else:
        print("Žádné fyzické osoby nebyly nalezeny.")