from lxml import etree


def get_xml_tag_and_value(xml: bytes) -> str:
    """
    The script takes the xml file in the binary format and returns the
    tags and value in the comma separated format followed by new line .
    """
    csv_string = ''
    root = etree.fromstring(xml)
    for index, element in enumerate(root):
        if index == len(root)-1:
            csv_string = csv_string + f'{element.tag}:{element.text}'
        else:
            csv_string = csv_string + f'{element.tag}:{element.text},\n'
    return csv_string

