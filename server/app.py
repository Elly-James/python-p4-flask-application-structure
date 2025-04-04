#!/usr/bin/env python3


# is used to indicate the interpreter that should be used to execute the script. 
# In this case, #!/usr/bin/env python3 tells the system to use the python3 interpreter found in the user's environment. 
# the shebang is only needed if you want to run the script directly as an executable (without explicitly calling Python).


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)



