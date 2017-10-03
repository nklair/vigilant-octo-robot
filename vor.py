#! /usr/bin/python3

pid_to_txt = {}
new_dict = {}
pid_to_title_year_conf = {}
pid_to_keyword = {}
pid_to_author_sequence = {}
aid_to_author_name = {}
viewed_conferences = {'icdm', 'kdd', 'wsdm', 'www'}

# Function to load in the data and store it in memory
def load_data():
    with open('microsoft/Papers.txt', 'r') as f:
        for line in f:
            split_line = line.split('\t')
            if split_line[7] in viewed_conferences:
                pid = split_line[0]
                title = split_line[2]
                year = split_line[3]
                conf = split_line[7]
                pid_to_title_year_conf[pid] = {
                        'title': title,
                        'year': year,
                        'conf': conf,
                }

               # Fill in other dicts with the PID information
                pid_to_txt[pid] = ''
                pid_to_keyword[pid] = set()
                pid_to_author_sequence[pid] = []

    with open('microsoft/index.txt', 'r') as f:
        for line in f:
            split_line = line.split('\t')
            pid = split_line[2]
            if pid in pid_to_txt:
                pid_to_txt[pid] = 'text/' + split_line[0] + '/' + split_line[1] + '.txt'
        for pid in pid_to_txt.keys():
            if pid_to_txt[pid] != '':
                new_dict[pid] = pid_to_txt[pid]
        #pid_to_txt = new_dict

    with open('microsoft/PaperAuthorAffiliations.txt', 'r') as f:
        for line in f:
            split_line = line.split('\t')
            pid = split_line[0]
            if pid in pid_to_author_sequence:
                pid_to_author_sequence[pid].append({
                        'aid': split_line[1],
                        'fid': split_line[2],
                        'aff': split_line[4],
                        'seqNum': split_line[5]
                })
                aid_to_author_name[split_line[1]] = ''

    with open('microsoft/Authors.txt', 'r') as f:
        for line in f:
            aid, name = line.split('\t')
            if aid in aid_to_author_name:
                aid_to_author_name[aid] = name

    with open('microsoft/PaperKeywords.txt', 'r') as f:
        for line in f:
            pid, keyword, kid = line.split('\t')
            if pid in pid_to_keyword:
                pid_to_keyword[pid].add(keyword)

def word_frequency(wordToFind, authorToReturn=3):
    pid_to_word_frequency = {}
    author_to_word_frequency = {}
    for pid in new_dict.keys():
        #print(pid_to_txt)
        if not pid_to_txt[pid] == '':
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
                    #if pid1 in author_to_word_frequency.keys():
                        author_to_word_frequency[aid] = {
                            'freq': pid_to_word_frequency[pid1],
                            'papers': 1
                        }
                elif pid1 in pid_to_word_frequency.keys():
                    author_to_word_frequency[aid]['freq'] += pid_to_word_frequency[pid1]
                    author_to_word_frequency[aid]['papers'] += 1
    print(author_to_word_frequency)
    for author in author_to_word_frequency.keys():
        print(str(author) + ': ' + str(author_to_word_frequency[author]['freq']) + str(author_to_word_frequency[author]['papers']))



if __name__ == '__main__':
    load_data()

    print('Papers: ' + str(len(pid_to_txt)))
    print('Authors: ' + str(len(aid_to_author_name)))

    word_frequency('matrix', 3)

