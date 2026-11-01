char = input("Enter a character = ")

match char.lower():
	case 'a' | 'e' | 'i' | 'o' | 'u' :
		print("its a consonant")
	case _:
		print("its a vovel")