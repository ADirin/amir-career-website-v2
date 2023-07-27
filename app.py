from flask import Flask

app = Flask(__name__)
#@ is a decorator which indicates after backslash display hello world
@app.route("/")
def hello_world():
    return "<h1>Hello, Amir!</h1>"
  #by running nothing has happened since in flash explained how things should be done

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug= True)