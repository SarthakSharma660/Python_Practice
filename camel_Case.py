
# function to change a string into camel case
def PascalCase(string):
    string=string.title()
    return string

# function call
print(PascalCase("THIS lInE WiLl be PRinTEd iN Pascal Case"))

# for string provided by user
user_input=input("Enter a string that needs to be con verted to Pascal Case : ")
print(PascalCase(user_input))


# for camel case
def camelCase(st):
    s = st.title()
    d = "".join(s.split())
    d = d.replace(d[0],d[0].lower())
    # d=d.join()
    return d

# example
print(camelCase("Hi i am py bot"))

# user input
user_input=input("Enter a string that needs to be con verted to camel Case : ")
print(camelCase(user_input))