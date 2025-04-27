# Workout Tracker API

A simple Flask + SQLite API for tracking workouts.  
Designed to run locally or inside a Docker container for easy deployment to a NAS or cloud server.

---

## Features

- Add new exercises (name, sets, reps)
- Retrieve list of all logged exercises
- Automatically timestamps each entry
- Lightweight, portable, and easy to expand

---

## Requirements

- Python 3.8+
- Flask
- SQLite (comes built-in with Python)

---

## Getting Started

1. Clone the repository:

    ```bash
    git clone [your repo url]
    cd workout-tracker
    ```

2. Create a Python virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install flask
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. The server will start on `http://localhost:5000/`.

---

## API Endpoints

### GET `/`
Returns a simple message to confirm the server is running.

### POST `/add`
Adds a new exercise.

**Request body:**

```json
{
  "name": "Push-up",
  "sets": 3,
  "reps": 15
}
