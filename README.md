# fifa_preprocessing
This module provides methods conceived to preprocess data stored in csv files etc., with the intent to perform data analysis and Machine Learning.

## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Acknowledgements](#acknowledgements)
* [Running](#running)
* [Functions](#functions)
* [Tutorial](#tutorial)
* [Testing](#testing)
* [Status](#status)
* [Authors](#authors)
* [License](#license)


## General Info
It was originally created to preprocess data from the EA Sports' FIFA 19 for a Machine Learning project to predict players' wages by regression. Therefore it contains functions that can be universally used for data preprocessing but also functions that are made specifically with the FIFA 19 data set in mind.

## Technologies
It was written in Python 3.6 and requires 'pandas' to be installed in used environment. Also it requires 'matplotlib.pyplot' be installed if it is run as main.
Used libraries:
* math
* pandas

To install use:
```
$ import math
$ import pandas as pd
```
## Acknowledgements
This project was created to use FIFA 19 data set, containing information about players in the game. It is strongly advised to use the same dataset to use this module to its full potential. The data set is shared by Karan Gadiya on https://www.kaggle.com/karangadiya/fifa19.

The data set is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License, which makes it unconvenientto include it in the package, because it would strongly constrain the possibilities to use this package.

## Running
If program is run directly it will return a graph. 

If being imported, it will display all possible functions.

## Functions
Already done functions:
* Loading data set from Fifa 19
* Removing goalkeepers from data
* Some data type converters

## Tutorial
This [tutorial](tutorial.ipynb) should help you start using our module!

## Testing
To execute tests on the mudule's functions run:
```
$ python3 -m doctest -v preprocessing.py 
```

## Status
Project is curently in progress.

## Authors
Piotr Frątczak, Jakub Płudowski

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
