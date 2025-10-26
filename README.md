# FastAPI To-Do API

A simple but professionally structured RESTful API for a "To-Do" list, built with Python and FastAPI.

This project was built to demonstrate best practices in modern API design, including:
* **Separation of Concerns:** Logic, models, and the app entrypoint are in separate files (`routes.py`, `models.py`, `main.py`).
* **Data Validation:** Uses Pydantic models to validate incoming data.
* **Auto-Documentation:** Generates interactive API docs at the `/docs` endpoint.

## Tech Stack
* **Python 3**
* **FastAPI**
* **Uvicorn** (ASGI Server)

## How to Run It

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/justknuth/fastapi-todo-api.git
    cd fastapi-todo-api
    ```

2.  **Change directory to the `api` folder:**
    ```bash
    cd api
    ```

3.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

4.  **Activate the virtual environment:**
    * **On macOS/Linux (Bash):**
        ```bash
        source venv/bin/activate
        ```
    * **On Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\activate
        ```

5.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Run the app:**
    ```bash
    uvicorn main:app --reload
    ```
    (You should see a message like: `Uvicorn running on http://127.0.0.1:8000`)

7.  **Test the API:**
    * Open your web browser and go to `http://127.0.0.1:8000/docs`.
    * This is an interactive documentation page for your API.
    * Expand the `POST /todos` endpoint, click "Try it out", and create a new to-do by pasting this into the request body:
        ```json
        {
          "task": "Finish my GitHub portfolio"
        }
        ```
    * Click "Execute". You'll see a `201` response.
    * Now, expand the `GET /todos` endpoint, click "Try it out", and click "Execute". You will see the to-do you just created in the response.