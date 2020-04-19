# fifa_preprocessing
*fifa_preprocessing* is a module which provides methods conceived to preprocess data stored in csv files etc., with the intent to perform data analysis and Machine Learning.

GitHub Pages: https://piotrfratczak.github.io/fifa_preprocessing/  <br />
PyPI:         https://pypi.org/project/fifa-preprocessing/

## Table of contents
* [General Info](#general-info)
* [Acknowledgements](#acknowledgements)
* [Technologies and Dependencies](#technologies-and-dependencies)
* [Installation](#installation)
* [Functions](#functions)
* [Documentation](#documentation)
* [Tutorial](#tutorial)
* [Testing](#testing)
* [Status](#status)
* [Authors](#authors)
* [License](#license)


## General Info
The module was originally created to preprocess data from the EA Sports' FIFA 19 for a Machine Learning project to predict players' wages by regression. Therefore it contains functions that can be universally used for data preprocessing but also functions that are made specifically with the FIFA 19 data set in mind.

## Acknowledgements
This project was created to use FIFA 19 data set, containing information about players in the game. It is strongly advised to use the same dataset to use this module to its full potential. The data set is shared by Karan Gadiya on https://www.kaggle.com/karangadiya/fifa19.

The data set is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License, which makes it unconvenientto include it in the package, because it would strongly constrain the possibilities to use this package.

## Technologies and Dependencies
The module was written in Python 3.6 and requires 'pandas' to be installed in used environment.

Required libraries:
* math
* pandas

Math library comes with a python distribution, pandas, on the other hand, has to be installed to run *fifa_preprocessing*.
To install pandas with pip:
```
$ pip install pandas
```

## Installation
*fifa_preprocessing* can be easily installed with pip:
```
$ pip install fifa-preprocessing
```

## Functions
The module consists of data preprocessing functions:
* Removing goalkeepers from data frame
* Data type converters
* Reformatting data
* spliting columns
* Converting to dummy variables
* Default preprocessing function for FIFA 19 data set

## Documentation
Full documantation of *fifa_preprocessing* can be found on its [readthedocs website](https://fifa-preprocessing.readthedocs.io/).

## Tutorial
This [tutorial](https://github.com/piotrfratczak/fifa_preprocessing/blob/master/tutorial/tutorial.ipynb) should help you start using our module!

## Testing
To execute tests on the mudule's functions run:
```
$ python3 -m doctest -v fifa_preprocessing.py 
```

## Status
Project is curently in progress.

## Authors
This package was created by [Piotr Frątczak](https://github.com/piotrfratczak) and [Jakub Płudowski](https://github.com/jpludowski), students at Warsaw University of Technology.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/piotrfratczak/fifa_preprocessing/blob/master/LICENSE) file for details. <br /> 
We chose this license for every one to feel free to use our code, tweak it and expand on it.
