from app import create_app

# solo arrancamos la app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)