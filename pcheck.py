import os
import time
os.system("clear")
def main():
    print("""
 __        __   __        __   __   __  
|__)  /\  /__` /__` |  | /  \ |__) |  \ 
|    /~~\ .__/ .__/ |/\| \__/ |  \ |__/ 
 __        ___  __        ___  __       
/  ` |__| |__  /  ` |__/ |__  |__)      
\__, |  | |___ \__, |  \ |___ |  \      
                                            
    """)
    
    print("""\033[3m\033[1mCreated by Truthful hacker
Password Vulnerability Checker
    """)
    
    
    
    word = input("\033[91mEnter your password:\033[93m ")
    #file = input("\033[91mEnter wordlist path:\033[93m ")
    file = ("rockyou.txt")
    file = open(file).readlines()
    
    for i in file:
        
        
        if word in i:
            time.sleep(2)
            print("\033[91m\nYour password is in this wordlist:",word)
            print("\033[96mDon't use this password")
            exit()
    time.sleep(2)
    print("\033[92m\nYour password is not in this wordlist:",word)
    
if os.path.isfile("rockyou.txt"):
    main()
    
else:
	os.system("wget -q http://tapr00t.com/files/wordlists/rockyou.txt")
	main()

