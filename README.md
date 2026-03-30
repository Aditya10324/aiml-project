# Movie Recommendation System

## Overview

This project is a content-based Movie Recommendation System developed
using Python. It recommends movies to users based on similarity in genre
and description using Natural Language Processing techniques.

The system processes textual movie data and suggests similar movies
along with their overview, helping users make informed decisions.

------------------------------------------------------------------------

## Problem Statement

With the increasing number of movies available, users often struggle to
decide what to watch. This project addresses that issue by recommending
movies similar to a given input, simplifying the selection process.

------------------------------------------------------------------------

## Features

-   Content-based recommendation system
-   Uses TF-IDF vectorization for text processing
-   Cosine similarity for computing movie similarity
-   Displays movie recommendations along with overview
-   Automatic dependency installation within the program
-   Simple command-line interface

------------------------------------------------------------------------

## Tech Stack

-   Python
-   Pandas
-   Scikit-learn

------------------------------------------------------------------------

## Installation

### Step 1: Clone the Repository

git clone
(https://github.com/Aditya10324/aiml-project)
------------------------------------------------------------------------

## Important Note on Dependencies

This project includes an automatic dependency installer inside the
Python script:
```python
import subprocess
import sys

def silent_install(packages):
    for pkg in packages:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", pkg],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)

silent_install(['pandas', 'scikit-learn'])

```
### What this means:

-   You do not need to manually install libraries
-   When you run the program, required packages are installed
    automatically
-   Installation happens silently (no terminal output)

------------------------------------------------------------------------

## Usage

Run the program using: python app.py

### Example:

Enter a movie name: Inception

### Output:

The system will display: - Recommended movie titles - Their overview
(description)

------------------------------------------------------------------------

## How It Works

1.  The dataset is loaded from a CSV file
2.  Important features (title, genre, overview) are combined
3.  Text data is converted into numerical form using TF-IDF
4.  Cosine similarity is computed between all movies
5.  Based on user input, the most similar movies are recommended

------------------------------------------------------------------------

## Requirements

-   Python 3.14
-   Internet connection (required only for first run to install
    dependencies)

------------------------------------------------------------------------

## Limitations

-   Recommendations depend on dataset quality
-   Does not consider user preferences or ratings
-   Content-based only (no collaborative filtering)

------------------------------------------------------------------------

## Future Improvements

-   Use larger datasets (IMDb, TMDb)
-   Add user-based recommendations
-   Improve similarity using more features (cast, director)
-   Develop a graphical user interface

------------------------------------------------------------------------

## Author

Name: Aditya Negi\
First Year B.Tech CSE\
VIT Bhopal University\
Registration Number: 25BCE10324
