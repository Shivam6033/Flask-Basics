import requests
from pathlib import Path

if __name__ == "__main__":
    xml_filepath = Path(__file__).parent.joinpath("files", "input", "note.xml")
    output_file_path = Path(__file__).parent.joinpath("files", "output", "note.txt")
    with open(xml_filepath, "rb") as f_open:
        file = {'file': f_open}
        response = requests.post("http://127.0.0.1:5000/xml2text", files=file)
        """
        response.json() -> {'csv': "to:Tove,\nfrom:Jani,\nheading:Reminder,\nbody:Don't forget me this weekend!"}
        """

    with open(output_file_path, 'w') as f_open:
        f_open.write(response.json()['csv'])
