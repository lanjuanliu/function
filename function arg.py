# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list))

# def say_hello(name):
#     print("Hello ", name)
#     print("How are you?")
# say_hello("Aatif")


# def add_numbers(number1, number2):
#     print("I will add two numbers.")
#     print(120 + 50)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name)

def say_hello_language(name, language):
    if language == "hindi":
        print("Namaste ", name)
        print("Aap kaise ho?")
    elif language == "punjabi":
        print("Sat sri akaal ", name)
        print("Tuhada ki haal hai?")
    else:
        print("Hello ", name)
        print("How are you?")
say_hello_language("Rishabh", "punjabi")
say_hello_language("Armaan", "english")
say_hello_language("Abhishek", "french")
say_hello_language("Kavay", "hindi")