import random

def estimate_polish_population_in_oberammergau():
  total_polish_population_in_bavaria = 120000
  population_of_oberammergau = 5000
  percentage_of_polish_people_in_oberammergau = random.randint(1, 10) / 100
  estimated_number_of_polish_people_in_oberammergau = population_of_oberammergau * percentage_of_polish_people_in_oberammergau
  return estimated_number_of_polish_people_in_oberammergau

print(estimate_polish_population_in_oberammergau())
