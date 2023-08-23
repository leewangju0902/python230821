# demoStr.py
#print(dir(str))

strA  = "python is very powerful"
strB  = "파이썬은 강력해"


print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("P")) #소대문자 구분함.
print(strA.count("p",7))
      
result = strA.upper()
print(result)
print(strA.startswith("py"))
print(strA.endswith("ul"))

print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())
data = "<<< spam and ham >>>"

result = data.strip("<> ") # ""안에 입력한 모든 문자를 제거
print (data)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)

lst= result2.split()
print(lst)
print(", ".join(lst))