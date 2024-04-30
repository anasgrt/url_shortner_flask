# Shortner URL Webservice Application - Flask
This repo contains a webservice application which can shorten urls like TinyURL and bit.ly

## Basic virtual environment with the necessary python libraries setup:

- Install the virtual environment in python (basically to avoid installing the packages globally)

```jsx
pip install virtualenv
```

- create the virtual environment

```jsx
python -m venv venv
```

- Source the virtual environment

```jsx
source venv/bin/activate
```

- Check which environment is used now

```jsx
which python3
```

## Instructions to start the application:

- Make sure you have Python installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

- Install packages listed in a requirements.txt file using pip - preferably in Virtual Environment!

```jsx
pip install -r requirements.txt
```
- You can run the Python application now by executing the **`app.py`** file. Use the following command:

```jsx
python app.py
```
- Access the Application:
Once the server is running, you can access the application by opening a web browser and navigating to http://127.0.0.1:5000/ .<br>
If everything is set up correctly, you should see the home page of the URL shortener application. <br>
You can also test other endpoints such as http://127.0.0.1:5000/shortcode and http://127.0.0.1:5000/shortcode/stats to verify their functionality.

- To stop the Flask development server, you can press Ctrl + C in the terminal where the server is running. This will terminate the server and stop the application.

# Github Actions Pipelines Test Pipelines:

This repository contains a GitHub Actions workflow for testing a Python Flask application with different Python versions:

## Usage

To use this GitHub Actions workflow, follow these steps:

1. Clone this repository and create a branch.
2. Make sure your Python Flask application is set up correctly with appropriate tests.
3. Modify the workflow file (`flask-test.yml`) if needed or add more tests on tests directory in the repo if needed.
4. Commit your changes and push them to your repository.
5. Trigger the workflow manually or wait for it to run automatically on push or pull request events.

### <ins>Test Note:</ins>

If you have more than one file in the tests directory, the unittest discover command will search recursively through the directory and its subdirectories to find all files that match the specified pattern (*_test.py). It will then execute all the test cases found in those files.

## The GitHub Actions Workflow:

This repository includes a GitHub Actions workflow (`flask-test.yml`) that runs tests for a Python Flask application using different Python versions. The workflow performs the following steps:

- Checks out the repository.
- Sets up the specified Python version using the `setup-python` action.
- Installs dependencies from the `requirements.txt` file.
- Runs tests using the `unittest` framework.

**`You can customize the Python version by selecting an option when triggering the workflow manually.Default option is set on Python version 3.12`**