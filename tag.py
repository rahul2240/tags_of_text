from flask import Flask
from flask import jsonify
from flask import make_response
from urllib.error import HTTPError,URLError
from flask import request
import requests

app = Flask(__name__)
@app.route('/', methods=['POST'])
def text():
    try:
        data = request.get_json()
        r = requests.post(
            "https://api.deepai.org/api/text-tagging",
            data={
                'text': data['text']
                 },
            headers={'api-key': 'fe2f2d95-9bb4-4488-bd37-aad471f2f23d'}
        )
        p = r.json()
        p = p["output"]
        tag = p.split("\n")
        tag = " ".join(tag)
        return make_response(jsonify({"tags": tag}), 201)

    except HTTPError as e:
        print(e.code)
        return str(e) + 'HTTPError'
    except URLError as e:
        print(e.args)
        return str(e) + 'Url Error'

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port= '8800',debug=True)

# r = requests.post(
#     "https://api.deepai.org/api/text-tagging",
#     data={
#         'text': 'Air pollution is a mixture of solid particles and gases in the air. Car emissions, chemicals from factories, dust, pollen and mold spores Some air pollutants are poisonous. Inhaling them can increase the chance youll have health problems. People with heart or lung disease, older adults and children are at greater risk from air pollution. Air pollution isnt just outside - the air inside buildings can also be polluted and affect your health.',
#     },
#     headers={'api-key': 'fe2f2d95-9bb4-4488-bd37-aad471f2f23d'}
# )
# print(r.json())


# Example posting a local text file:
#
# import requests
# r = requests.post(
#     "https://api.deepai.org/api/text-tagging",
#     files={
#         'text': open('/path/to/your/file.txt', 'rb'),
#     },
#     headers={'api-key': 'fe2f2d95-9bb4-4488-bd37-aad471f2f23d'}
# )
# print(r.json())
#

# Example directly sending a text string:

# import requests
# r = requests.post(
#     "https://api.deepai.org/api/text-tagging",
#     data={
#         'text': 'YOUR_TEXT_HERE',
#     },
#     headers={'api-key': 'fe2f2d95-9bb4-4488-bd37-aad471f2f23d'}
# )
# print(r.json())
