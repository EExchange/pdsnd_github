"""
   Github link:https://github.com/EExchange/pdsnd_github.git
"""
import time
import pandas as pd
import numpy as np
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
df = pd.read_csv('chicago.csv')
month_ls = ['all','january','february','march','april','may','june','july','august','september','october','november','december']
day_ls = ['all', 'monday', 'tuesday','wednesday','thursday','friday','saturday','sunday']
def get_filters():
    """
   Specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analysis
        (str) month - name of the month to filter by, or "all" to apply for month filter
        (str) day - name of the day of week to filter by, or "all" to apply for day filter
    """
    print('Hi! Let\'s explore US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input(
                '1. Enter the name of the city to start analysing:(eg. "Chicago","New York City","Washington"')).lower()
            city_ls = ['chicago', 'new york city', 'washington']
            if city in city_ls:
                break
            else:
                print('There\'s no data of {}!'.format(city))
                continue
        except:

            print('ERROR: There\'s no data of {}!'.format(city))
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input("2. Enter the month: (eg. all, January, February, ... , June).")).lower()

            if month in month_ls:
                break
            else:
                print('ERROR: Input value should be "all, January, February, ... , June!"')
                continue
        except:
            print('ERROR: Input value should be "all, January, February, ... , June!"')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input("3. Enter the day of week: (eg. all, Monday, Tuesday, ... Sunday).")).lower()

            if day in day_ls:
                break
            else:
                print('ERROR: Input value should be "all, Monday, Tuesday, ... Sunday!"')
                continue
        except:
            print('ERROR: Input value should be "all, Monday, Tuesday, ... Sunday!"')
            continue
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if application.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply for month filter
        (str) day - name of the day of week to filter by, or "all" to apply for day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv('chicago.csv')

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # extract hour afrom Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Display statistic on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = month_ls[df['month'].mode()[0]].title()
    print('The most common month is:')
    print("---->",month)

    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0].title()
    print('The most common day is:')
    print("---->",day)

    # TO DO: display the most common start hour
    hour = df['hour'].mode()[0]
    print('The most common hour is:')
    print("----> at",hour,"o' clock")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Display statistic on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Station_start = df['Start Station'].mode()[0].title()
    print('The most commonly used start station is:')
    print("---->", Station_start)

    # TO DO: display most commonly used end station
    Station_end = df['End Station'].mode()[0].title()
    print('The most commonly used end station is:')
    print("---->", Station_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_trip']= "From  ["+df['Start Station'] +"]  To  ["+ df['End Station']+"]"
    comb_trip = df['combination_trip'].mode()[0].title()
    print('The most frequent combination of start station and end station trip is:')
    print("---->", comb_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Display statistic on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = int(df['Trip Duration'].sum())
    print('The total travel time is:')
    print("---->", total_time,"Sec.")

    # TO DO: display mean travel time
    mean_time = int(df['Trip Duration'].mean())
    print('The total travel time is:')
    print("---->", mean_time,"Sec.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Display statisti on bikeshare user."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:')
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print('Counts of user Gender:')
        print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of birth:')
        print("---->",int(df['Birth Year'].min()))
        print('Most recent year of birth:')
        print("---->", int(df['Birth Year'].max()))
        print('Most common year of birth:')
        print("---->", int(df['Birth Year'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):
    """Display function for more detail information """
    print('Would you like to view more detail information?')
    index_start = 0
    while True:
        try:
            answer = str(input(
                'Show  5 items more? Yes or No?')).lower()
            answer_ls = ['yes', 'no']
            if answer == 'yes':

                index_end = index_start+5
                if df.shape[0]<index_end:
                    index_end = df.shape[0]
                print(df.iloc[index_start:index_end])

                if index_end == df.shape[0]:
                    print('There is no more items, only From:{} to :{} rows left!'.format(index_start,index_end))
                    break
                else:
                    index_start = index_end
                    continue
            elif answer == 'no':
                break
            else:
                print("Invalid input, please try it again")
            continue
        except:
            print("Invalid input, please try it again")
            continue


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":

    main()
