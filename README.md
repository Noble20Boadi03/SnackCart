# FastAPI + React Application

A full-stack application with a FastAPI backend and React frontend for managing products.

## Prerequisites

- Python 3.8+
- Node.js 14+ and npm
- PostgreSQL (for database)

## Project Structure

```
├── backend/
│   ├── firstcode.py                    # Main FastAPI application
│   ├── models.py                       # Pydantic models
│   ├── postgre_database.py             # Database connection
│   ├── postgre_database_models.py      # SQLAlchemy models
│   ├── requirements.txt                # Python dependencies
│   └── venv/                           # Python virtual environment
│
└── frontend/
    ├── src/
    │   ├── App.js                      # Main React component
    │   ├── index.js                    # React entry point
    │   └── ...
    └── package.json                    # Node dependencies
```

## Setup Instructions

### 1. Backend Setup

#### Step 1: Navigate to the project directory
```bash
cd "c:\Users\HP\OneDrive\Documents\SOFTWARe ENG\FASTAPI\beginners_telesko_turorials"
```

#### Step 2: Create and activate virtual environment (if not already done)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
source venv/bin/activate
```

#### Step 3: Install Python dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Configure PostgreSQL database
- Ensure PostgreSQL is running
- Update database connection details in `postgre_database.py` if needed
- The application will automatically create tables on startup

### 2. Frontend Setup

#### Step 1: Navigate to the frontend directory
```bash
cd frontend
```

#### Step 2: Install Node dependencies
```bash
npm install
```

## Running the Application

### Option 1: Run Both Services Simultaneously (Recommended)

#### Terminal 1 - Start Backend:
```bash
# Make sure you're in the project root and virtual environment is activated
python -m uvicorn firstcode:app --reload
```

The backend will run on `http://localhost:8000`

#### Terminal 2 - Start Frontend:
```bash
cd frontend
npm start
```

The frontend will run on `http://localhost:3000`

### Option 2: Run Individually

**Backend only:**
```bash
python -m uvicorn firstcode:app --reload
```

**Frontend only:**
```bash
cd frontend
npm start
```

## API Endpoints

The FastAPI backend exposes the following endpoints (available at `http://localhost:8000`):

- `GET /` - Welcome/root endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

View the interactive documentation at `http://localhost:8000/docs` once the backend is running.

## Configuration

### CORS Settings
The backend is configured to accept requests from the React frontend:
- **Origin:** `http://localhost:3000`
- **Methods:** All methods allowed
- **Headers:** All headers allowed

### Database
The application uses PostgreSQL with SQLAlchemy ORM. Ensure your database credentials are properly configured in `postgre_database.py`.

## Technologies Used

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI web server
- **SQLAlchemy** - ORM for database
- **psycopg2** - PostgreSQL adapter

### Frontend
- **React** - UI library
- **Axios** - HTTP client
- **react-scripts** - Build tooling

## Troubleshooting

### Backend won't start
- Ensure Python virtual environment is activated
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify PostgreSQL is running and connection details are correct

### Frontend won't start
- Ensure you're in the `frontend` directory
- Delete `node_modules` and run `npm install` again
- Clear npm cache: `npm cache clean --force`

### Port already in use
- Backend (8000): `netstat -ano | findstr :8000` (Windows)
- Frontend (3000): Change in frontend or kill process using the port

### CORS errors
- Ensure backend is running on `http://localhost:8000`
- Check that frontend is accessing backend through the proxy configured in `package.json`

## Notes

- The virtual environment (`venv`) is already set up in the project
- The `--reload` flag enables automatic server restart on code changes (development only)
- The frontend proxy is configured to forward API calls to the backend


