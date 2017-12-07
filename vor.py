import task1
import task2
import task3
import task4
import task6
import task7
import task5

pid_to_txt = {}
new_dict = {}
pid_to_title_year_conf = {}
pid_to_keyword = {}
pid_to_author_sequence = {} # Maps the paper id to a list of author ids
aid_to_author_name = {} # Maps an author id to the author's name
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
                aid_to_author_name[aid] = name.strip()

    with open('microsoft/PaperKeywords.txt', 'r') as f:
        for line in f:
            pid, keyword, kid = line.split('\t')
            if pid in pid_to_keyword:
                pid_to_keyword[pid].add(keyword)

if __name__ == '__main__':
    load_data()

    while True:
        try:
            print("\nWhich method would you like to use?")
            print("\t1. Task 1: Data Preprocessing")
            print("\t2. Task 2: Entity Mining")
            print("\t3. Task 3: Entity Typing")
            print("\t4. Task 4: Collaboration Discovery")
            print("\t5. Task 5: Problem-Method Association Mining")
            print("\t6. Task 6: Conference Classification")
            print("\t7. Task 7: Paper Clustering")
            print("\t8. Exit")
            print("> ", end='', flush=True)

            choice = -1
            choice = int(input())
            if choice < 1 or choice > 8:
                print("Error: Please enter the number corresponding to one of the choices above")
                continue
        except ValueError:
            print("Error: Please enter the number corresponding to one of the choices above")
            continue

        # Perform the correct task based on the choice of the user
        if choice == 1:
            task1.task1(new_dict, pid_to_author_sequence, pid_to_title_year_conf, aid_to_author_name)
        elif choice ==2:
            phrases = {}
            for pid in pid_to_keyword:
                for word in pid_to_keyword[pid]:
                    if word not in phrases.keys():
                            phrases[word] = []
                    phrases[word].append(pid_to_keyword)
            task2.task2(phrases, new_dict)
        elif choice == 3:
            task3.task3(new_dict)
        elif choice == 4:
            task4.task4(aid_to_author_name, pid_to_author_sequence)
        elif choice == 6:
            task6.task6(pid_to_title_year_conf, pid_to_keyword, pid_to_author_sequence)
        elif choice == 7:
            task7.task7(pid_to_title_year_conf, pid_to_keyword, pid_to_author_sequence)
        elif choice == 5:
            task5.task5(pid_to_keyword)
        elif choice == 8:
            break
        else:
            print("This option has not yet been implemented")

