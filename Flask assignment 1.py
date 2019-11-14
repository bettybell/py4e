from flask import Flask, request
app = Flask (__name__)

@app.route("/")
def index () :
        return "Hello World!"

@app.route("/form")
def form () :
    return '''
        <form action="/processing" method="POST">
            Hours:<input type="text" name="Enter hours"><br>
            Rate:<input type="text" name="Enter rate"><br>
            <input type="submit" value="Calculate payment"> 
        </from>
    '''

@app.route("/processing", methods=["POST","GET"])
def processing():
    Hours = request.form["Enter hours"]
    Rate = request.form["Enter rate"]
    return "Payment is {}".format(float(Hours) * float(Rate))


if __name__ == "__main__":
    app.run(debug=True)