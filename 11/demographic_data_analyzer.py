import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race?
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100,
        1
    )

    # Advanced education: Bachelors, Masters, Doctorate
    advanced_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    # People with advanced education who earn >50K
    higher_education_rich = round(
        (df[advanced_education]['salary'] == '>50K').mean() * 100,
        1
    )

    # People without advanced education who earn >50K
    lower_education_rich = round(
        (df[~advanced_education]['salary'] == '>50K').mean() * 100,
        1
    )

    # Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # Percentage of people working minimum hours who earn >50K
    min_hours = df[df['hours-per-week'] == min_work_hours]

    num_min_workers = len(min_hours)

    rich_percentage = round(
        (min_hours['salary'] == '>50K').mean() * 100,
        1
    )

    # Country with highest percentage earning >50K
    country_salary = df.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').mean() * 100
    )

    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(
        country_salary.max(),
        1
    )

    # Most popular occupation for people earning >50K in India
    india_rich = df[
        (df['native-country'] == 'India') &
        (df['salary'] == '>50K')
    ]

    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(
            "Percentage with Bachelors degrees:",
            percentage_bachelors
        )
        print(
            "Percentage with higher education that earn >50K:",
            higher_education_rich
        )
        print(
            "Percentage without higher education that earn >50K:",
            lower_education_rich
        )
        print("Min work time:", min_work_hours, "hours/week")
        print(
            "Percentage of rich among those who work fewest hours:",
            rich_percentage
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )
        print(
            "Highest percentage of rich people:",
            highest_earning_country_percentage
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
