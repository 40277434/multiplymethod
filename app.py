from flask import Flask, request




app = Flask(__name__)



def multiply(x,y):

    return int(x)*int(y);



    

@app.route('/')

def hello_world():

    x = request.args.get('x')

    y = request.args.get('y')

    result= dict()
    result['answer']=multiply(x,y)
    return result

    

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=80)

      

