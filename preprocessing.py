import math
import pandas as pd

"""This module provides methods adapted to preprocess FIFA19 data set to enable performing Machine Learning on it.
"""

def exclude_goalkeepers(data_frame):
    """boolean: Indicate whether or not to include goalkeepers in the data. """
    goalkeepers = data_frame[data_frame['Position'] == 'GK']
    data_frame.drop(goalkeepers.index, inplace=True)
    return data_frame


def money_format(money):
    """Convert monetary amount string into an integer.
    
    Remove unnecessary characters.    
    Values are expressed in thousands of euros.

    Returns
    -------
    money : int
        Integer value of the monetary amount.
    """
    money = money.replace('€', '')
    if 'M' in money:
        money = money.replace('M', '')
        return int(float(money)*1000)
    money = money.replace('K', '')
    return int(money)

    
def rating_format(rating):
    """Convert strings of type x+y into an integer equal to the sum.

    Ratings in FIFA are expressed as a sum of two numbers.

    Returns
    -------
    rating : int
        Integer value of the rating.
    """
    if type(rating) is not str:
        return 0
    elif '+' in rating:
        plus = rating.index('+')
        base = int(rating[:plus])
        add = int(rating[plus + 1:])
        return base + add
    else:
        return int(rating)


def work_format(work):
    """Convert categorical variables to numerical.

    Returns
    -------
    int
        Integer value of the work rate (0/1/2).
    """
    if work == 'High':
        return 2
    elif work == 'Medium':
        return 1
    else:
        return 0


def to_int(not_int):
    """Convert an object that represents a number into a number.
    
    Returns
    -------
    int
	Integer value of the passed object. If the passed object doesnt represent a number return 0.
    """
    if math.isnan(not_int):
        return 0
    else:
        return int(not_int)


def apply_format(data_frame, column_names, format_method):
    for column in column_names:
        if isinstance(column, str) and (column in data_frame) and callable(format_method):
            data_frame[column] = data_frame[column].apply(format_method)
    return data_frame


def to_dummy(data_frame, column_names):
    for column in column_names:
        if isinstance(column, str) and column in data_frame:
            dummies = pd.get_dummies(data_frame[column])
            data_frame = pd.concat([data_frame, dummies])
            data_frame = data_frame.drop([column], axis=1)
    return data_frame


def split_work_rate(data_frame):
    data_frame.rename(columns={'Work Rate': 'Work'}, inplace=True)
    data_frame[['Defensive Work Rate', 'Offensive Work Rate']] = data_frame.Work.str.split('/ ', expand=True)
    data_frame = data_frame.drop('Work', axis=1)
    return apply_format(data_frame, ['Defensive Work Rate', 'Offensive Work Rate'], work_format)


def preprocess(source_file):
    """Preprocess data to be able perform regression with decision tree.

    Drop attributes unrelated to the target.
    Convert attribute types.
    Manage column representation of attributes.

    Parameters
    ----------
    source_file : str
        File path of the data source file.

    Returns
    -------
    data : pandas.DataFrame
        Preprocessed data, ready to perform regression on it.
    """
    data = pd.read_csv(source_file)

    # Drop useless attributes.
    # Unnamed: 0 is an index (0 - n); ID - FIFA 19 internal id; Photo, Flag and Club Logo are images.
    # Real Face - Yes/No value if the game uses a 3D scan of the actual face of the player.
    # Loaned From is usually missing, duration of the contract and date of joining the club are not essential.
    # Name and body parameters are not correlated to wage.
    data = data.drop(['Unnamed: 0', 'ID', 'Name', 'Photo', 'Flag', 'Club Logo', 'Loaned From', 'Height', 'Weight',
                      'Body Type', 'Real Face', 'Joined', 'Contract Valid Until'], axis=1)

    # Exclude goalkeepers based on the boolean variable - exclude_goalkeepers.
    data = exclude_goalkeepers(data)
    
    # Compute ratings on specific positions on the field and on football skills.
    for label in data.columns[15:41]:
        data[label] = data[label].apply(rating_format)
    for label in data.columns[41:75]:
        data[label] = data[label].apply(to_int)

    # Drop rows with missing values.
    data.dropna(inplace=True)

    # Convert monetary amounts.
    data = apply_format(data, ['Wage', 'Value', 'Release Clause'], money_format)

    # Convert floats to int as the nature of this information ('Jersey Number', 'International Reputation', 'Skill Moves', 'Weak Foot') is discrete.
    data = apply_format(data, ['Jersey Number', 'International Reputation', 'Skill Moves', 'Weak Foot'], to_int)

    # Convert categorical data to dummy variables.
    # DecisionTreeRegressor does not work when categorical variables are used.
    data = to_dummy(data, ['Preferred Foot', 'Club', 'Position', 'Nationality'])

    # Split work rate into defensive and offensive work rate.
    data = split_work_rate(data)

    return data


def demo():
    print(preprocess.__doc__)
    import matplotlib.pyplot as plt
    
    data = preprocess('fifa19_data.csv')
    # Relation Between Jersey Number and Wage of a Player
    fig = data.plot(kind='scatter', x='Wage', y='Jersey Number', color='blue')
    fig.set_title("Relation Between Jersey Number and Wage of a Player")
    fig.set_xlabel('Wage [k€]')
    fig = plt.gcf()
    plt.show()


if __name__ == '__main__':
    demo()

