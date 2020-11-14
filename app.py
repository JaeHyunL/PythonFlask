from flask import Flask ,render_template
from flask_admin import Admin 
app = Flask(__name__) # set optional bootswatch theme 
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean' 
# set flask_admin 
#admin = Admin(app, name='microblog', template_mode='bootstrap3') 
admin = Admin(app, name='microblog', base_template='index2.html') 

@app.route('/') 
def hello_world(): 
    pagetitle = "HomePage"
    
    return render_template("index.html",mytitle=pagetitle, mycontent="Hello World") 


if __name__ == '__main__': app.run()
