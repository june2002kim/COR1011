str1='!abcABCdEF!!aBCDeFAbC!!'
find='abc'
del_='!'

str1_=str1.lower()
str1dex=str1_.find(find)
str1count=str1_.count(find)

str2=str1.replace(del_,'')

print('"%s 문자열에서 %s 문자열은 %d 인덱스, %d 번 존재"' %(str1, find, str1dex, str1count))
print('%s가 제거된 문자열 : %s' %(del_, str2))
