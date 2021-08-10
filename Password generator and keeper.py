#using python 2.7 version 
import os
import string
import random
import pickle

#declaring different character sets needed to make password
if __name__=="__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    
#inputs password length    
length=int(input('Enter password length :\t'))

#making list that includes all characters
combine_list=[]
combine_list.extend(list(s1))
combine_list.extend(list(s2))
combine_list.extend(list(s3))
combine_list.extend(list(s4))

#condition if length is less than 4
if(length<4):
    pass_list=random.sample(combine_list,length)

    #shuffle 
    random.shuffle(pass_list)
    password=''.join(pass_list)
          
    # print out password
    print('Your password is :')
    print(password)
    print('It is a weak password. Please generate a long password :)')
else:
    # randomly select at least one character from each character set above 
    rand_lower = random.choice(s1)
    rand_upper = random.choice(s2)
    rand_digit = random.choice(s3)
    rand_symbol = random.choice(s4)

    #now the password has 4 characters
    temp_pass = list(rand_digit) + list(rand_upper) + list(rand_lower) + list(rand_symbol)

    #it randomely selects the other characters
    temp_pass2=random.sample(combine_list,length-4)
    pass_list=temp_pass + temp_pass2

    #shuffle 
    random.shuffle(pass_list)
    password=''.join(pass_list)
          
    # print out password
    print('Your password is :')
    print(password) 

#asks the user whether they want to save it or not
answer=raw_input('\nWould you like to keep this password: yes or no - \n')

if("yes" in answer):
    #asks account name from user
    acc_name=raw_input('Enter account name:\t')
    #checks wether file exists or not
    if os.path.exists('silence.abcd'):
        with open('silence.abcd','r')as readfile:
            info=pickle.load(readfile)
            info[acc_name]=password
    else:
        #new dictionary made if file don't exist
        info={}
        info[acc_name]=password
    #dictionary saved in file
    with open('silence.abcd','w') as filewrite:
        pickle.dump(info,filewrite,protocol=2)
    print('Password saved')

else:
    print('ok,password not saved')

   




