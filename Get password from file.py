#using python 2.7 version
import pickle
import pyperclip

#asks master password from user
m_pass=raw_input('Enter master password :\t')

#you can change the master password as needed
if(m_pass=="rishika"):
    acc_name=raw_input('Enter account name :\t')
    with open('silence.abcd','r')as readfile:
        info=pickle.load(readfile)
    if acc_name in info.keys():
        pyperclip.copy(info[acc_name])
        print('password copied :)')

    else:
        print("Password not found")
else:
    print("Password doesn't match")
