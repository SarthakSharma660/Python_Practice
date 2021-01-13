travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# a sample dictionary
add={
  "country": "ab",
  "visits": 0  ,
  "cities":  [] ,
}
# function to add new places
def add_new_country(country,visits,cities):
  for key in add:
    if key=="country":
      add[key]=country
    elif key=="visits":
      add[key]=visits
    else:
      add[key]=cities
  travel_log.append(add)
# function call
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# printing the final dictionary
print(travel_log)
# printing list items 
for index in range (0,len(travel_log)):
    print(travel_log[index])