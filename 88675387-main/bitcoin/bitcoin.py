import sys
import requests
import json
def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
if len(sys.argv)!=2:
    sys.exit("Missing command-line argument")

if len(sys.argv)==2:
    val=isDigit(sys.argv[1])
    if val:
        val=float(sys.argv[1])
        # print(val)
        try:
            # val=val.replace(',','')
            # v=len(val)-1
            # val = str(float(val))
            response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            rate=response.json()
            rate=rate["bpi"]["USD"]["rate"]
            rate=rate.replace(',','')
            rate=float(rate)
            # val=float(val)
            res=rate*val
            print(f"${res:,.4f}")

            # sys.exit(res)
        except requests.RequestException:
            pass

    else:
        sys.exit("Command-line argument is not a number")

