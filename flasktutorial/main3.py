from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_mail import Mail
import json
import os
import math
from datetime import date

with open('config.json','r') as c:
    params=json.load(c)["params"]

local_server=True

app=Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER']=params['upload_location']
app.config.update(                         #for login email
    MAIL_SERVER ='smtp.gmail.com',
    MAIL_PORT ='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail=Mail(app)              # use Mail which is imported

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']     # for connectig to mysql
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db=SQLAlchemy(app)                        # intialize

class Contact(db.Model):
    '''
    sno,name,emial,phone_num,mes,date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mes = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Posts(db.Model):
    '''
    sno,title,slug,content,date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    img_file = db.Column(db.String(12), nullable=True)
    date = db.Column(db.String(12), nullable=True)

@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    #[0:params["no_of_posts"]]  # no posts

    page=request.args.get('page')
    if(not str(page).isnumeric()):
        page=1
    page=int(page)                   ##for slicing of post
    posts=posts[(page-1)*int(params['no_of_posts']) : (page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
    #pagination logic
    #first page
    if (page==1):
        prev="#"
        next="/?page="+str(page+1)
    #last page
    elif(page==last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    #middle
    else:
        next = "/?page=" + str(page + 1)
        prev = "/?page=" + str(page - 1)

    return render_template('index.html', params=params,posts=posts,prev=prev,next=next)      # or return   "hello world"

@app.route("/post/<string:post_slug>",methods=['GET'])                   #for slug
def post_route(post_slug):                       # varibale declare
    post=Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html',params=params,post=post)


# for creating end points like / and other end point execute other function
@app.route("/about")
def ravi():                            # varibale declare
    return render_template('about.html', params=params)
                                        # name1 is for template html file
                                        # name is for python file

@app.route("/dashboard",methods=['GET','POST'])
def dashboard():            # varibale declare

    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html',params=params,posts=posts)

    if request.method =='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username==params['admin_user'] and userpass==params['admin_password']):
            #set the session variable
            session['user']=username
            posts=Posts.query.all()
            return render_template('dashboard.html',params=params,posts=posts)

    return render_template('login.html', params=params)


@app.route("/edit/<string:sno>",methods=['GET','POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method=='POST':
            box_title=request.form.get('title')
            tagline=request.form.get('tagline')
            slug=request.form.get('slug')
            content=request.form.get('content')
            img_file=request.form.get('img_file')
            date=datetime.now()

            if sno=='0':
                post=Posts(title=box_title,tagline=tagline,slug=slug,content=content,img_file=img_file,date=date)
                db.session.add(post)
                db.session.commit()
                #return redirect('/edit/'+sno)
            else:
                post=Posts.query.filter_by(sno=sno).first()
                post.title=box_title
                post.tagline=tagline
                post.slug=slug
                post.content=content
                post.img_file=img_file
                post.date=date
                db.session.commit()
                return redirect('/edit/' + sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html',params=params,post=post)

@app.route("/uploader",methods=['GET','POST'])              # for upload file
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == 'POST'):
            f=request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            return "Uploaded successfully"

@app.route("/logout")      #for logout we kill the sesson
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route("/delete/<string:sno>",methods=['GET','POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')

@app.route("/contact",methods=['GET','POST'])
def contact():
    if (request.method=='POST'):
        '''add entry to databse'''
        name= request.form.get('name')             # take name form html
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        '''
            sno,name,emial,phone_num,mes,date
        '''
        entry=Contact(name=name,email=email,phone_num=phone,mes=message,date=date)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('new message from blog'+ name,
                          sender=email,
                          recipients=[params["gmail-user"]],
                          body=message+"\n"+phone)

    return render_template('contact.html', params=params)

@app.route("/sample post")
def post():
    return render_template('post.html',params=params)

app.run(debug=True)    # by using true we only first execute the code next time it automatically reloaded on website