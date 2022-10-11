String1=input("Enter string1:")
String2=input("Enter string2:")

String1=sorted(String1.lower())
String2=sorted(String2.lower())

if String1==String2:
   print("Strings are anagram")
else:
   print("Strings are not in anagram")
