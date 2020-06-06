from sistema import app
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

if __name__ == "__main__":
    app.run(debug=True)
    csrf.init_app(app)