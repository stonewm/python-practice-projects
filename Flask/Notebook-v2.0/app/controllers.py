
from app.models import db, Notes
from sqlalchemy import desc

class NotesDao():
    def create_note(self, note_body):
        new_note = Notes(body=note_body)
        db.session.add(new_note)
        db.session.commit()

        return new_note


    def update_note(self, note):
        modified_note = Notes.query.get(note.id)
        db.session.commit()

        return modified_note


    def delete_note(self, note):
        to_delete_note = Notes.query.get(note.id)
        db.session.delete(to_delete_note)
        db.session.commit()

        return True


    def list_all(self):
        return Notes.query.order_by(desc(Notes.id)).all()


    def get_note(self, id):
        return Notes.query.get(id)