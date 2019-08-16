import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWhich city you would like to explore, Chicago, New York, or Washington?\n').lower()
    while(True):

        if(city == 'chicago' or city == 'new york' or city == 'washington' or city == 'all'):
            break
        else:
            city = input('Enter Correct city: ').lower()

    # Get user input for month (all, january, february, ... , june)
    month = input('\nFor which month? January, February, March, April, May, or June?\n').lower()

    while(True):
        if(month == 'all' or month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june'):
            break
        else:
            month = input('Enter a valid month\n').lower()
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input('Which day ? monday, tuesday, wednesday, thursday, friday, saturday , sunday or all to display data of all days?\n').lower()

    while(True):

        if(day == 'all' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday'):
            break
        else:
            day = input('Enter Correct day: ').lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    """To load the csv file of the selected city"""

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    """to_datetime used to convert date into date format"""
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        """to find the index of selected month from list"""
        month = months.index(month) + 1

        df = df[df['Start Time'].dt.month == month]
    """New DataFrame that contains old DataFrame with month = selected month"""

    #Filter data by day of the week
    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]
     #print 5 rows.
    print(df.head())
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    if(month == 'all'):
        most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(most_common_month))

    # Display the most common day of week
    if(day == 'all'):
        most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most common day is ' + str(most_common_day))

    # Display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('\nMost common start station is {}\n'.format(most_common_start_station))

    # Display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\nMost common end station is {}\n'.format(most_common_end_station))

    # Display most frequent combination of start station and end station trip
    combination_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\nMost popular trip is from {}\n'.format(most_frequent_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is %s in seconds" %(total_travel_time))

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is %s in seconds" %(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types")
    if 'User Type' in df.columns:
        print(df['User Type'].value_counts())
    else:
        print("For %s User Type data not available" %(city))
    # Display counts of gender
    print("Counts of Gender")
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("For %s Gender data not available" %(city))

    # Display earliest, most recent, and most common year of birth
    print("Year of Birth")
    if 'Birth Year' in df.columns:
        max_birth_year = df['Birth Year'].max()
        print("Most Recent Birth Year is %s" %(max_birth_year))

        min_birth_year = df['Birth Year'].min()
        print("Most Earliest Birth Year is %s" %(min_birth_year))

        frequent_birth_year = df['Birth Year'].mode()[0]
        print("Most Frequent Birth Year is %s" %(frequent_birth_year))
    else:
        print("For %s Birth Year data not available" %(city))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    user_input = input('Do you want to see raw data? Enter yes or no.\n')
    line_number = 0

    while 1 == 1 :
        if user_input.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = input('\nDo you want to see 5 more lines of raw data? Enter yes or no.\n')
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
