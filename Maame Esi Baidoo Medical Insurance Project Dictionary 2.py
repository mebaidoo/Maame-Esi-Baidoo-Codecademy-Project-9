# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def damages_update(damages_list, updated_damages):
  for item in damages_list:
    if item == "Damages not recorded":
      updated_damages.append(item)
    elif item[-1] == "M":
      a = item.strip("M")
      b = float(a)
      updated_damages.append(b * conversion["M"])
    else:
      c = item.strip("B")
      d = float(c)
      updated_damages.append(d * conversion["B"])
  return updated_damages
      
# test function by updating damages
damages_updated = []
print("This is the list of the updated damages: " + str(damages_update(damages, damages_updated)))

# 2 
# Create a Table
def create_dictionary(Name, Month, Year, Max_Sustained_Wind, Areas_Affected, Damage, Death):
  b = {}
  i = 0
  for item in Name:
    a = {Name[i]: {"Name": Name[i], "Month": Month[i], "Year": Year[i], "Max Sustained Wind": Max_Sustained_Wind[i], "Areas Affected": Areas_Affected[i], "Damage": Damage[i], "Deaths": Death[i]}}
    b.update(a)
    i += 1
  return b
  
# Create and view the hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths)
print("\nThis is a dictionary containing the names of the hurricanes as keys and their related information: " + str(hurricanes))
# 3
# Organizing by Year
def convert_dictionary(a_dictionary):
  c = {}
  for item in a_dictionary:
    current_year = a_dictionary[item]["Year"]
    current_cane = a_dictionary[item]
    if current_year not in c.keys():
      c[current_year] = []
    if current_year in c.keys():
      c[current_year].append(current_cane)
  return c

# create a new dictionary of hurricanes with year and key
new_hurricanes = convert_dictionary(hurricanes)
print("\nThis is the new hurricanes dictionary: " + str(new_hurricanes))

# 4
# Counting Damaged Areas
def counting_damages(a_dictionary):
  b = {}
  for item in a_dictionary:
    a = a_dictionary[item]["Areas Affected"]
    c = 0
    for item in a:
      if item in b:
        c += 1
        b[item] = c
      else:
        c += 1
        b[item] = c
    c += 1
  return b
    
# create dictionary of areas to store the number of hurricanes involved in
affected_area_count = counting_damages(hurricanes)
print("\nThis dictionary shows how many times an area was affected by the hurricane: " + str(affected_area_count))

# 5 
# Calculating Maximum Hurricane Count
def max_hurricanes(areas_affected_count):
  max_area = "Central America"
  max_area_count = 0
  for item in areas_affected_count:
    if areas_affected_count[item] > max_area_count:
      max_area_count = areas_affected_count[item]
      max_area = item
  print("\n" + str(max_area) + " was the area affected most by hurricanes and " + str(max_area_count) + " was how often it was hit.")

# find most frequently affected area and the number of hurricanes involved in
area_max_hurricanes = max_hurricanes(affected_area_count)

# 6
# Calculating the Deadliest Hurricane
def find_deadliest_hurricane(Hurricane_Names, Deaths):
  a = {key: value for key, value in zip(Hurricane_Names, Deaths)}
  max_mortality_cane = "Central America"
  max_mortality = 0
  for item in a:
    if a[item] > max_mortality:
      max_mortality = a[item]
      max_mortality_cane = item
  print("\nThe hurricane that caused the most deaths is " + str(max_mortality_cane) + " and " + str(max_mortality) + " was the number of deaths it caused.")
# find highest mortality hurricane and the number of deaths
deadliest_hurricane = find_deadliest_hurricane(names, deaths)
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# Creating function
def rate_mortality(a_dictionary):
  a = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
  for item in a_dictionary:
    if a_dictionary[item]["Deaths"] == 0:
      a[0].append(a_dictionary[item])
    elif a_dictionary[item]["Deaths"] > 0 and a_dictionary[item]["Deaths"] <= 100:
      a[1].append(a_dictionary[item])
    elif a_dictionary[item]["Deaths"] > 100 and a_dictionary[item]["Deaths"] <= 500:
      a[2].append(a_dictionary[item])
    elif a_dictionary[item]["Deaths"] > 500 and a_dictionary[item]["Deaths"] <= 1000:
      a[3].append(a_dictionary[item])
    elif a_dictionary[item]["Deaths"] > 1000 and a_dictionary[item]["Deaths"] <= 10000:
      a[4].append(a_dictionary[item])
    else:
      a[5].append(a_dictionary[item])
  print("\nThis is a new dictionary containing ratings for mortality as keys based on the dictionary, {0: 0 deaths, 1: 100 deaths, 2: 500 deaths, 3: 1000 deaths, 4: 10000 deaths} and lists of hurricanes within that rating as values: " + str(a))
# categorize hurricanes in new dictionary with mortality severity as key
mortality_ratings = rate_mortality(hurricanes)

# 8 Calculating Hurricane Maximum Damage
def find_costly_hurricane(a_dictionary):
  greatest_cost = 0
  greatest_cost_cane = "Cuba I"
  for item in a_dictionary:
    if a_dictionary[item]["Damage"] == "Damages not recorded":
      continue
    elif a_dictionary[item]["Damage"] > greatest_cost:
      greatest_cost = a_dictionary[item]["Damage"]
      greatest_cost_cane = a_dictionary[item]["Name"]
    else:
      continue
  print("\n" + str(greatest_cost_cane) + " caused the greatest damage with a cost of " + str(greatest_cost))
# find highest damage inducing hurricane and its total cost
costly_hurricane = find_costly_hurricane(hurricanes)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
# Creating rating function
def rate_damage(a_dictionary):
  a = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for item in a_dictionary:
    if a_dictionary[item]["Damage"] == "Damages not recorded":
      continue
    elif a_dictionary[item]["Damage"] == damage_scale[0]:
      a[0].append(a_dictionary[item])
    elif a_dictionary[item]["Damage"] > damage_scale[0] and a_dictionary[item]["Damage"] <= damage_scale[1]:
      a[1].append(a_dictionary[item])
    elif a_dictionary[item]["Damage"] > damage_scale[1] and a_dictionary[item]["Damage"] <= damage_scale[2]:
      a[2].append(a_dictionary[item])
    elif a_dictionary[item]["Damage"] > damage_scale[2] and a_dictionary[item]["Damage"] <= damage_scale[3]:
      a[3].append(a_dictionary[item])
    elif a_dictionary[item]["Damage"] > damage_scale[3] and a_dictionary[item]["Damage"] <= damage_scale[4]:
      a[4].append(a_dictionary[item])
    else:
      a[5].append(a_dictionary[item])
  print("\nThis is a dictionary that contains hurricane ratings based on their damage: " + str(a))

# categorize hurricanes in new dictionary with damage severity as key
damage_rating = rate_damage(hurricanes)