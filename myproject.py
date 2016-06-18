from flask import Flask,render_template,jsonify,request,abort,make_response,url_for
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
application = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
application.config['MYSQL_DATABASE_USER'] = 'root'
application.config['MYSQL_DATABASE_PASSWORD'] = 'raja'
application.config['MYSQL_DATABASE_DB'] = 'bucketlist'
application.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(application)

tasks = [{
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done": False,
      "id": 1,
      "title": "Buy groceries"
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }] 

@application.route("/")
def hello():
    return render_template('index.html')

@application.route("/data")
def  page():
    return "<h1 style='color:blue'>Hello!</h1>"

@application.route("/showsignup")
def showsignup():
    return render_template('signup.html')

#@application.route('/signUp',methods=['POST'])
#def signUp():
     
#    conn = mysql.connect()
    # read the posted values from the UI
#    _name = request.form['inputName']
#    _email = request.form['inputEmail']
#    _password = request.form['inputPassword']
#    _hashed_password =  generate_password_hash(password)
#    cursor = conn.cursor()
    
#    cursor.callproc('sp_createuser',(_name,_email,_hashed_password))
#    # validate the received values
#    data = cursor.fetchall()
#    if len(data) is 0:
#        return json.dumps({'html':'<span>All fields good !!</span>'})
#    else:
#        return json.dumps({'html':'<span>Enter the required fields</span>'})


@application.route('/hello/api/v1.0/tasks',methods = ['GET'])
def get_task():
    
    return jsonify({'tasks':tasks})


@application.route('/hello/api/v1.0/tasks/<int:task_id>',methods = ['GET'])
def get_tasks(task_id):
   task = [task for task in tasks if task['id'] == task_id]
   if len(task) ==0:
      abort(404)
   return jsonify({'tasks':task[0]})

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
