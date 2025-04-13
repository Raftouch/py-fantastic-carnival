user_roles = ('admin', 'editor', 'viewer')

not_tuple = ('admin')
# print(type(not_tuple)) # str

my_tuple = ('admin',)
# print(type(my_tuple))

role_1, role_2, _ = user_roles
# print(role_1)