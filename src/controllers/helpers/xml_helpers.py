import xml.etree.ElementTree as ET

def dict_to_xml(tag, d):
    """
    Turn a simple dict of key/value pairs into XML
    """
    elem = ET.Element(tag)
    for key, val in d.items():
        child = ET.SubElement(elem, key)
        child.text = str(val)
    return elem

def pokemons_to_xml(pokemons):
    """
    Convert a dictionary or a list of dictionaries to an XML string
    """
    if isinstance(pokemons, dict):
        pokemons = [pokemons]
    
    root = ET.Element("pokemons")
    for pokemon in pokemons:
        pokemon_elem = dict_to_xml("pokemon", pokemon)
        root.append(pokemon_elem)
    
    return ET.tostring(root, encoding='unicode')