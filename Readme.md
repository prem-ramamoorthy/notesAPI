# Notes Management API

A simple REST API for managing notes built with FastAPI. This API allows you to create, read, update, and delete notes with automatic timestamps and proper error handling.

# Live Link
    https://notesapi-1-s22g.onrender.com

## Features

- Create, read, update, and delete notes
- Automatic timestamp generation
- Proper HTTP status codes
- Input validation with Pydantic
- Interactive API documentation
- Clean, organized code structure
- In-memory storage (no database required)

## Project Structure

```
notes_api/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── models/
│   └── note.py            # Pydantic models
├── controllers/
│   └── note_controller.py # Business logic
└── routes/
    └── note_routes.py     # API endpoints
```

## Installation & Setup

1. **Clone or create the project files**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Access the API:**
   - API Base URL: http://localhost:8000
   - Interactive Docs: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc

## API Endpoints

### GET /notes
Get all notes
- **Response:** `200 OK` with array of notes

### POST /notes
Create a new note
- **Request Body:**
  ```json
  {
    "title": "My Note",
    "content": "This is my note content"
  }
  ```
- **Response:** `201 Created` with created note

### GET /notes/{id}
Get a specific note by ID
- **Response:** `200 OK` with note or `404 Not Found`

### PUT /notes/{id}
Update an existing note
- **Request Body:** (both fields optional)
  ```json
  {
    "title": "Updated Title",
    "content": "Updated content"
  }
  ```
- **Response:** `200 OK` with updated note or `404 Not Found`

### DELETE /notes/{id}
Delete a note by ID
- **Response:** `204 No Content` or `404 Not Found`

## Example Usage

### Create a note:
```bash
curl -X POST "http://localhost:8000/notes" \
     -H "Content-Type: application/json" \
     -d '{"title": "Shopping List", "content": "Milk, Eggs, Bread"}'
```

### Get all notes:
```bash
curl "http://localhost:8000/notes"
```

### Get a specific note:
```bash
curl "http://localhost:8000/notes/1"
```

### Update a note:
```bash
curl -X PUT "http://localhost:8000/notes/1" \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Shopping List"}'
```

### Delete a note:
```bash
curl -X DELETE "http://localhost:8000/notes/1"
```

## Response Format

All notes follow this structure:
```json
{
  "id": 1,
  "title": "My Note",
  "content": "This is my note content",
  "date": "2025-09-04",
  "created_at": "2025-09-04T20:08:00.123456",
  "updated_at": "2025-09-04T20:08:00.123456"
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200` - Success
- `201` - Created
- `204` - No Content (successful deletion)
- `404` - Not Found
- `422` - Validation Error

Error responses include descriptive messages:
```json
{
  "detail": "Note with id 999 not found"
}
```

## Development

The code is organized into separate modules:
- **Models**: Define data structures and validation
- **Controllers**: Handle business logic
- **Routes**: Define API endpoints
