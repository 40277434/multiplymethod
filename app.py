from flask import Flask, request,redirect,url_for

app = Flask(__name__)


def multiply(x, y):
    return int(x) * int(y);

@app.route('/')

def hello_world():
    x = request.args.get('x')
    y = request.args.get('y')
    if(x.isdigit() and y.isdigit()):
        result = dict()
        result['answer'] = multiply(x, y)
        return result
    else :
        return demo2


@app.route('/demo0')
def demo0():
    return 'Webpage not found'

@app.route('/demo1')
def demo1():
    return 'Pay attention to input parameters'

@app.route('/demo2')
def demo2():
    return 'The input data type is not an integer'


@app.errorhandler(404)
def demo0(e):
    return redirect(url_for('demo0'))
@app.errorhandler(500)
def demo1(e):
    return redirect(url_for('demo1'))
@app.errorhandler(500)
def demo2(e):
    return redirect(url_for('demo2'))


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)
