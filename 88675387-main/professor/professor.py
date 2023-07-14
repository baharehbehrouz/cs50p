
import random
import sys


def main():
    Lvl = get_level()
    mistak=0
    err=0
    i=0
    while i<10:
        i+=1
        FNumber = generate_integer(Lvl)
        SNumber = generate_integer(Lvl)
        sum = FNumber + SNumber
        expression=str(FNumber) +" + "+str(SNumber)+" = "
            # if i<10:
        # AnsRes=input(expression)
        # AnsRes=delSpace(AnsRes)
        # if AnsRes.isdigit():
        AnsRes=get_Sum(expression)
        if AnsRes!=sum:
            while True:
              if err<2:
                 print("EEE")
                 err+=1
    #                     # if i<10:
                 AnsRes = get_Sum(expression)
    #
    #                     AnsRes = delSpace(AnsRes)
                 if AnsRes==sum:
    #                         # if i<10:
    #                         #     i+=1
                     err=0
                     break
              elif err==2:
                   print(expression,sum)
    #                     # if i<10:
    #                     #     i+=1
                   mistak+=1
                   err=0
                   break
    #         else:
    #             if i>=10:
    #                 break
    print("score:",10-mistak)
def get_Sum(expression):

 while True:
  try:
        ans=input(expression)
        if ans.isdigit():
            # ans=ans.split("")
            ans=int(ans)
        return ans
  except :
      print("ValueError")
      
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

