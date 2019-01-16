
from flask import request, render_template, Blueprint, flash, redirect, url_for
from app.controllers import NotesDao
from app.forms import *


# 定义蓝图
notesbp = Blueprint('notesbp', __name__, template_folder='templates')

@notesbp.route('/')
def index():

    noteservice = NotesDao()

    # return book list to front end
    notes = noteservice.list_all()
    return render_template('index.html', notes=notes)


@notesbp.route('/new', methods=['GET', 'POST'])
def new_note():
    form = NewNoteForm()

    if request.method == 'POST':
        body = request.form['body']
        noteservice = NotesDao()
        noteservice.create_note(body)

        return redirect(url_for('notesbp.index'))

    return render_template('new_note.html', form=form)


@notesbp.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    form = EditNoteForm()
    note = NotesDao().get_note(note_id)

    if request.method == 'POST':
        body = request.form['body']
        note.body = body
        NotesDao().update_note(note)

        return redirect(url_for('notesbp.index'))

    form.body.data = note.body
    return render_template('edit_note.html', form=form)


@notesbp.route('/delete/<int:note_id>', methods=['GET'])
def delete_note(note_id):
    notesdao = NotesDao()
    note = notesdao.get_note(note_id)
    notesdao.delete_note(note)

    return redirect(url_for('notesbp.index'))




