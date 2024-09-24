# Django Project Setup

This document will guide you through setting up and running the Django project on your local machine.

## Prerequisites

Ensure that the following tools are installed on your system:

- Python (3.10+)
- Pip (Python package manager)
- Virtualenv (recommended)

## Getting Started

1. **Create and activate a virtual environment**:
   It's recommended to use a virtual environment to manage your dependencies.

   For Linux/macOS:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   For Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the dependencies**:
   After activating the virtual environment, install all the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   Before running the project, apply the migrations to set up the database schema.

   ```bash
   python manage.py migrate
   ```

5. **Load the fixture data**:
   After running migrations, load the initial data from the fixture file into the database:

   ```bash
   python manage.py loaddata load_sample_data.json
   ```

6. **Run the development server**:
   Start the Django development server to view the project locally:

   ```bash
   python manage.py runserver
   ```

87 **Access the application**:
   Open a web browser and navigate to:

   ```
   http://127.0.0.1:8000/
   ```

## Troubleshooting

- Ensure your virtual environment is activated when installing dependencies or running commands.
- If you encounter any errors related to migrations, try resetting the migrations by running:

   ```bash
   python manage.py migrate --fake
   ```

After the backend server is up and running,  go to charts-app folder

    cd charts-app
    
    

# Getting Started with React App

In the project directory, you can run:

### `npm install`

Install the required packages to run this frontend application

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

