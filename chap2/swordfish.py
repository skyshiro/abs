# Super secure, I know.

accessName = 'Tannis'
accessPassword = 'swordfish'

while True:
    print('Please type name:')
    name = input()

    if name != accessName:
        continue
    print('Hello ' + accessName + ', what is the password?')
    password = input()
    if password == accessPassword:
        break
print('Access granted, ' + accessName)

# Can use continue and breaks inside while and for loops
