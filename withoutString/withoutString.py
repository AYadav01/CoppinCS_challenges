#first method
def withoutString_1(base, remove):

	finalString = ""
	removedString = tuple(base.split(remove))

	for  char in removedString:
		finalString += char

	return finalString

#function call
print(withoutString_1("Hello there", "e"))

#second function to acheive the same effect
def withoutString_2(base, remove):
  if remove in base:
    newString = base.replace(remove,"")
    
  print(newString)

#function call
withoutString_2("Hello therexzz", "xz")