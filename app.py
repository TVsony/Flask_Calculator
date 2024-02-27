from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return ("Calculator")

@app.route('/cal',methods=["GET"])
def math_opration():
    operation=request.json["operation"]
    numbers1=request.json["number1"]
    numbers2=request.json["number2"]

    if operation=="add":
        result=numbers1+numbers2
    elif operation=="multiply":
        result=numbers1*numbers2
    elif operation=="division":
        result=numbers1/numbers2
    else:
        result=numbers1-numbers2
    return result





if __name__=='__main__':
    app.run(debug=True)