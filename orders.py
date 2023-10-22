from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World, I am the Orders Service, I will handle orders!'


@app.route('/api/orders/new')
def new_order():
	return 'Hello World, I am the Orders Service, I will handle orders!'


@app.route('/api/orders/update')
def update_order():
	return 'Hello World, I am the Orders Service, I will handle orders!'


@app.route('/api/orders/get')
def get_order():
	return 'Hello World, I am the Orders Service, I will handle orders!'


@app.route('/api/orders/delete')
def delete_order():
	return 'Hello World, I am the Orders Service, I will handle orders!'

if __name__ == '__main__':
	app.run()
