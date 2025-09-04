# routes/note_routes.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from models.note import NoteCreate, NoteUpdate, NoteResponse
from controllers.note_controller import NoteController

router = APIRouter()
note_controller = NoteController()

@router.get("/notes", response_model=List[NoteResponse], status_code=status.HTTP_200_OK)
async def get_all_notes():
    """Get all notes"""
    return note_controller.get_all_notes()

@router.get("/notes/{note_id}", response_model=NoteResponse, status_code=status.HTTP_200_OK)
async def get_note_by_id(note_id: int):
    """Get a specific note by ID"""
    note = note_controller.get_note_by_id(note_id)
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    return note

@router.post("/notes", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
async def create_note(note_create: NoteCreate):
    """Create a new note"""
    return note_controller.create_note(note_create)

@router.put("/notes/{note_id}", response_model=NoteResponse, status_code=status.HTTP_200_OK)
async def update_note(note_id: int, note_update: NoteUpdate):
    """Update an existing note"""
    updated_note = note_controller.update_note(note_id, note_update)
    if not updated_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    return updated_note

@router.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int):
    """Delete a note by ID"""
    deleted = note_controller.delete_note(note_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {note_id} not found"
        )
    return None