from flask import Flask, render_template, jsonify
#importing the module flask and then installing class Flask

#creating an object of the class Flask
app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 2,
  'title': 'Data Engineer',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Bengaluru, India',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 15,00,000'
}]


#routing to empty
@app.route("/")
def hello_jovian():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
