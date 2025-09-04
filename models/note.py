# models/note.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Note(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=200, description="Note title")
    content: str = Field(..., min_length=1, description="Note content")
    date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Note title")
    content: str = Field(..., min_length=1, description="Note content")

class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Note title")
    content: Optional[str] = Field(None, min_length=1, description="Note content")

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    date: str
    created_at: str
    updated_at: str