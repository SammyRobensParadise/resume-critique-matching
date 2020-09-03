# Load the Pandas libraries with alias 'pd'
import pandas as pd

# importance 1 is highest
wants_website_critique = 1
interest_match = 2
same_location = 3
# unique for Covid-19
physical_distancing = 4

# read from file
data = pd.read_csv('/Users/sammyrobens-paradise/projects/resume-critique-matching/responses.csv')

# get students
incoming_students = data.loc[data['Year (Fall 2020)'] == '1A']
upper_year_students = data.loc[data['Year (Fall 2020)'] != '1A']

# get incoming design students
incoming_design_students = incoming_students.loc[
    incoming_students['Resume types you would like to have critiqued or critique'].str.contains('Design')
]

# get incoming product students
incoming_product_students = incoming_students.loc[
    incoming_students['Resume types you would like to have critiqued or critique'].str.contains('Product')]

# get incoming software students
incoming_software_students = incoming_students.loc[
    incoming_students['Resume types you would like to have critiqued or critique'].str.contains('Software')]

# get incoming hardware students
incoming_hardware_students = incoming_students.loc[
    incoming_students['Resume types you would like to have critiqued or critique'].str.contains('Mechanical')]

# get incoming research students
incoming_research_students = incoming_students.loc[
    incoming_students['Resume types you would like to have critiqued or critique'].str.contains('Research')]

# get general advice students
incoming_general_students = incoming_students.loc[
    incoming_students['Resume types you would like to have critiqued or critique'].str.contains('General')]

# get upper year design students
upper_year_design_students = upper_year_students.loc[
    upper_year_students['Resume types you would like to have critiqued or critique'].str.contains('Design')]

# get upper year product students
upper_year_product_students = upper_year_students.loc[
    upper_year_students['Resume types you would like to have critiqued or critique'].str.contains('Product')]

# get upper year software students
upper_year_software_students = upper_year_students.loc[
    upper_year_students['Resume types you would like to have critiqued or critique'].str.contains('Software')]

# get upper year hardware students
upper_year_hardware_students = upper_year_students.loc[
    upper_year_students['Resume types you would like to have critiqued or critique'].str.contains('Mechanical')]

# get upper year research students
upper_year_research_students = upper_year_students.loc[
    upper_year_students['Resume types you would like to have critiqued or critique'].str.contains('Research')]

# get upper year general students
upper_year_general_students = upper_year_students.loc[
    upper_year_students['Resume types you would like to have critiqued or critique'].str.contains('General')]

# IN PROGRESS
