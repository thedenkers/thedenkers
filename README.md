# SIH - Virtual Tourist Guide for Goa

This is a part of participation in Smart India Hackathon 2020.

**Progress reports are given in text files *Progress_Report_1.txt*, *Progress_Report_2.txt*. *Progress_Report_Final.txt***

## Basic Information

- **Organization:** Govt. of Goa
- **Team Name:** The Denkers
- **Team Members:**
  - Asmita Khode(Team Leader)
  - Anurag Deshmukh
  - Nikhil Soni
  - Purvesha
  - Suraj Satankar
  - Vinod Kumar Gupta

## Introduction

Virtual Tourist Guide is a mobile application which is developed to help tourist in Goa.
This application will guide the tourist throughout the journey.
Through this application the user can get information about any tourist place just by clicking the picture of the place.
The User can also share and rate the place by signing up.
The Govt of Goa will be benefitted from the project by keeping a statistics of the user activity.

## Technology Stack

- Android(kotlin) - for mobile
- Python 3 - for creating API and ML related work
- Flask Framework - for web and API calling
- Tensorflow Lite - for image recognition
- MongoDB - for information about monuments and user account management

## Steps to run the application

As the Android codebase is seperately maintained by Nikhil Soni, this guide is for flask app only.

- create a virtual environment *(Skip is already created)*

    `python3 -m venv venv`

- log into virtual environment

    **for linux**

    `source venv/bin/activate`

    **for windows**

    `venv\Scripts\activate`

- install required modules

    `pip install -r requirements.txt`

- run the app

    `flask run`

- browse http://localhost:5000/

## License

This project or part of this project is a property of team members of this project.
The source code or contents of the project should not be used in any other project/work/purpose.
