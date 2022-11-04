# Exercise 5:
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as Reykjavik is in Iceland.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

print("\nExercise 5:\n")

# here, a function named "countryandcities" is defined...
# i added two parameters, "country" and "city"
# in the "country" parameter, i added a default country, but left "city" empty
def countryandcities(country = "Australia", city = ""):
    # inside the function, there is a print command that prints details for the given countries and cities
    print("The city " + city.title() + ", is in " + country.title() + ".\n")

# outside the function, i called the user-defined function, giving a value for "city"
countryandcities(city = "Melbourne")
# i called it again, but this time, i gave a different value for "city"
countryandcities(city = "Sydney")
# once again, i called the function, but this time, i added input so the user can put any country and city
countryandcities(input("\nEnter a country: "), input("Enter a city: "))