from flask import Flask, jsonify, request

from manipulator import get_xml_tag_and_value

app = Flask(__name__)


@app.route("/xml2text", methods=["POST"])
def convert_xml_to_text():
    file_storage_obj = request.files['file']
    csv_string = get_xml_tag_and_value(file_storage_obj.read())
    return jsonify({'csv': csv_string})


if __name__ == "__main__":
    app.run(debug=True)
