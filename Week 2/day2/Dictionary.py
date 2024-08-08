#understand dictionary data type , there also methods that we can access.
#Dictionary methods :
#the process or activity of writing computer programs
#dictionary  = collection of data
#the correct brackers are the "{}" brakets (curly brakets)
#England" : "London"
#  "key"  :  "value"
# ":" separates the key from the value


capital_cities = {
    "England": "London",
    "France" : "Paris",
    "Spain" : "Madrid"
}
# print(capital_cities)

#key must be a data type that can`t be changed i.e. string , int, boolean
# value can be any data type
# dictionary let us look things up via  a key
 

print(capital_cities)
print(capital_cities["France"])

capital_cities["England"] = "Manchester"
print(capital_cities) # example of value being changed on a key




#dictionaries are very common from data basis
#dictionaries can contain duplicate keys
#keys must be unique
#keys cannot be changed , only values can be changed
#dictionaries have their own sets of methods
# - .keys (will return the list of the keys within the dictionary)
# - .values (will return a list of value within the dictionary)
# - .items (will return a list of tuples)
# - .get ( allows us to find out the value of the key , if the key does not exist it will return None )
#dictionaries can change , we have access to methods to helps us update the dictionary
# -.setdefault method takes two arguments we need to us a "," between key and value , is for adding new keys and values to our dictionary
# -.update  it will merge two dictionaries into one 
# -.pop will remove a key value pair from the dictionary
#-popitem will remove the last item from the dictionary



