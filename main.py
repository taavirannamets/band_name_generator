# 1. Create a greeting for the program
print('Hi there! Let\'s get started with finding your band an awesome name. For that, please answer the questions below.')

# 2. Ask the user for the city that they grew up in

city = input('In what city did you grow up? \n')

# 3. Ask the user for their favourite pet

pet = input('What\'s your favourite pet? \n')


# 4. Combine the name of their city and pet name, then show them their band name

band_name = city + " " + pet
print('Whoah! Your new band name is ' + band_name)
