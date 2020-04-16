# fifa_preprocessing
This module provides methods conceived to preprocess data stored in a csv file etc., with the intent to perform data analysis and Machine Learning.

## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Data](#data)
* [Running](#running)
* [Functions](#functions)
* [Status](#status)
* [Authors](#authors)


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
## Data
Data set is scrapped from https://www.kaggle.com/karangadiya/fifa19

## Running
If program is run directly it will return a graph. 

If being imported, it will display all possible functions.

## Functions
Already done functions:
* Loading data set from Fifa 19
* Removing goalkeepers from data
* Some data type converters

## Status
Project is curently in progress.

## Authors
Piotr Fratczak, Jakub Pludowski
