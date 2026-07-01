# AUTOMATE DATA ANALYZER
#### Video URL: https://youtu.be/QfBwZAKI0LA
#### Description:
So, this project is a simple command-line interface (CLI) tool built with Python to help us analyze data from any CSV file automatically. It basically checks if our data is corrupted or not, calculates basic descriptive statistics, and performs linear regression to make predictions.

I decided to build this tool because cleaning data manually is super boring and time-consuming. To make this happen, I used the Pandas library to handle the data frames and the SciPy library to do all the heavy lifting for the statistical math and regression calculations.

### Key Features:
1. **Automated Data Validation**: The program acts like a gatekeeper. It will instantly reject a file if it has fewer than 3 rows, contains empty cells (Null/NaN), or if a numerical column accidentally contains text strings. It uses `pd.to_numeric` to make sure all data points are strictly numbers.
2. **Descriptive Statistics**: Once the data is verified and clean, the program automatically calculates the Mean, Median, and Standard Deviation for whatever variables the user chooses.
3. **Linear Regression Analysis**: It computes the exact prediction formula ($Y = mX + c$), finds the R-Squared value to see how strong the correlation is, calculates the P-Value, and prints an automated, easy-to-understand conclusion about how much variable X actually influences variable Y.

### Project Files:
* `project.py`: This is the main file that contains the entire program loop, user prompts, data validation logic, statistics functions, and the regression formula.
* `test_project.py`: A dedicated file to test all the core functions in `project.py` using `pytest`. This ensures the program behaves exactly as expected when fed both clean and corrupted data.
* `requirements.txt`: A simple text file listing the external libraries needed to run the app (`pandas`, `scipy`, `pytest`).