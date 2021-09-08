# # jabber = open("/home/oem/Projects/python_programming_masterclass/Python IO/sample.txt", 'r')
# jabber = open("sample.txt", 'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()

# # with manages errors and if there is one it closes the file beforw error is raised
# # with also closes file at the end of with statement so we don't have to do this explicitly
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# # process text line by line
# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)

for line in lines:
    print(line, end='')