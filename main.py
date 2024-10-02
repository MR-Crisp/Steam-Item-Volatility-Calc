from website import create_app # imports from the website folder as there is an '__init__.py' file

app = create_app()

if __name__== '__main__':
    app.run(debug=True)
