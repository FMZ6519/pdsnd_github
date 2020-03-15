import time
import pandas as pd
import numpy as np
#This is an update for Project 3
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("Please enter a city: Chicago, Washington or New York City: ").lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Please only enter a city like discribed. Check your spelling.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter a specific month: January, February, March, April, May, June or all: ").lower()
        if month not in MONTH_DATA:
            print("Please only enter a month like discribed. Check your spelling. This is for Project 3.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter a specific day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all: ").lower()
        if day not in DAY_DATA:
            print("Please only enter a day like discribed. Check your spelling. This is for Project 3.")
            continue
        else:
            break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print("Most common Month: ", common_month," ", "Most common day of the week: ", common_day, " ", "Most common Start Hour: ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("Most commonly used start station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("Most commonly used end station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = df.groupby(['Start Station', 'End Station']).count()
    print("Most frequent combination is ", common_start_station, " and", common_end_station, ".")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("Total travel time: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("There are ", user_types, "type of user.")

    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print("There are ", counts_of_gender, "gender fields.")
    except KeyError:
        print("Sorry, no data available.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = df['Birth Year'].min()
        print("Earliest year of birth: ", earliest_yob)
    except KeyError:
        print("Sorry, no data available.")

    try:
        most_recent_yob = df['Birth Year'].max()
        print("Most recent year of birth: ", most_recent_yob)
    except KeyError:
        print("Sorry, no data available.")

    try:
        most_common_yob = df['Birth Year'].value_counts().idxmax()
        print("Most common year of birth: ", most_common_yob)
    except KeyError:
        print("Sorry, no data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Display raw data
    start_count = 0
    stop_count = 5

    show_data = input("If you want to see the raw data please enter yes: ").lower()

    if show_data == 'yes':
        while stop_count <= df.shape[0] - 1:

            print(df.iloc[start_count:stop_count,:])
            start_count += 5
            stop_count += 5

            close_data = input("Please type yes for more data. Otherwise enter no: ").lower()
            if close_data == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
