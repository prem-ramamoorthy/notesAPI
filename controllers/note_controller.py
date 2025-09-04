# controllers/note_controller.py
from typing import List, Optional
from datetime import datetime
from models.note import Note, NoteCreate, NoteUpdate, NoteResponse

class NoteController:
    def __init__(self):
        self.notes: List[Note] = []
        self.next_id = 1

    def get_all_notes(self) -> List[NoteResponse]:
        """Get all notes"""
        return [self._note_to_response(note) for note in self.notes]

    def get_note_by_id(self, note_id: int) -> Optional[NoteResponse]:
        """Get a specific note by ID"""
        note = self._find_note_by_id(note_id)
        if note:
            return self._note_to_response(note)
        return None

    def create_note(self, note_create: NoteCreate) -> NoteResponse:
        """Create a new note"""
        current_time = datetime.now().isoformat()
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        new_note = Note(
            id=self.next_id,
            title=note_create.title,
            content=note_create.content,
            date=current_date,
            created_at=current_time,
            updated_at=current_time
        )
        
        self.notes.append(new_note)
        self.next_id += 1
        
        return self._note_to_response(new_note)

    def update_note(self, note_id: int, note_update: NoteUpdate) -> Optional[NoteResponse]:
        """Update an existing note"""
        note = self._find_note_by_id(note_id)
        if not note:
            return None
        
        # Update only provided fields
        if note_update.title is not None:
            note.title = note_update.title
        if note_update.content is not None:
            note.content = note_update.content
        
        note.updated_at = datetime.now().isoformat()
        
        return self._note_to_response(note)

    def delete_note(self, note_id: int) -> bool:
        """Delete a note by ID"""
        note = self._find_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            return True
        return False

    def _find_note_by_id(self, note_id: int) -> Optional[Note]:
        """Helper method to find a note by ID"""
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def _note_to_response(self, note: Note) -> NoteResponse:
        """Convert Note model to NoteResponse"""
        return NoteResponse(
            id=note.id,
            title=note.title,
            content=note.content,
            date=note.date,
            created_at=note.created_at,
            updated_at=note.updated_at
        )