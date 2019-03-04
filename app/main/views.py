from flask import render_template,request,redirect,url_for,abort,request
from . import main
from ..models import  User,Blog,Comment,Subscriber,Quote
from flask_login import login_required, current_user
from .forms import BlogForm,CommentForm,UpdateProfile,SubscriberForm
from .. import db,photos
from ..request import get_quotes


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The Blogs Application'
    quote = get_quotes()
    blogs = Blog.get_blogs()
    

    return render_template('index.html', title = title, blogs=blogs, quote=quote)


@main.route('/user/<uname>')

def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.Updatecommit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
   user = User.query.filter_by(username = uname).first()
   if 'photo' in request.files:
       filename = photos.save(request.files['photo'])
       path = f'photos/{filename}'
       user.profile_pic_path = path
       db.session.commit()
   return redirect(url_for('main.update_profile',uname=uname))

@main.route('/blog/new', methods=['GET', 'POST'])
@login_required

def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = form.blog.data
        print(blog)
        new_blog = Blog(blog=blog, user_id=current_user.id)
        new_blog.save_blogs()
        return redirect(url_for('main.index'))


        # db.session.add(new_blog)
        # db.session.commit()

    return render_template('new_blog.html', blog_form= form)

@main.route('/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required

def new_comment(id):
    form = CommentForm()
    comments=Comment.query.filter_by(blog_id=id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        print(comment)
        new_comment = Comment(comment=comment,blog_id=id,user_id=current_user.id)
        new_comment.save_comments()
        return redirect(url_for('main.index'))
    
    return render_template('new_comment.html', comment_form= form,comments=comments)     
     

@main.route('/subscribe',methods=["GET","POST"])
def subscriber():
    form=SubscriberForm()

    if form.validate_on_submit():
        subscriber = Subscriber(name=form.name.data,email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()

        mail_message("Welcome to my blog","email/welcome_user",subscriber.email,subscriber=subscriber)
        flash('A confirmation by email has been sent to you by email')
        return redirect(url_for('main.index'))
        title = 'Subscribe'
    return render_template('subscription.html',form=form)



@main.route('/blog/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_blog(id):
    """
    Edit a blogpost in the database
    """
    new_blog=False

    blog = Blog.get_blogs(id)
    form = BlogForm()

    if form.validate_on_submit():
        blog.blog = form.blog.data

        db.session.commit()
        print('edited comment ')


        return redirect(url_for('main.index'))
        form.blog.data = blog.blog

    return render_template('new_blog.html',action = 'Edit',
                           new_blog = new_blog,
                           blog_form = form,
                           legend='Update Post')