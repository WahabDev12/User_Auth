from flaskapp import create_app,db

# Instantiating app to create_app class in __init__.py file
app = create_app()
app.app_context().push()

# Run Flask app in DEBUG MODE
if __name__ == '__main__':
    db.create_all(app=create_app()) 
    app.run(debug=True)