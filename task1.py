def task1(pid_to_txt, pid_to_author_sequence, pid_to_title_year_conf, aid_to_author_name):
    while True:
        try:
            print("\nWhich action would you like to take?")
            print("\t1. Word frequency")
            print("\t2. Title length")
            print("> ", end='', flush=True)

            choice = -1
            choice = int(input())
            if choice < 1 or choice > 2:
                print("Error: Please enter the number corresponding to one of the choices above")
                continue
            break
        except ValueError:
            print("Error: Please enter the number corresponding to one of the choices above")

    # Perform the correct task based on the choice of the user
    if choice == 1:
        print("Which word would you like to find?")
        print("> ", end='', flush=True)
        wordToFind = input()
        for author_id in word_frequency(wordToFind, pid_to_txt, pid_to_author_sequence, 5):
            print(aid_to_author_name[author_id])
    elif choice == 2:
        for author_id in title_length(pid_to_txt, pid_to_author_sequence, pid_to_title_year_conf, 5):
            print(aid_to_author_name[author_id])
    else:
        print("This option has not yet been implemented")

def word_frequency(wordToFind,  pid_to_txt, pid_to_author_sequence, authorsToReturn=3):
    pid_to_word_frequency = {}
    author_to_word_frequency = {}
    for pid in pid_to_txt.keys():
        with open(pid_to_txt[pid], 'r') as f:
            for line in f:
                words = line.split()
                for word in words:
                    if word == wordToFind:
                        if not pid in pid_to_word_frequency.keys():
                            pid_to_word_frequency[pid] = 1
                        else:
                            pid_to_word_frequency[pid] += 1

        for pid1 in pid_to_author_sequence.keys():
            for author in pid_to_author_sequence[pid1]:
                aid = author['aid']
                if not aid in author_to_word_frequency.keys() and pid1 in pid_to_word_frequency.keys():
                    author_to_word_frequency[aid] = {
                        'freq': pid_to_word_frequency[pid1],
                        'papers': 1
                    }
                elif pid1 in pid_to_word_frequency.keys():
                    author_to_word_frequency[aid]['freq'] += pid_to_word_frequency[pid1]
                    author_to_word_frequency[aid]['papers'] += 1
    highest_use_authors = [None]*authorsToReturn
    for author in author_to_word_frequency.keys():
        if author_to_word_frequency[author]['papers'] >= 3:
            i = 0
            curr_author = author

            while i < authorsToReturn and highest_use_authors[i] != None and float(author_to_word_frequency[highest_use_authors[i]]['freq'])/float(author_to_word_frequency[highest_use_authors[i]]['papers']) > float(author_to_word_frequency[author]['freq'])/float(author_to_word_frequency[author]['papers']):
                i += 1
                
            if i == authorsToReturn - 1:
                highest_use_authors[i] = curr_author
            else:    
                while i < authorsToReturn - 1:
                    a = curr_author
                    curr_author = highest_use_authors[i+1]
                    highest_use_authors[i] = a
                    i += 1

    return highest_use_authors

def title_length(pid_to_txt, pid_to_author_sequence, pid_to_title_year_conf, authorsToReturn=3):
    pid_to_title_length = {}
    author_to_title_length = {}
    for pid in pid_to_txt.keys():
        pid_to_title_length[pid] = len(pid_to_title_year_conf[pid]['title'])

        for pid1 in pid_to_author_sequence.keys():
            for author in pid_to_author_sequence[pid1]:
                aid = author['aid']
                if not aid in author_to_title_length.keys() and pid1 in pid_to_title_length.keys():
                    author_to_title_length[aid] = {
                        'freq': pid_to_title_length[pid1],
                        'papers': 1
                    }
                elif pid1 in pid_to_title_length.keys():
                    author_to_title_length[aid]['freq'] += pid_to_title_length[pid1]
                    author_to_title_length[aid]['papers'] += 1
    highest_use_authors = [None]*authorsToReturn
    for author in author_to_title_length.keys():
        if author_to_title_length[author]['papers'] >= 3:
            i = 0
            curr_author = author

            while i < authorsToReturn and highest_use_authors[i] != None and float(author_to_title_length[highest_use_authors[i]]['freq'])/float(author_to_title_length[highest_use_authors[i]]['papers']) > float(author_to_title_length[author]['freq'])/float(author_to_title_length[author]['papers']):
                i += 1
                
            if i == authorsToReturn - 1:
                highest_use_authors[i] = curr_author
            else:    
                while i < authorsToReturn - 1:
                    a = curr_author
                    curr_author = highest_use_authors[i+1]
                    highest_use_authors[i] = a
                    i += 1

    return highest_use_authors


