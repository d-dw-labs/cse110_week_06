'''courses_file = open('courses.txt')
with open('courses.txt') as courses_file:

    for line in courses_file:
        print(line)

name = ' \t Dylan De Wit \n'
name = name.strip()
print(f'***{name}***')
#print(f'***{name_stripped}***')


colours = 'red, blue, green orange'
colour_list = colours.split(',')
for i in range(len(colour_list)):
    colour_list[i] = colour_list[i].strip()
print(f'{colour_list}')'''

