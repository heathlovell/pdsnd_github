import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWhat city would you like to explore: chicago, new york city, or washington?\n')
        if city.lower() == 'chicago':
            city = 'chicago'
            break
        elif city.lower() == 'new york city':
            city = 'new york city'
            break
        elif city.lower() == 'washington':
            city = 'washington'
            break
    

    # get user input for month (all, january, february, ... , june)
    print()
    while True:
        print('What month would you like to explore:', end = '')
        month = input('\nall, january, february, march, april, may, or june?\n')
        if month.lower() == 'all':
            month = 'all'
            break
        elif month.lower() == 'january':
            month = 'january'
            break
        elif month.lower() == 'february':
            month = 'february'
            break
        elif month.lower() == 'march':
            month = 'march'
            break
        elif month.lower() == 'april':
            month = 'april'
            break
        elif month.lower() == 'may':
            month = 'may'
            break
        elif month.lower() == 'june':
            month = 'june'
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    print()
    while True:
        print('What day would you like to explore:', end = '')
        day = input('\nall, sunday, monday, tuesday, wednesday, thursday, friday, or saturday?\n')
        if day.lower() == 'all':
            day = 'all'
            break
        elif day.lower() == 'sunday':
            day = 'sunday'
            break
        elif day.lower() == 'monday':
            day = 'monday'
            break
        elif day.lower() == 'tuesday':
            day = 'tuesday'
            break
        elif day.lower() == 'wednesday':
            day = 'wednesday'
            break
        elif day.lower() == 'thursday':
            day = 'thursday'
            break
        elif day.lower() == 'friday':
            day = 'friday'
            break
        elif day.lower() == 'saturday':
            day = 'saturday'
            break


    print('-'*40)
    #print(city, month, day)
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

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day of the Week:', popular_day)

    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)

    # display most commonly used end station
    popular_start_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_start_station)

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' - ' + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('Most Frequent Trip:', popular_trip)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df['Trip Duration'].sum()
    print("Total Travel Time:", travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time:", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    #count_user_types = df['User Type'].value_counts()
    #print("Count of User Types:", count_user_types)
    print()
    
   
    print(str(df['User Type'].unique()[0]) + '\t'+ str(df['User Type'].value_counts()[0]))
    print(str(df['User Type'].unique()[1]) + '\t'+ str(df['User Type'].value_counts()[1]))
    
    print()

    if city != 'washington':
        # Display counts of gender
        #count_gender = df['Gender'].value_counts()
        #print("Count of Gender:", count_gender)
        print(str(df['Gender'].unique()[0]) + '\t'+ str(df['Gender'].value_counts()[0]))
        print(str(df['Gender'].unique()[1]) + '\t'+ str(df['Gender'].value_counts()[1]))
    

        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        latest_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()

        print()
        print("Earliest Birth Year:", int(earliest_birth_year))
        print("Most Recent Birth Year:", int(latest_birth_year))
        print("Most Common Birth Year:", int(common_birth_year))

    else:
        print('Gender and Birth Year Information is not available for Washington.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df.columns)
        #print(df.describe())
        #print(df.info())
    
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        display_data = input('\nWould you like to see the raw data? Enter yes or no.\n')
        counter = 0
        while True:
            if display_data.lower() != 'no':
                print(df[counter:counter + 5].to_string())
                counter += 5
                display_data = input('\nWould you like to see another 5 rows of data? Enter yes or no.\n')
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

    print("Thank you for using bikeshare!")

if __name__ == "__main__":
	main()
