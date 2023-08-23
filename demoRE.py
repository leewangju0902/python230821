# demoRE.py
import re

result = re.search("[0-9]*th"," 35th")
print(result)
print(result.group())

#result = re.match("[0-9]*th"," 35th") #시작부터 찾기때문에 안됨
if False:
    result = re.match("[0-9]*th","35th")
    print(result)
    print(result.group())

print("---연도를 찾는 경우---")
result = re.search("\d{4}", "올해는 2023년 입니다.")
print(result.group())

print("---우편번호를 찾는 경우---")
result = re.search("\d{5}", "우리 동네는 52300 입니다.")
print(result.group())

telChecker  = re.compile("(\d{2,3})-(\d{3,4})-(\d{4})")

m = telChecker.match("02-3429-5000")
if m:
    print(m.group())

if bool(telChecker.match("02-가3429-5000")):
    print(telChecker.match("02-가3429-5000").group())

if bool(telChecker.match("020-3429-5000")):
    print(telChecker.match("020-3429-5000").group())

if bool(telChecker.match("5020-3429-5000")):
    print(telChecker.match("5020-3429-5000").group())

