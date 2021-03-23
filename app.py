from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    x = request.args.get('x')
    y = request.args.get('y')
    return multiply(x,y)
    
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
      
def multiply(x,y):
    return x*y;