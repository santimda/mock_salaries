from person import Person
import random
from pathlib import Path
import pandas as pd

PERSON_COUNTER = 0

MEN_NAMES = [
    "Mark",
    "John",
    "Steve",
    "Carlos",
    "Oscar",
    "Tim",
    "Alex"
]

WOMEN_NAMES = [
    "Clara",
    "Maria",
    "Paula",
    "Elisabeth",
    "Jessica",
    "Alex"
]

WHITE_FRACTION = 0.6    # Assume a majority of white people
DEGREE_FRACTION = 0.4   # Assume that degrees are less common

def generate_person():
    global PERSON_COUNTER

    person_id = PERSON_COUNTER
    PERSON_COUNTER += 1

    sex = random.choice(["M", "F"])

    if sex == "M":
        name = random.choice(MEN_NAMES)
    else:
        name = random.choice(WOMEN_NAMES)

    age = random.randint(18, 65)

    years_of_experience = random.randint(0, age-18)

    white = random.random() < WHITE_FRACTION   
    degree = random.random() < DEGREE_FRACTION  

    # Assume that without a degree it is not possible to work in 
    # some areas, and that people with a degree avoid others
    if degree:
        work_area = random.choice(
            ["Health", "Education", "IT"]
        )
    else: 
        work_area = random.choice(
            ["IT", "Cleaning", "Transport"]
        )

    return Person(
        id=person_id,
        name=name,
        sex=sex,
        age=age,
        white=white,
        degree=degree,
        work_area=work_area,
        years_of_experience=years_of_experience
    )


if __name__ == "__main__":
    ROOT = Path(__file__).resolve().parent.parent
    DATA_DIR = ROOT / "data"

    DATA_DIR.mkdir(exist_ok=True)

    N = 25000

    people = [
        generate_person()
        for _ in range(N)
    ]

    df = pd.DataFrame(
        [vars(person) for person in people]
    )
    print(df.head())


    print(f"Saved {N} rows.")
    df.to_csv(
        DATA_DIR / "simulated_salaries.csv",
        index=False
    )
