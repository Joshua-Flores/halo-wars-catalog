# Halo Wars 2 Leader Catalog

This project is a FastAPI-based application to manage a catalog of leaders from Halo Wars 2. It includes CRUD operations and uses an SQLite database for testing purposes.

## Requirements

- Python 3.8+
- pip
- Virtualenv (optional but recommended)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/halo-wars-catalog.git
cd halo-wars-catalog
```

### Set Up the Virtual Environment

It is recommended to use a virtual environment to manage dependencies. You can set one up using the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Set Up the Database

For testing purposes, an SQLite database is used. The database schema is automatically managed by SQLAlchemy, so no additional setup is needed for the test environment.

### Running the Application

To run the FastAPI application locally, use Uvicorn:

```bash
uvicorn app.main:app --reload
```

The application will be available at http://localhost:8000/docs.

### Running Tests

To run the tests and ensure everything is working correctly, use pytest:

```bash
pytest -s
```
