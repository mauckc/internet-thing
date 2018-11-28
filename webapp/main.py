from flask import *
app = Flask(__name__)

@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

#@app.route('/result')
#def result():
 #   dict = {'phy':50,'che':60,'maths':70}
   #return render_template('result.html', result = dict)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)
