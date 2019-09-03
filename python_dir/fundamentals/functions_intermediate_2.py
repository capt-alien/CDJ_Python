#!python3

# 1) Update Values in Dictionaries and Lists
# d) Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# a)
def change_1(x=x, students=students, sports_directory=sports_directory, z=z):
# a) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    x[1][0] = 15
    print(x)
# b) Change the last_name of the first student from 'Jordan' to 'Bryant'
    students[0]['last_name'] = 'Bryant'
    print(students)
    # c) In the sports_directory, change 'Messi' to 'Andres'
    sports_directory['soccer'][0]='Andres'
    print(sports_directory)


# 2) Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of
# dictionaries, the function loops through each dictionary in the list and prints
# each key and the associated value. For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students=students):
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
    for x in students:
        for key, value in x.items():
            print(key,"=" ,value)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel




def main():
    # changes_1()
    iterateDictionary()


if __name__ == '__main__':
    main()
