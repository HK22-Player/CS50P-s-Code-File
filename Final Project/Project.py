import pandas as pd
from scipy import stats
import sys

def main():
    print("Data Analyzer")
    try:
        df_raw = pd.read_csv(input("Name of the File: "))

        df = data_validation(df_raw)
        print("Data is Valid and Ready for Analysis!")

        print(f"Available columns: {list(df.columns)}")
        x_col = input("Choose Variable X (Independent): ")
        y_col = input("Choose Variable Y (Dependent): ")

        mean_x, median_x, std_x = statistic_descriptive(df, x_col)
        mean_y, median_y, std_y = statistic_descriptive(df, y_col)
        print("Statistic Descriptive Results")
        print(f"Stats X ({x_col}) get Mean = {mean_x:.4f}, Median = {median_x}, and Standart Deviation = {std_x}")
        print(f"Stats Y ({y_col}) get Mean = {mean_y:.4f}, Median = {median_y}, and Standart Deviation = {std_y}")

        regression_result = linear_regression(df, x_col, y_col)
        print("Linear Regression Results")
        print(f"Regression Formula  : Y = {regression_result['slope']:.4f}X + ({regression_result['intercept']:.4f})")
        print(f"R-Squared Value     : {regression_result['r_squared']:.4f} which means ({regression_result['r_squared'] * 100:.2f}% Variable Y is influenced by Variable X)")
        print(f"Probability Value   : {regression_result['p_value']:.4f}")
        print(f"Standard Error      : {regression_result['std_err']:.4f}")

        r_squared = regression_result['r_squared']
        if r_squared == 0:
            print("Conclusion: Variable X doesn't influence Variable Y")
        elif 0 < r_squared < 0.25:
            print("Conclusion: Variable X has a very weak influence on Variable Y")
        elif 0.25 <= r_squared < 0.5:
            print("Conclusion: Variable X has a weak influence on Variable Y")
        elif 0.5 <= r_squared < 0.75:
            print("Conclusion: Variable X has a moderate influence on Variable Y")
        elif 0.75 <= r_squared < 0.9:
            print("Conclusion: Variable X has a strong influence on Variable Y")
        elif 0.9 <= r_squared < 1:
            print("Conclusion: Variable X has a very strong influence on Variable Y")
        else:
            print("Conclusion: Variable X has a perfect influence on Variable Y")
        print("Analysis has done")

    except FileNotFoundError:
        print("File Not Found!")
        sys.exit(1)
    except ValueError as inside_error:
        print(f"Error: {inside_error}")
        sys.exit(1)
    except Exception as outside_error:
        print(f"System Error: {outside_error}")
        sys.exit(1)

def data_validation(s):
    if len(s) < 3:
        raise ValueError("Too Few Data")
    if s.isnull().values.any():
        raise ValueError("There is Null Data")
    for column in s.columns:
        try:
            pd.to_numeric(s[column], errors='raise')
        except (ValueError, TypeError):
            raise ValueError("There is Text Data")
    return s

def statistic_descriptive(s, column):
    if column not in s.columns:
        raise ValueError("Data Not Found!")
    mean = s[column].mean()
    median = s[column].median()
    standart_deviation = s[column].std()
    return mean, median, standart_deviation

def linear_regression(s, x_col, y_col):
    if x_col not in s.columns or y_col not in s.columns:
        raise ValueError("Column X or Y not found in the data!")
    X = s[x_col]
    Y = s[y_col]
    slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
    r_squared = r_value ** 2
    return {
        "slope": slope,
        "intercept": intercept,
        "r_value": r_value,
        "r_squared": r_squared,
        "p_value":p_value,
        "std_err":std_err}

if __name__ == "__main__":
    main()