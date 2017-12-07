#! /usr/bin/python3


problem_keywords = ["problem","difficult","question"]
method_keywords = ["method", "approach", "model","solution"]
metric_keywords = ["metric", "measure", "normal"]
dataset_keywords = ["data", "set", "group"]



def task3(pid_to_t):
	problems = []
	methods = []
	metrics = []
	datasets = []
	phrase_to_counts = {}
	with open("keyword_usage.txt",'r') as f:
		for line in f:
			word, num = line.strip('\n').split(',')
			phrase_to_counts[word] = [0,0,0,0]
	#with open("microsoft/PaperKeywords.txt","r") as f:
	output = open("entity_types.txt", "w+")
	for word in phrase_to_counts.keys():
		for pid in pid_to_t.keys():
			with open(pid_to_t[pid],'r') as file:
				#print("opening new file: " + pid_to_t[pid])
			#for word in phrase_to_counts.keys():
				#word, num = line.strip('\n').split(',')
				for l in file:
					if l.count(word) != 0:
						for p in problem_keywords:
							if p in l:
								phrase_to_counts[word][0] = phrase_to_counts[word][0] + 1
						for meth in method_keywords:
							if meth in l:
								phrase_to_counts[word][1] = phrase_to_counts[word][1] + 1
						for metr in metric_keywords:
							if metr in l:
								phrase_to_counts[word][2] = phrase_to_counts[word][2] + 1
						for d in dataset_keywords:
							if d in l:
								phrase_to_counts[word][3] = phrase_to_counts[word][3] + 1
		print("committing entity type")
		li = phrase_to_counts[word]
		i = li.index(max(li))
		if i == 0:
			output.write(str(word) + ",PROBLEM\n")
		elif i == 1:
			output.write(str(word) + ",METHOD\n")
		elif i == 2:
			output.write(str(word) + ",METRIC\n")
		elif i == 3:
			output.write(str(word) + ",DATASET\n")
		output.flush()


			
	#print(phrase_to_counts)
#	for phrase in phrase_to_counts:
#		li = phrase_to_counts[word]
#		i = li.index(max(li))
#		if i == 0:
#			problems.append(phrase)
#		elif i == 1:
#			methods.append(phrase)
#		elif i == 2:
#			metrics.append(phrase)
#		elif i == 3:
#			datasets.append(phrase)
#	with open("entity_types.txt", "w+") as f:
#		for p in problems:
#			
#		for meth in methods:
#			
#		for metr in metrics:
#			
#		for ds in datasets:
#			
#		f.flush()




