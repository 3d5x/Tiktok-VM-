import random
import requests

token = input('\nEnter your token: ')
ID = input('\nEnter your id: ')


def Yahoo():
      
      number = input("how many counts of email: ")
      start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Start (:").json()
      id_msg	= (start_msg['result']["message_id"])
      n = 1
      bad = 0
      Done = 0
      while 1:
        random_number = "qwertyuioplkjhgfdsamnbvcxz1234567890"
        user = str(''.join((random.choice(random_number) for i in range(int(number)))))
        email = user+"@yahoo.com"
        url = f"https://fars.gq/Emailtik/?email={email}"
        req = requests.get(url).text
        if 'Email Not linked' in req:
            bad +=1
            requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker .\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
        elif 'Error' in req:
            bad +=1
            requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker .\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
        else:
            rq = requests.get("https://vilr.pythonanywhere.com/yahoo/"+user).text
            if rq == "Yes✅":
                Done +=1
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker .️\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
                WK = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=- Hunted account tiktok .\n - Email : ❲ {email} ❳"
                requests.post(WK)

            else:
                bad +=1
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker . ️\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
        n+=1


def Gmail():
      
      number = input("how many counts of email: ")
      start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Start (:").json()
      id_msg	= (start_msg['result']["message_id"])
      n = 1
      bad = 0
      Done = 0
      while 1:
        random_number = "qwertyuioplkjhgfdsamnbvcxz1234567890"
        user = str(''.join((random.choice(random_number) for i in range(int(number)))))
        email = f"{user}@gmail.com"
        url = f"https://fars.gq/Emailtik/?email={email}"
        req = requests.get(url).text
        if 'Email Not linked' in req:
            bad +=1
            requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker .\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
        elif 'Error' in req:
            bad +=1
            requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker .\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
        else:
            rq = requests.get("https://apis.red/api/gmail/?mail="+email).text
            if rq == "Valid mail":
                Done +=1
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker .️\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
                WK = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=- Hunted account tiktok .\n - Email : ❲ {email} ❳"
                requests.post(WK)

            else:
                bad +=1
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker . ️\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
        n+=1


def Hotmail():
      
      number = input("how many counts of email: ")
      start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Start (:").json()
      id_msg	= (start_msg['result']["message_id"])
      n = 1
      bad = 0
      Done = 0
      while 1:
        random_number = "qwertyuioplkjhgfdsamnbvcxz1234567890"
        user = str(''.join((random.choice(random_number) for i in range(int(number)))))
        email = user+"@hotmail.com"
        url = f"https://fars.gq/Emailtik/?email={email}"
        req = requests.get(url).text
        if 'Email Not linked' in req:
            bad +=1
            requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker .\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
        elif 'Error' in req:
            bad +=1
            requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker .\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
        else:
            rq = requests.get("https://apis.red/api/hotmail/?mail="+email).text
            if rq == "Valid mail":
                Done +=1
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker .️\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
                WK = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=- Hunted account tiktok .\n - Email : ❲ {email} ❳"
                requests.post(WK)

            else:
                bad +=1
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=-  Running Now Checker . ️\n\n⌯ EmAi : {email} \n\n⌯ HiTs : {Done}\n\n⌯ BaD : {bad}")
        n+=1

if __name__ == "__main__":

    print("""
    
████████▀▀▀████
████████────▀██
████████──█▄──█
███▀▀▀██──█████
█▀──▄▄██──█████
█──█████──█████
█▄──▀▀▀──▄█████
███▄▄▄▄▄███████

    """)
    def log_it():
        
        choose=int(input(f"""
1) Yahoo
2) Gmail  
3) hotmail 
----------------------------------------------------------------------------

choose your number: """))

    
        if choose==1:
            Yahoo()
        elif choose==2:
            Gmail()
        elif choose==3:
            Hotmail()
        else:
            print("please choose one of them")
            log_it()
log_it()        