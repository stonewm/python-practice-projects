
from wtforms import Form, TextAreaField, SubmitField

class NewNoteForm(Form):
    body = TextAreaField('body')
    submit = SubmitField('Save')

class EditNoteForm(Form):
    body = TextAreaField('body')
    submit = SubmitField('Update')

# class GoToEditForm(Form):
#     submit = SubmitField('Edit')
