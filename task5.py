import fp_growth


def task5(pid_to_keyword):
	word_to_type = {}
	pid_to_word = {}
	paper_list = []

	with open("entity_types.txt", "r") as f:
		for line in f:
			word, e_type = line.strip('\n').split(',')
			word_to_type[word] = e_type

	for pid in pid_to_keyword.keys():
		for kw in pid_to_keyword[pid]:
			if kw in word_to_type.keys():
				if pid not in pid_to_word.keys():
					pid_to_word[pid] = set()
				pid_to_word[pid].add(kw)

	for pid in pid_to_word.keys():
		paper_list.append(pid_to_word[pid])

	result = fp_growth.find_frequent_itemsets(paper_list,10)
	for item in result:
		if len(item) != 2 or word_to_type[item[0]] != "METHOD" and word_to_type[item[0]] != "PROBLEM" or word_to_type[item[1]] != "METHOD" and word_to_type[item[1]] != "PROBLEM":
			continue
		if word_to_type[item[0]] != word_to_type[item[1]]:
			continue
		print(item)
