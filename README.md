# Matrix Calculator Web App

A Flask-powered web application for performing matrix computations including determinant calculation and Reduced Row Echelon Form (RREF).

**Live Demo:** _Coming soon_

## Features

- **Modern Web Interface:** Built with HTML, CSS (Bootstrap), and JavaScript
- **Matrix Computation API:**
  - `/api/determinant` – Computes the determinant of a square matrix
  - `/api/rref` – Computes the Reduced Row Echelon Form
- **Dynamic Input:** Adjustable matrix dimensions with real-time validation
- **Responsive Design:** Works across desktop and mobile devices

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yellepeddibk/matrix-calculator.git
cd matrix-calculator

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python webapp/app.py
```

Open http://127.0.0.1:8000 in your browser.

---

## Project Structure
```
matrix-calculator/
├── webapp/
│   ├── app.py              # Flask backend
│   ├── templates/
│   │   └── matrix.html     # Web interface
│   └── static/
│       ├── js/
│       │   └── matrix.js   # Frontend logic
│       └── css/
│           └── style.css   # Styling
├── tests/
│   ├── conftest.py         # Pytest configuration
│   └── test_app_smoke.py   # Smoke tests
├── requirements.txt        # Python dependencies
└── README.md
```

---

## API Endpoints

### Determinant Calculation
- **Endpoint:** `POST /api/determinant`
- **Request Body:**
```json
{
  "matrix": [[2, 4], [3, 1]]
}
```
- **Response:**
```json
{
  "result": -10.0
}
```

### Reduced Row Echelon Form (RREF)
- **Endpoint:** `POST /api/rref`
- **Request Body:**
```json
{
  "matrix": [[1, 2], [3, 4]]
}
```
- **Response:**
```json
{
  "result": [[1, 0], [0, 1]]
}
```

---

## Requirements

- Python 3.11+
- Flask
- NumPy
- Gunicorn (for production)

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## Development

```bash
# Run linter
ruff check .

# Run tests
pytest -v
```

---

## Deploy on Render

1. Connect your GitHub repo to [Render](https://render.com)
2. Create a new **Web Service**
3. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn webapp.app:app`
4. Deploy and get your live URL

---

## Future Enhancements

- Additional matrix operations (inversion, multiplication, rank)
- Expanded API capabilities

---

## License

MIT License

## Author

**Bhargav Yellepeddi** — [@yellepeddibk](https://github.com/yellepeddibk)