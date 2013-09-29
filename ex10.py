tabby_cat = "\tI'm tabbed in.%s"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list : 
\t* Cat Food
\t* Fishies
\t* Mofo Homies
\t* Eat Shit
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

escape_sequence = ["/","-","|","\\","|"]
while True:
	for i in escape_sequence:
		print "%s\r" % i,