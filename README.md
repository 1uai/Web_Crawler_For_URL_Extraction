<pre>
SQL Injection Scanner

This project is a SQL Injection Scanner built with Flask to help detect vulnerabilities in web forms by simulating different types of SQL injection attacks. It extracts forms from a target website, allows users to select form fields, and tests them using various SQL injection payloads.
Features

    Extracts and displays input forms from a given URL.
    Provides options to choose specific form fields for SQL injection testing.
    Supports multiple SQL injection types including:
        In-band SQL Injection
        Union-based SQL Injection
        Error-based SQL Injection
        Time-based Blind SQL Injection
        Authentication Bypass Payloads
    Sends injected forms with payloads and analyzes the response for SQL injection vulnerabilities.

Project Structure

bash

/SQL_Injection_Scanner
│
├── /static
│   └── /CSS                  # Contains CSS styles for the front-end.
│
├── /templates
│   └── /HTML                 # Contains HTML templates for the Flask app.
│
├── Flask_app.py               # Main Flask application for running the scanner.
├── Payloads_Of_SQL.py         # Contains all the SQL injection payloads used in the scanner.
├── Forms_Extraction.py        # Extracts input forms from the target website using Selenium.

Installation

    Clone this repository:

    bash

git clone https://github.com/YourUsername/SQL_Injection_Scanner.git

Navigate to the project directory:

bash

cd SQL_Injection_Scanner

Install required dependencies:

bash

    pip install -r requirements.txt

    Make sure to have a Selenium WebDriver (e.g., chromedriver or geckodriver) installed and configured for extracting forms.

Usage

    Start the Flask server:

    bash

    python Flask_app.py

    Open your web browser and go to http://localhost:5000.

    Enter the URL of the target website. The app will display the forms found on the page.

    Select a form, choose input parameters to inject, and choose the type of SQL injection attack.

    The app will perform the attack and display the results of the scan.

SQL Injection Types

    In-band SQL Injection: Directly executes queries and retrieves data in the same communication channel.
    Union-based SQL Injection: Uses the UNION operator to extract information.
    Error-based SQL Injection: Forces the database to display errors that reveal vulnerabilities.
    Time-based Blind SQL Injection: Exploits a time delay to infer vulnerabilities when no visible output is returned.
    Authentication Bypass Payloads: Attempts to bypass login forms using SQL injection.

Requirements

    Python 3.x
    Flask
    BeautifulSoup
    Selenium
    Requests

Contribution

Feel free to fork this repository, submit issues, and make pull requests. Contributions are welcome!
License

This project is licensed under the MIT License.
</pre>
