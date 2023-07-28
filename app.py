from flask import Flask, render_template, jsonify

app = Flask(__name__)

#Create a list of jobs and then add the list to the render as a parameter and finally modified the HTML in to do section
JOBS = [
  {
    'id': 1,
    'title': 'Software Engineer',
    'location':  'Espoo, FIN',
    'salary': '€ 4000'
  },
  {
    'id': 2,
    'title': 'Python Programmer',
    'location':  'TRE, FIN',
    'salary': '€ 4500'
  },
  {
    'id': 3,
    'title': 'UX designer',
    'location':  'HKI, FIN',
    'salary':'',
    
  },
  {
    'id': 4,
    'title': 'Backend Eng',
    'location':  'US',
    'salary': '€ 5500'
   }

  
]


#@ is a decorator who indicates after the backslash display hello world
@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                          company_name='Amirs')



#add JSON file of the JOBS
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug= True)