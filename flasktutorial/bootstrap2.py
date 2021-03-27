from flask import Flask,render_template
app= Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')      # or return   "hello world"

# for creating end points like / and other end point execute other function
@app.route("/about")
def ravi():
    name="ravi rana"                             # varibale declare
    return render_template('about.html',name1=name)
                                        # name1 is for template html file
                                        # name is for python file
@app.route("/boot")
def boot():
    return render_template('bootstrap.html')

app.run(debug=True)    # by using true we only first execute the code next time it automatically reloaded on website