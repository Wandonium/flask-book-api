from flask import Flask, render_template, request, jsonify
import os, re
import db

app = Flask(__name__)

# create the database and table. Insert 10 test books into db
# Do this only once to avoid inserting the test books into 
# the db multiple times
if not os.path.isfile('books.db'):
    db.connect()

# route for landing page
# check out the template folder for the index.html file
# check out the static folder for css and js files
@app.route("/")
def index():
    return render_template("index.html")

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return True
    else:
      return False

# time complexity is O(sqr(n)) coz of array to produce bks and
# array to check if title in bks. This needs optimization
# space complexity is O(1) coz of use of array of dictionaries
@app.route("/request", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    email = req_data['email']
    if not isValid(email):
        return jsonify({
            'status': '422',
            'res': 'failure',
            'error': 'Invalid email format. Please enter a valid email address'
        })
    title = req_data['title']
    bks = [b.serialize() for b in db.view()]
    for b in bks:
        if b['title'] == title:
            return jsonify({
                # 'error': '',
                'res': b,
                'status': '200'
            })
    # print('bks: ', bks)
    return jsonify({
        # 'error': '',
        'res': f'Sorry! Book with title {title} was not found!',
        'status': '404'
    })

# time complexity is O(sqr(n)) coz of array to produce bks and
# array to check if title in bks. This needs optimization
# space complexity is O(1) coz of use of array of dictionaries
@app.route('/request', methods=['GET'])
def getRequest():
    content_type = request.headers.get('Content-Type')
    bks = [b.serialize() for b in db.view()]
    if (content_type == 'application/json'):
        json = request.json
        for b in bks:
            if b['id'] == int(json['id']):
                return jsonify({
                    # 'error': '',
                    'res': b,
                    'status': '200'
                })
        return jsonify({
            'error': f"Sorry! Book with id '{json['id']}' not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': bks,
                    'status': '200'
                })

# time complexity is O(sqr(n)) coz of array to produce bks and
# array to check if title in bks. This needs optimization
# space complexity is O(1) coz of use of array of dictionaries
@app.route('/request/<id>', methods=['GET'])
def getRequestId(id):
    req_args = request.view_args
    # print('req_args: ', req_args)
    bks = [b.serialize() for b in db.view()]
    if req_args:
        for b in bks:
            if b['id'] == int(req_args['id']):
                return jsonify({
                    # 'error': '',
                    'res': b,
                    'status': '200'
                })
        return jsonify({
            'error': f"Sorry! Book with id '{req_args['id']}' was not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': bks,
                    'status': '200'
                })

# time complexity is O(sqr(n)) coz of array to produce bks and
# array to check if title in bks. This needs optimization
# space complexity is O(1) coz of use of array of dictionaries
@app.route('/request/<id>', methods=['DELETE'])
def deleteRequest(id):
    req_args = request.view_args
    print('req_args: ', req_args)
    bks = [b.serialize() for b in db.view()]
    if req_args:
        for b in bks:
            if b['id'] == int(req_args['id']):
                db.delete(b['id'])
                updated_bks = [b.serialize() for b in db.view()]
                # print('updated_bks: ', updated_bks)
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=8000)