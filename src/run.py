from flaskMoviesApp import app

# ελέγχει εάν ένα αρχείο Python εκτελείται απευθείας ή εισάγεται από άλλο αρχείο
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8003)
