from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/v1/sanitized/<int:n>')
def sanitized(n):

    if(n==str):
        result= {
            "input" : "Sanitized"
        }
    else:
        result= {
            "input" : "UnSanitized"
        }

    return jsonify(result)


if __name__ =='__main__':
    app.run(debug=True)
