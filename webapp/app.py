from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Serve the HTML template
@app.route("/")
def index():
    return render_template("matrix.html")

# API endpoint for determinant calculation
@app.route("/api/determinant", methods=["POST"])
def determinant():
    matrix = request.json["matrix"]
    np_matrix = np.array(matrix, dtype=float)

    if np_matrix.shape[0] != np_matrix.shape[1]:
        return jsonify({"error": "Matrix must be square"}), 400

    det = float(np.linalg.det(np_matrix))
    return jsonify({"result": det})

# API endpoint for RREF calculation
@app.route("/api/rref", methods=["POST"])
def rref():
    matrix = request.json["matrix"]
    np_matrix = np.array(matrix, dtype=float)

    rref_matrix = compute_rref(np_matrix)
    return jsonify({"result": rref_matrix.tolist()})

def compute_rref(matrix: np.ndarray) -> np.ndarray:
    rref = matrix.copy().astype(float)
    m, n = rref.shape
    row = 0

    for col in range(n):
        if row >= m:
            break

        pivot = np.argmax(np.abs(rref[row:, col])) + row
        if rref[pivot, col] == 0:
            continue

        rref[[row, pivot], :] = rref[[pivot, row], :]
        rref[row, :] /= rref[row, col]

        for r in range(m):
            if r != row:
                rref[r, :] -= rref[r, col] * rref[row, :]

        row += 1

    return rref

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
