contacts={}  #empty dictionary

while True:
    print('\nContact Book App')
    print('1. Creator contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search contact')
    print('6. Count contact')
    print('7. Exit')

    choice = input('enter your choice =')

    if choice == '1': 
         name= input('enter your name=')
         if name in contacts:
                print(f'Contact with name {name} already exists!')
         else:
            age= input('enter age=')
            email=input('enter email=')
            mobile=input('enter mobile number=')
            contacts[name] = {'age': age, 'email': email, 'mobile': mobile}               
            print(f'Contact {name} added successfully!')
    elif choice =='2':
        name=input('enter contact name to view=')
        if name in contacts:
            contact= contacts[name]
            print(f"Name: {name}, Age: {contact['age']}, Mobile Number:{contact['mobile']}")
        else:
            print('contact not found')
    elif choice=='3':
        name=input('enter the contact name to update=')
        if name in contacts :
            age=input('enter new age=')
            email=input('enter new email=')
            mobile=input('enter new mobile number=')
            contacts[name] = {'age': age, 'email': email, 'mobile': mobile}
            print(f'Contact {name} updated successfully!') 
        else:
            print("contact not found")
    elif choice =='4':
        name=input('enter the contact name to delete=')
        if name in contacts:
            del contacts[name]
            print(f'Contact {name} deleted successfully!')
        else:
            print("contact not found")              
    elif choice =='5':
        name= input('enter the contact name to search =')
        found= False
        for name, contact in contacts.items():
            if name.lower() == name.lower():
                print(f'Found - Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile Number: {contact['mobile']}')
                found=True
        if not found:
            print('contact not found')
    elif choice =='6':
        count= len(contacts)
        print(f'Total contacts: {count}')
    elif choice =='7':
       print('exiting th program')
       break
    else:
       print('invalid choice, please try again')
input=int('press 1: fo continue or press 2: for exit')
        