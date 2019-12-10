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
    user_city_input= input("Enter the city name (Chicago or New york or Washington)\n").strip()
    city= user_city_input.title()


    while (city != "Chicago" and city != "New York" and city != "Washington"  ):
        print("invalid input, try again")
        user_city_input= input ("Enter the city name (Chicago or New york or Washington)\n").strip()
        city= user_city_input.title()


    # TO DO: get user input for month (all, january, february, ... , june)
    user_month_input= input("Enter the month (all, january, february, ... , june). Type 'all' for no time filter\n").strip()
    month= user_month_input.title()


    while (month != "All" and month != "January" and month != "February" and month != "March" and month != "April" and month != "May" and month != "June"):
        print("invalid input, try again")
        user_month_input= input ("Enter the month (all, january, february, ... , june). Type 'all' for no month filter\n").strip()
        month= user_month_input.title()

     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    user_day_input= input("Enter the  day of week (all, monday, tuesday, ... sunday). Type 'all' for no day filter\n").strip()
    day= user_day_input.title()


    while (day != "All" and day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Saturday" and day != "Sunday"):
         print("invalid input, try again")
         user_day_input= input ("Enter the  day of week (all, monday, tuesday, ... sunday). Type 'all' for no day filter\n").strip()
         day= user_day_input.title()
    print("You chose the following: City:", city, "Month:",month,"Day:", day)




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
    if city == 'Chicago':
        df = pd.read_csv(CITY_DATA['chicago'])
    elif city == 'New York':
        df = pd.read_csv(CITY_DATA['new york city'])
    else:
        df = pd.read_csv(CITY_DATA['washington'])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()

    if month != 'All':
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month:\n{} \n'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most common day:\n{} \n'.format(popular_day))


    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour:\n{} \n'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_s_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:\n{} \n'.format(popular_s_station))


    # TO DO: display most commonly used end station
    popular_e_station = df['End Station'].mode()[0]
    print('Most commonly used end station:\n{} \n'.format(popular_e_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['combination']= df['Start Station'] + " - To - " + df['End Station']
    popular_trip = df['combination'].mode()[0]
    print('Most common frequent combination of start station and end station trip:\n{} \n'.format(popular_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_trip_duration= df['Trip Duration'].sum()
    print('Total travel time:\n{} \n'.format(Total_trip_duration))
    # TO DO: display mean travel time
    Mean_trip_duration= df['Trip Duration'].mean()
    print('Mean travel time:\n{} \n'.format(Mean_trip_duration))

    Total_count_of_Trips= df['Trip Duration'].count()
    print('Number of trips:\n{} \n'.format(Total_count_of_Trips))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of user types:\nSubscriber')
    print(df['User Type'].value_counts()['Subscriber'])
    print('\nCustomer:')
    print(df['User Type'].value_counts()['Customer'])

    print('\nCounts of gender:\n')
    print('Male:')
    print(df['Gender'].value_counts()['Male'])
    print('\nFemale:')
    print(df['Gender'].value_counts()['Female'])

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Oldest year of birth : ' , df['Birth Year'].min())
    print('\nNewest year of birth : ' ,df['Birth Year'].max())
    print('\nMost common year of birth : ', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        """Displays 5 rows of raw data"""
        user_raw_data= input("Do you want to see raw data? Enter : yes or no.\n").lower()
        start = 0
        end = 5
        while(user_raw_data == "yes"):
            print(df.iloc[start:end])
            start += 5
            end += 5
            user_raw_data= input("Do you still want to see more raw data? Enter : yes or no.\n").lower()


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
