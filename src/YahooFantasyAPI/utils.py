import xmltodict


def xml2dict(xml_string):
    res = xmltodict.parse(xml_input=xml_string)
    return res