from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    blog= TextAreaField('Write your Blog',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):

    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    username = StringField("Enter your name")
    email = StringField("Email", validators=[Required()])
    submit= SubmitField('Subscribe')   

class CommentForm(FlaskForm):

    comment= TextAreaField('Comment',validators=[Required()])
    submit = SubmitField('Submit')
class UpdateForm(FlaskForm):
   
    blog=TextAreaField('Add New Blog' , validators=[Required()]) 
    submit= SubmitField('SUBMIT')    