from flask import Flask,jsonify

app = Flask(_name_)

@app.route('/')
def home():
    return jsonify({'message':'welcome'})

@app.route('/on')
def on():
    return jsonify({'state':'1'})

@app.route('/off')
def off():
    return jsonify({'state':'0'})

if __name__=='__main__':
	app.run(debug=True)
	

    








