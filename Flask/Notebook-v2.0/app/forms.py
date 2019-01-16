
from wtforms import Form, TextAreaField, SubmitField

class NewNoteForm(Form):
    body = TextAreaField('body', render_kw={'class': 'text-body', 'rows': 10, 'placeholder': '输入您的想法...'})
    submit = SubmitField('Save')

class EditNoteForm(Form):
    body = TextAreaField('body', render_kw={'class': 'text-body', 'rows': 10, 'placeholder': '输入您的想法...'})
    submit = SubmitField('Update')

