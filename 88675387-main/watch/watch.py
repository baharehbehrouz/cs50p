import re
# import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s.strip().lower()
    if len(re.findall("https?",s))==1 and re.search(r'^<.+(src=")(https?)://(www.)?(youtube).com/embed/(\w*)".*></.+>$',s):
        if match:=re.search(r'^<.+src="(https?://)(www.)?(youtube).com/embed/(\w*)".*></.+>$',s):

            return "https://youtu.be/"+match.group(4)
if __name__ == "__main__":
    main()