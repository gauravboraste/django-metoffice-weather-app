#Climate Data Project
**Project Name**
-Create a Django Application to parse summarised weather data from UK MetOffice and serve it via API.
A Django-based web application for retrieving and visualizing climate data from the Met Office.

**Overview**
This project provides a user-friendly interface for fetching climate data from the Met Office API and storing it in a database. The application allows users to select a region, parameter, and year to retrieve the corresponding climate data. The data is then visualized using a line chart to show the monthly values for the selected parameter.

**Main link for Region and Parameter selection:** 
https://www.metoffice.gov.uk/research/climate/maps-and-data/uk-and-regional-series#yearOrdered

**For example**
https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt

**Features**
1) Retrieves climate data from the Met Office API
2) Stores data in a database for future reference
3) Allows users to select a region, parameter, and year to retrieve data
4) Visualizes data using a line chart
5) Supports multiple parameters and regions


**Evaluation:**
1) Project Setup
2) Data parsing (Parsing and data handling)
3) Data modelling (Storing into database locally)
4) API (Serving via Restful APIs)
5) Tests

**Getting Started**
1) Clone the repository: git clone https://github.com/your-username/climate-data-project.git
2) Install the required packages: pip install -r requirements.txt
3) Run the development server: python manage.py runserver
4) Open the application in your web browser: http://localhost:8000


**Usage**
1) Select a region, parameter, and year from the dropdown menus.
2) Click the "Fetch Data" button to retrieve the climate data.
3) The data will be displayed in a line chart, showing the monthly values for the selected parameter.

**Technical Details**
1) Built using Django 3.2 and Python 3.9
2) Uses the Met Office API to retrieve climate data
3) Stores data in a SQLite database
4) Uses Matplotlib to generate line charts
5) Supports multiple browsers and devices


**Acknowledgments**
1) Met Office for providing the climate data API
2) Django and Python communities for their support and resources
