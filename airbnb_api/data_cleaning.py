"""
Contains wrangle function to create boolean columns for common amenities
"""

import pandas as pd


def wrangle(df):
    """
    Takes the dataframe created in app.py and creates boolean columns
    for most common amenities
    """
    # List of most frequent amenities
    top_amenities_list = ['Wifi', 'Kitchen', 'Heating', 'Essentials',
                          'Hair dryer', 'Laptop friendly workspace',
                          'Hangers', 'Iron', 'Shampoo', 'TV', 'Hot water',
                          'Internet', 'Host greets you', 'Smoke detector',
                          'Buzzer/wireless intercom', 'Lock on bedroom door',
                          'Refrigerator', 'Free street parking',
                          'Dishes and silverware']
    # Copying dataframe to prevent errors
    df = df.copy()

    # loop to create Boolean columns for each amenity
    for amenity in top_amenities_list:
        df[amenity] = df['amenities'].str.contains(amenity)

    # Dropping column that contained all amenities
    df = df.drop(columns='amenities')

    return df
