from dataclasses import dataclass
import numpy as np

from salary_model import (
    WORK_AREA_FACTORS,
    experience_factor,
    MALE_SALARY_MEAN,
    MALE_SALARY_STD,
    FEMALE_SALARY_MEAN,
    FEMALE_SALARY_STD,
    DEGREE_BONUS,
    NON_WHITE_FACTOR,
    SALARY_NOISE_STD,
    MINIMUM_SALARY
)

@dataclass
class Person:
    id: int
    name: str
    sex: str
    age: int
    white: bool
    degree: bool
    work_area: str
    years_of_experience: int
    salary: float = None

    def calculate_salary(self):

        if self.sex == "M":
            salary = np.random.normal(
                MALE_SALARY_MEAN,
                MALE_SALARY_STD
            )
        else:
            salary = np.random.normal(
                FEMALE_SALARY_MEAN,
                FEMALE_SALARY_STD
            )

        salary *= experience_factor(
            self.years_of_experience
        )

        if not self.white:
            salary *= NON_WHITE_FACTOR

        salary *= WORK_AREA_FACTORS[self.work_area]

        if self.degree:
            salary += DEGREE_BONUS

        salary += np.random.normal(
            0,
            SALARY_NOISE_STD
        )

        return round(max(salary, MINIMUM_SALARY), 2)

    def __post_init__(self):
        self.salary = self.calculate_salary()