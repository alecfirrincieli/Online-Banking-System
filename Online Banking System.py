"""an online banking system.  Users can sign up with the system, log in to the
 system, change their password, and delete their account.  They can also update their bank account balance and transfer
 money to another user’s bank account."""


def import_and_create_bank(filename):

    bank = {}

    f = open(filename, 'r')
    lines = f.readlines()
    
    
    for line in lines:
        lst = line.strip().split(':')
        
        if len(lst) <= 1:
            continue
        
        key = lst[0].strip()
        value = lst[1].strip()
        
        try:
            value = float(value)
            bank[key] = bank.get(key, 0) + value
            
        except:
            continue
            
    f.close()
            
        
    

    return bank

import_and_create_bank("bank.txt")








def signup(user_accounts, log_in, username, password):
    '''
    This function allows users to sign up.
    If both username and password meet the requirements:
    - Updates the username and the corresponding password in the user_accounts dictionary.
    - Updates the log_in dictionary, setting the value to False.
    - Returns True.

    If the username and password fail to meet any one of the following requirements, returns False.
    - The username already exists in the user_accounts.
    - The password must be at least 8 characters.
    - The password must contain at least one lowercase character.
    - The password must contain at least one uppercase character.
    - The password must contain at least one number.
    - The username & password cannot be the same.

    '''
    if (username in user_accounts): return False
    
    if (valid_password(username, password)):    
        
        user_accounts.update({username:password})
        
        log_in.update({username: False})
        
        return True
    return False                                                    

def valid_password(username, password):
    '''
    - The password must be at least 8 characters.
    - The password must contain at least one lowercase character.
    - The password must contain at least one uppercase character.
    - The password must contain at least one number.
    '''

    # password and username assigned to a variable
    p_word = password
    u_name = username


    '''
    - The password must contain at least one lowercase character.
    - The password must contain at least one uppercase character.
    - The password must contain at least one number. '''

    lower, upper, digit, = 0, 0, 0

    # The password must be at least 8 characters.
    if len(p_word) >= 8:

        for i in p_word:
             #validation for lowercase characters.
            if (i.islower()):
                lower += 1

            # validation for upper case characters
            if (i.isupper()):
                upper += 1

            #validation for numerics
            if (i.isdigit()):
                digit += 1

    # validating all three conditions
    return(lower >= 1 and upper >= 1 and digit >= 1 and len(p_word) >=8 and (username != password)) 
        
    
valid_password("Brandon", "Brandon1234")  
    
        


# In[6]:


def import_and_create_accounts(filename):
    '''
    This function is used to create an user accounts dictionary and another login dictionary.  The given argument is the
    filename to load.
    '''

    user_accounts = {}
    log_in = {}


    
    #opens the file in read mode.
    f = open(filename, 'r')

    #get all lines in the files as a list
    lines = f.readlines()

    #iterate over the lines and strip the lines and add to lst separated by ':'
    for line in lines:
        lst = line.strip().split('-')

        # to exclude the empty lines and lines with no user names or password.
        if len(lst) <= 1:
            continue

        username_key = lst[0].strip()
        password_value = lst[1].strip()

        signup(user_accounts, log_in, username_key, password_value)

    f.close()  


    
    

    return user_accounts,log_in



# In[10]:


def login(user_accounts, log_in, username, password):
    '''
    This function allows users to log in with their username and password.
    The user_accounts dictionary stores the username and associated password.
    The log_in dictionary stores the username and associated log-in status.

    If the username does not exist in user_accounts or the password is incorrect:
    - Returns False.
    Otherwise:
    - Updates the user's log-in status in the log_in dictionary, setting the value to True.
    - Returns True.
       '''

    if(username in user_accounts) and (password == user_accounts.get(username)):
        log_in.update({username: True})
        return True
    
    return False
    


def update(bank, log_in, username, amount):
    '''
    In this function, you will try to update the given user's bank account with the given amount.
    bank is a dictionary where the key is the username and the value is the user's account balance.
    log_in is a dictionary where the key is the username and the value is the user's log-in status.
    amount is the amount to update with, and can either be positive or negative.

    To update the user's account with the amount, the following requirements must be met:
    - The user exists in log_in and his/her status is True, meaning, the user is logged in.

    If the user doesn't exist in the bank, create the user.
    - The given amount can not result in a negative balance in the bank account.

    Return True if the user's account was updated.
    '''



    if (log_in.get(username, False)):
        balance = bank.get(username, 0)
        new_balance = balance + amount
        
        if (new_balance >= 0):
            bank.update({username: new_balance})
            return True
        
    return False



def transfer(bank, log_in, userA, userB, amount):
    '''
    In this function, you will try to make a transfer between two user accounts.
    bank is a dictionary where the key is the username and the value is the user's account balance.
    log_in is a dictionary where the key is the username and the value is the user's log-in status.
    amount is the amount to be transferred between user accounts (userA and userB).  amount is always positive.

    What you will do:
    - Deduct the given amount from userA and add it to userB, which makes a transfer.
    - You should consider some following cases:
      - userA must be in the bank and his/her log-in status in log_in must be True.
      - userB must be in log_in, regardless of log-in status.  userB can be absent in the bank.
      - No user can have a negative amount in their account. He/she must have a positive or zero balance.

    Return True if a transfer is made.
    '''

    if(userB not in log_in): return False
    if(amount <=0): False
    if update(bank, log_in, userA, -amount):
        balance = bank.get(userB,0) + amount
        bank.update({userB : balance})
        return True
    return False
    


def change_password(user_accounts, log_in, username, old_password, new_password):
    '''
    This function allows users to change their password.

    If all of the following requirements are met, changes the password and returns True. Otherwise, returns False.
    - The username exists in the user_accounts.
    - The user is logged in (the username is associated with the value True in the log_in dictionary)
    - The old_password is the user's current password.
    - The new_password should be different from the old one.
    - The new_password fulfills the requirement in signup.

    '''
    
    if(username not in user_accounts): return False
    
    if not(log_in.get(username)): return False
    
    if not (user_accounts.get(username) == old_password): return False
    
    if(old_password == new_password): return False
    
    if(valid_password(username, new_password)):
        user_accounts.update({username: new_password})
        
    else:
        return False
        
    return True


def delete_account(user_accounts, log_in, bank, username, password):
    '''
    Completely deletes the user from the online banking system.
    If the user exists in the user_accounts dictionary and the password is correct, and the user 
    is logged in (the username is associated with the value True in the log_in dictionary):
    - Deletes the user from the user_accounts dictionary, the log_in dictionary, and the bank dictionary.
    - Returns True.
    Otherwise:
    - Returns False.

  '''

    if (username not in user_accounts): return False
    if (log_in.get(username) and user_accounts.get(username) == password ):
        del user_accounts[username]
        del log_in[username]
        del bank[username]
        
       
        
        return True
    return False
    



def main():
    
  

    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password);
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break;
        else:
            print("The option is not valid. Please re-enter the option.\n")


if __name__ == '__main__':
    main()






