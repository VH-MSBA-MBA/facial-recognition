# Purpose

This is a quick and dirty, no frills Django web application for a Masters of Science in Business Analytics final project. It is just meant to demonstrate [AWS Rekognition](https://aws.amazon.com/rekognition/?blog-cards.sort-by=item.additionalFields.createdDate&blog-cards.sort-order=desc) for cloud technology project.

This application will ask to access your camera. If you consent, and take a picture of yourself, you can submit the picture. Rekognition will analyze and return characteristics about the picture such as mood, gender, age, etc.

# Installation

## Python

This assumes you already have Python installed, particularly Pythong 3.8. Check your version with:

```
python --version

# or 

python3 --version
```

## Virtual Environment

It is recommended to create a Python virtual environemnt when deploying this application locally. I use [virtualenv](https://virtualenv.pypa.io/en/latest/), but anything similar will be fine.

For `virtualenv` run one of the following commands:

```
pip install virtualenv

# or

pip3 install virtualenv
```

## Installing the Application

Follow these steps to get the application running locally.

1. Clone the repo:

   ```
   git clone https://github.com/cheslijones/facial-recognition.git
   ```

2. Change into the directory:

   ```
   cd facial-recognition
   ```

3. Create the virtual environment (assuming you are using `virtualenv` and have Python 3.8 installed):

    ```
    virtualenv -p python3 .venv
    ```

4. Activate the virtual environment (again, assuming you are using `virtualenv`):

    ```
    source .venv/bin/activate
    ```

5. Install the application dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Start-up the application:

   ```
   ./manage.py runserver
   ```

7. Finally, in the browser you can navigate to the following IP and port to interact with the running application: `127.0.0.1:8000`. 

# Deploying the Application
