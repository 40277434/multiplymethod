from flask import Flask, request,redirect,url_for

app = Flask(__name__)


def multiply(x, y):
    return int(x) * int(y);

@app.route('/')

def hello_world():
    x = request.args.get('x')
    y = request.args.get('y')
    result = dict()

    if(x.isdigit() and y.isdigit()):
        answer=multiply(x, y)
        result['answer'] =answer
        result['error']=False
        result['string']="%s*%s=%s"%(x,y,answer)
    else :
        result['reason'] ="X and Y must be digits"
        result['error']=True
    return result



if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)
