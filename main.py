# Load the Pandas libraries with alias 'pd'
import pandas as pd

# importance 1 is highest
wants_website_critique = 1
interest_match = 2
same_location = 3
# unique for Covid-19
physical_distancing = 4


# @returns
def portfolio_critique_frame(df):
    return df.loc[df[
                      'Would you also like a website/portfolio critique or feel comfortable critiquing website/portfolios?'] == 'Yes']


class Student:
    def __init__(self, name, email, interests, wants_portfolio_review):
        self._name = name
        self._email = email
        self._interests = interests
        self._wants_portfolio_review = wants_portfolio_review

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_info(self):
        return {
            "name": self._name,
            "email": self._email,
            "interests": self._interests,
            "wants_portfolio_review": self._wants_portfolio_review
        }


# setup Pair  Class
class Pair:
    def __init__(self, upper_year, incoming_student):
        self._u_y = upper_year
        self._i_s = incoming_student

    def get_pair(self):
        return {
            "incoming_student": self._i_s,
            "upper_year": self._u_y
        }


UpperYearDesignList = []
IncomingDesignList = []

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

# add design prefixes
incoming_design_students_with_portfolio = portfolio_critique_frame(incoming_design_students)
upper_year_design_students_with_portfolio = portfolio_critique_frame(upper_year_design_students)

# add Incoming Design
incoming_design_students_with_portfolio = incoming_design_students_with_portfolio.add_prefix("Incoming ")
design_students = pd.concat([upper_year_design_students_with_portfolio, incoming_design_students_with_portfolio])

# add product prefixes
incoming_product_students_with_portfolio = portfolio_critique_frame(incoming_product_students)
upper_year_product_students_with_portfolio = portfolio_critique_frame(upper_year_product_students)

# add Incoming Product
incoming_product_students_with_portfolio = incoming_design_students_with_portfolio.add_prefix("Incoming")
product_students = pd.concat([upper_year_product_students_with_portfolio, incoming_product_students_with_portfolio])

#
incoming_software_students_with_portfolio = portfolio_critique_frame(incoming_software_students)
upper_year_software_students_with_portfolio = portfolio_critique_frame(upper_year_software_students)




with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(design_students)
    print(product_students)
