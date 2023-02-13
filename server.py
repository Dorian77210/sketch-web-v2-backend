import pandas as pd

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)
    