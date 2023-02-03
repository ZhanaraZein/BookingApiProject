# Booking API Project

Booking API Project is an end-to-end data analytics pipeline, which provides processing and analysis based on star ratings, overall ratings, reviews and locations from the Booking API.
The main objective of the project is to develop a search function in Python for users to find hotels, apartments and other accomodations in Prague based on specified criteria through a website [Booking.com](https://www.booking.com/index.ru.html?aid=304142&label=gen173nr-1BCAEoggI46AdIM1gEaDqIAQGYASG4ARfIAQzYAQHoAQGIAgGoAgO4Au2m754GwAIB0gIkZDg4ZWE5ODEtYWJjYi00Njk3LTg3MzMtNGVhYWY5NTgzMzhh2AIF4AIB&sid=44632f1b92082830e0652acb584d3335&) programmatically.

# How to Install and Run the Project

Requirements to run the project can be found in [Requirements.txt](https://github.com/ZhanaraZein/BookingApiProject/blob/main/Requirements.txt).

### Step 1: Run the analysis using the script [BookingAPI-(Prague-Properties)_300123](BookingAPI-(Prague-Properties)_300123.py)

* Clone the repository.
* Specify the path to the folder where the script is saved by writing "cd folder_adress". Press Enter.
* Open Command Prompt and install the following library by writing "pip install -r requirements.txt". Press Enter.
* When the folder is specified, write "python "BookingAPI-(Prague-Properties)_300123.py" outputdir". Press Enter.

Database files and visualizations will be saved automatically in the folder "data".

### Step 2: Run the search function using the script [BookingAPI_on_Query](https://github.com/ZhanaraZein/BookingApiProject/blob/main/BookingAPI_on_Query.py)

* Open Command Prompt and specify the path to the folder where the scrip is saved by writing "cd folder adress". Press Enter. If the path is specified ignore this step.
* When the folder is specified, write "python "BookingAPI_on_Query.py" outputdir". Press Enter.

# How to Use The Query Script

The user should answer the following questions:
* How many children?
* How many guests?
* How many rooms?

Then the user should specify the date of departure and the date of arrival in the format: yyyy-mm-dd.
Departure date must be after arrival date.
Arrival date must be today or the future date.

The list of available offers with necessary information will be shown in Command Prompt.

# Project Contributors

| No  | Author | Email Adress |
| ------------- | ------------- | ------------- |
| 1  | Dastan Pirmat  | 23055687@fsv.cuni.cz |
| 2  | Zhanara Zeinesheva  | 81386056@fsv.cuni.cz |



##### THIS PROJECT WAS MADE EXCLUSIVELY FOR EDUCATIONAL PURPOSES! THE USE OF THE PROJECT FOR COMMERCIAL PURPOSES IS STRICTLY PROHIBITED!

