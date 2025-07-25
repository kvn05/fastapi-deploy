# FastAPI Simple API

https://fastapi-deploy-kavans-projects-fac429ac.vercel.app/

A minimal and straightforward API built with FastAPI, showcasing basic CRUD-like operations on in-memory data for books and users. This project serves as a foundational example for deploying FastAPI applications.

## ✨ Features

* **FastAPI Framework:** Leverage the speed and simplicity of FastAPI.
* **In-Memory Database:** Quick setup with dictionaries for demonstration purposes.
* **Basic Endpoints:**
    * `/`: Welcome message
    * `/books/`: Get all books
    * `/books/{book_id}`: Get a specific book
    * `/users/`: Get all users
    * `/users/{user_id}`: Get a specific user
* **Vercel Deployment Ready:** Configured for seamless deployment on Vercel.

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/kvn05/fastapi-deploy.git
    cd fastapi-deploy
    ```

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage dependencies.

    * **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

Once your virtual environment is active and dependencies are installed, you can start the FastAPI application:

```bash
uvicorn main:app --reload
