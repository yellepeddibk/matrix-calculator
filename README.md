# Matrix Calculator

[![CI](https://github.com/yellepeddibk/matrix-calculator/actions/workflows/ci.yml/badge.svg)](https://github.com/yellepeddibk/matrix-calculator/actions/workflows/ci.yml)

A deployed Flask web application for matrix computations with a responsive UI, RESTful API endpoints, CI, and cloud hosting on Render.

**[🚀 Live Demo](https://matrix-calculator-kw8z.onrender.com)**

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Matrix Calculator provides an intuitive web interface and REST API for common linear algebra operations. The application demonstrates:

- Clean separation between frontend and backend
- RESTful API design with JSON request/response
- Production deployment with health checks and process management
- CI/CD pipeline with automated linting and testing
- Responsive UI that works across desktop and mobile devices

---

## Architecture

```
                        Matrix Calculator Architecture

    ┌─────────────────────────────────────────────────────────────────┐
    │                         Client Layer                            │
    ├─────────────────────────────────────────────────────────────────┤
    │                                                                 │
    │   ┌─────────────────┐         ┌─────────────────────────────┐   │
    │   │   Web Browser   │         │      API Client (curl)      │   │
    │   │                 │         │                             │   │
    │   │  matrix.html    │         │  POST /api/determinant      │   │
    │   │  + Bootstrap    │         │  POST /api/rref             │   │
    │   │  + JavaScript   │         │                             │   │
    │   └────────┬────────┘         └──────────────┬──────────────┘   │
    │            │                                 │                  │
    └────────────┼─────────────────────────────────┼──────────────────┘
                 │           HTTP/JSON             │
                 ▼                                 ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │                       Flask Application                         │
    ├─────────────────────────────────────────────────────────────────┤
    │                                                                 │
    │   ┌─────────────────┐    ┌─────────────────┐    ┌───────────┐   │
    │   │   Routes        │    │   Computation   │    │  Health   │   │
    │   │                 │    │                 │    │           │   │
    │   │  GET /          │ ─> │  NumPy Matrix   │    │  /healthz │   │
    │   │  POST /api/*    │    │  Operations     │    │           │   │
    │   └─────────────────┘    └─────────────────┘    └───────────┘   │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │                      Production Infrastructure                  │
    ├─────────────────────────────────────────────────────────────────┤
    │                                                                 │
    │   ┌─────────────────┐    ┌─────────────────┐    ┌───────────┐   │
    │   │   Gunicorn      │    │   Render        │    │  GitHub   │   │
    │   │   WSGI Server   │    │   Cloud Host    │    │  Actions  │   │
    │   └─────────────────┘    └─────────────────┘    └───────────┘   │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘
```

---

## Features

### Matrix Operations
| Operation | Description | Constraints |
|-----------|-------------|-------------|
| **Determinant** | Computes determinant via NumPy (LU decomposition) | Square matrices only |
| **RREF** | Computes RREF using Gaussian elimination with partial pivoting | Any m×n matrix |

### Web Interface
- **Dynamic Matrix Input:** Adjustable rows and columns (2-10)
- **Real-time Validation:** Input validation before computation
- **Responsive Design:** Bootstrap-powered UI works on all devices
- **Clear Results:** Formatted output with operation details

### API Design
- RESTful JSON endpoints for programmatic access
- Proper HTTP status codes (200 OK, 400 Bad Request)
- Health check endpoint for container orchestration

### Production Infrastructure
- **CI/CD:** GitHub Actions runs linting and tests on every PR
- **Cloud Hosting:** Deployed on Render with auto-deploy from main
- **Process Management:** Gunicorn WSGI server for production
- **Health Checks:** `/healthz` endpoint for uptime monitoring

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| **Language** | Python 3.11+ |
| **Web Framework** | Flask 3.x |
| **Computation** | NumPy |
| **Frontend** | HTML5, CSS3 (Bootstrap), JavaScript |
| **WSGI Server** | Gunicorn |
| **Testing** | Pytest |
| **Linting** | Ruff |
| **CI/CD** | GitHub Actions |
| **Hosting** | Render |

---

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/yellepeddibk/matrix-calculator.git
cd matrix-calculator

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Locally

```bash
# Start the Flask development server
python webapp/app.py

# Open in browser
# http://localhost:5000
```

### Using the API

```bash
# Calculate determinant
curl -X POST http://localhost:5000/api/determinant \
  -H "Content-Type: application/json" \
  -d '{"matrix": [[1, 2], [3, 4]]}'

# Calculate RREF
curl -X POST http://localhost:5000/api/rref \
  -H "Content-Type: application/json" \
  -d '{"matrix": [[1, 2, 3], [4, 5, 6]]}'
```

---

## API Reference

### Health Check

```
GET /healthz
```

**Response:**
```json
{
  "status": "ok"
}
```

### Determinant Calculation

```
POST /api/determinant
```

**Request Body:**
```json
{
  "matrix": [[2, 4], [3, 1]]
}
```

**Response (200 OK):**
```json
{
  "result": -10.0
}
```

**Error Response (400 Bad Request):**
```json
{
  "error": "Matrix must be square"
}
```

### Reduced Row Echelon Form (RREF)

```
POST /api/rref
```

**Request Body:**
```json
{
  "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
}
```

**Response (200 OK):**
```json
{
  "result": [[1, 0, -1], [0, 1, 2], [0, 0, 0]]
}
```

---

## Project Structure

```
matrix-calculator/
├── .github/
│   └── workflows/
│       └── ci.yml              # CI pipeline (lint + test)
├── webapp/
│   ├── app.py                  # Flask application + API routes
│   ├── __init__.py             # Package marker
│   ├── templates/
│   │   └── matrix.html         # Web interface template
│   └── static/
│       ├── js/
│       │   └── matrix.js       # Frontend logic
│       └── css/
│           └── style.css       # Custom styling
├── tests/
│   ├── conftest.py             # Pytest fixtures
│   └── test_app_smoke.py       # Application tests
├── Procfile                    # Render/Heroku process definition
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── LICENSE                     # MIT License
└── README.md                   # This file
```

---

## Testing

The project includes smoke tests covering application initialization and API endpoints.

```bash
# Run all tests
pytest -v

# Run linter
ruff check .
```

### Test Coverage

| Test | Description |
|------|-------------|
| `test_app_imports` | Verifies Flask app initializes correctly |
| `test_app_is_flask_instance` | Confirms app is a Flask instance |
| `test_app_has_routes` | Validates all expected routes are registered |
| `test_healthz_endpoint` | Tests health check returns 200 OK |

---

## Deployment

### Render (Recommended)

1. Fork this repository to your GitHub account
2. Create a new **Web Service** on [Render](https://render.com)
3. Connect your GitHub repository
4. Configure build settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn webapp.app:app`
5. Deploy

The Procfile is already configured:
```
web: gunicorn webapp.app:app
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port (set by Render) | `5000` |

### Manual Deployment

```bash
# Install production dependencies
pip install -r requirements.txt

# Run with Gunicorn
gunicorn webapp.app:app --bind 0.0.0.0:$PORT
```

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/description`)
3. Make changes and add tests
4. Run linting (`ruff check .`)
5. Run tests (`pytest -v`)
6. Commit changes (`git commit -m "Add feature"`)
7. Push to branch (`git push origin feature/description`)
8. Open a Pull Request

---

## Future Enhancements

- [ ] Matrix multiplication endpoint
- [ ] Matrix inversion endpoint
- [ ] Eigenvalue/eigenvector computation
- [ ] Matrix rank calculation
- [ ] Step-by-step solution display
- [ ] API rate limiting
- [ ] OpenAPI/Swagger documentation

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

**Bhargav Yellepeddi** — [@yellepeddibk](https://github.com/yellepeddibk)