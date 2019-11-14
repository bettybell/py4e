from flask import Flask, request
app = Flask (__name__)

@app.route("/")
def index () :
        return "Hello World!"

@app.route("/form")
def form () :
    return '''
        <form action="/processing" method="POST">
            Enter a File Name: <input type="text" name="file_name"><br>
            <input type="submit" value="Open"> 
        </from>
    '''

@app.route("/processing", methods=["POST","GET"])
def processing():
    fname = request.form["file_name"]
    fhand = open(fname)
    inp = fhand.read()
    return "{}".format(inp)



if __name__ == "__main__":
    app.run(debug=True)