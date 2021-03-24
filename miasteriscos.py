from time import sleep

def Asteriscos():
  for i in range(500):
      if i==24:
       break  
      print(i*"*",i*"*",i*"*")
      sleep(.500)

Asteriscos()
