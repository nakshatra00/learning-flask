from flask import Flask, render_template
#importing the module flask and then installing class Flask

#creating an object of the class Flask
app = Flask(__name__)


#routing to empty
@app.route("/")
def hello_jovian():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
