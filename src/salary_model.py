# Baseline salaries
MALE_SALARY_MEAN = 40
MALE_SALARY_STD = 10

FEMALE_SALARY_MEAN = 35
FEMALE_SALARY_STD = 5

# Biases
NON_WHITE_FACTOR = 0.95

# Education
DEGREE_BONUS = 10

# Minimum salary
MINIMUM_SALARY = 15

# Salary differences between work areas
WORK_AREA_FACTORS = {
    "Cleaning": 0.8,
    "Education": 0.95,
    "Health": 1.0,
    "IT": 1.2,
    "Transport": 0.9,
}

# Extra random variation
SALARY_NOISE_STD = 2

def experience_factor(years):
    if years < 2:
        return 1.0
    elif years < 5:
        return 1.05
    elif years < 10:
        return 1.15
    elif years < 20:
        return 1.25
    else:
        return 1.30