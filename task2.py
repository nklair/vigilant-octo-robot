#! /usr/bin/python3


# phrase is the phrase to get the support of in all the papers
# pid_to_text is a dictionary of pid to the name of the text file of that paper
def phrase_support(phrase, pid_to_text):
	support = 0
	for pid in pid_to_text:
		with open(pid_to_text[pid], 'r') as f:
			for line in f:
				support += line.count(phrase) # counts all occurences of the phrase in the paper
	return support

# phrase_dict is a dictionary that maps a phrase to all its equivalent phrases
#	Example: {'Support Vector Machine': ['Support Vector Machine', 'support vector machine', 'SVM', 'svm']}
# pid_to_text is the dictionary that maps all pids to the paper's text file
def equivalent_phrase_support(phrase_dict, pid_to_text):
	result = {}
	with open('keyword_usage.txt', 'w+') as f:
		for phrase in phrase_dict:
			#phrase_sup = 0
			for word in phrase_dict[phrase]:
				for p in word:
					for r in word[p]:
						if r not in result.keys():
							result[r] = 0
							result[r] += phrase_support(r, pid_to_text)
							f.write(str(r) + ',' + str(result[r])+ '\n')
							#print( str(r) + ': ' + str(result[r]))
		#result[phrase] = phrase_sup
	return result

def top_supported_phrases(phrase_dict, pid_to_text,amount=10):
	sup = equivalent_phrase_support(phrase_dict, pid_to_text)
	result = []
	i = 0
	for key, value in sorted(sup.items(), key=lambda k,v: (v,k)):
		if i == amount:
			break
		result.append((key,value))
		i += 1
		#print "%s: %s" % (key, value)
	return result
def task2(phrase_dict, pid_to_text):
	print("This task will get the most common entities. Please enter how many you would like to see:")
	print(top_supported_phrases(phrase_dict, pid_to_text, int(input())))
