# expense_tracker
A simple web application to track personal expenses.

## Features
- Add new expenses with description, amount, and category.
- View a list of all expenses.
- Delete expenses.
- API endpoint to fetch expenses data.

## Requirements
- Python 3.6 or higher
- Flask 2.0.1
- Gunicorn 20.1.0 (for production deployment)

## Installation
1. Clone the repository:
   git clone https://github.com/yourusername/expense_tracker.git
   cd expense_tracker

2. Create a virtual environment (optional but recommended):
   - On macOS/Linux:
     python3 -m venv venv
     source venv/bin/activate
   - On Windows:
     python -m venv venv
     venv\Scripts\activate


3. Install the dependencies:
   pip install -r requirements.txt

## Running the Application

### On macOS/Linux

1. Start the Flask application:
   python app.py
  

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

### On Windows

1. Start the Flask application:
   python app.py

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## API Endpoint

- To fetch expenses data, you can access the `/api/expenses` endpoint:
  GET http://127.0.0.1:5000/api/expenses

## Development

- The application uses Flask for the backend and HTML/CSS for the frontend.
- The expenses are stored in a JSON file named `data/expenses.json`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or issues, please open an issue on the GitHub repository.

### Additional Tips

- **Customize the README**: Feel free to customize the content of the `README.md` file to better fit your project's needs.
- **Add a License**: If you haven't already, consider adding a license file (`LICENSE`) to your project to specify the terms under which others can use your code.
- **Contribute**: Encourage others to contribute to your project by adding a "Contributing" section to your `README.md` file.

By including a `README.md` file with clear instructions, you make it easier for others to understand, install, and use your application.
