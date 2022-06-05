"""
File: rating_stats.py
----------------------
This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data. 
"""

HIGH_RATING = 3.5

def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """
    male_count = 0
    male_high = 0
    female_high = 0
    female_count = 0
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            line = line.strip()
            parts = line.split(",")
            rating = float(parts[0])
            gender = parts[1]
            if gender == "M":
                male_count += 1
                if rating > HIGH_RATING:
                    male_high += 1
            else:
                female_count += 1
                if rating > HIGH_RATING:
                    female_high += 1
        f_percent = round(female_high / female_count * 100)
        m_percent = round(male_high / male_count * 100)
        print(str(f_percent) + "% of reviews for women in the dataset are high.")
        print(str(m_percent) + "% of reviews for men in the dataset are high.")


def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load? ")

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)


if __name__ == '__main__':
    main()
