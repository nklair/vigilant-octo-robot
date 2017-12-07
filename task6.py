from decision_tree import decision_tree
from decision_tree.information_gain import information_gain
from decision_tree.gain_ratio import gain_ratio
from decision_tree.delta_gini import delta_gini
from naive_bayes import NaiveBayes

def task6(pid_to_title_year_conf, pid_to_keyword, pid_to_author_sequence):
    action_choice = -1
    splitting_choice = -1
    while True:
        try:
            print("\nWhich action would you like to take?")
            print("\t1. View training statistics")
            print("\t2. Identify conference by keyword")
            print("> ", end='', flush=True)

            action_choice = -1
            action_choice = int(input())
            if action_choice < 1 or action_choice > 2:
                print("Error: Please enter the number corresponding to one of the choices above")
                continue
            break
        except ValueError:
            print("Error: Please enter the number corresponding to one of the choices above")

    pid_to_conf = {}
    for pid in pid_to_title_year_conf:
        pid_to_conf[pid] = pid_to_title_year_conf[pid]['conf']

    nb = NaiveBayes()
    nb.train(pid_to_conf, pid_to_keyword)

    # Perform the correct task based on the choice of the user
    if action_choice == 1:
        tests_completed = 0
        tests_successful = 0
        for pid in pid_to_conf:
            if len(pid_to_keyword[pid]) < 1:
                continue
            conf = nb.classify(list(pid_to_keyword[pid])[0])
            if conf == pid_to_conf[pid]:
                tests_successful += 1
            tests_completed += 1

            if tests_completed >= 100:
                break
        print("Accuracy: " + str(tests_successful / tests_completed) + "%")
    elif action_choice == 2:
        result = None
        while not result:
            print("Which keyword would you like to look for?")
            print("> ", end='', flush=True)

            keyword = input().lower()

            result = nb.classify(keyword)

            if not result:
                print("I'm sorry. The keyword you are looking for does not appear in any acedemic papers.")
            else:
                print("It appears that your keyword is likely from the " + result + " conference.")
    else:
        print("This option has not yet been implemented")

def load_data(pid_to_title_year_conf, pid_to_keyword, pid_to_author_sequence):
    pids = set(pid_to_title_year_conf.keys()) & set(pid_to_keyword.keys()) & set(pid_to_author_sequence.keys())

    confs = set(map(lambda x: pid_to_title_year_conf[x]['conf'], list(pid_to_title_year_conf)))
    keywords = set()
    for pid in pid_to_keyword:
        keywords = keywords | set(pid_to_keyword[pid])

    authors = set()
    for pid in pid_to_author_sequence:
        for listing in pid_to_author_sequence[pid]:
            authors.add(listing['aid'])

    # Map each value (conf, keyword, and author) to a unique index starting at 0
    index = 0
    value_to_index_mapping = {}
    
    for value in keywords:
        value_to_index_mapping[value] = index
        index += 1

    for value in authors:
        value_to_index_mapping[value] = index
        index += 1

    index += 1 # Add extra space for conference field

    # For each pid, go through, create an array of the appropriate size, and set the appropriate values in the data
    data = []
    for pid in pids:
        current_data = [0 for x in range(index)]

        # Mark off conferences
        current_data[-1] = pid_to_title_year_conf[pid]['conf']

        # Mark off keywords
        for keyword in pid_to_keyword[pid]:
            current_data[value_to_index_mapping[keyword]] = 1

        # Mark off authors
        for author in pid_to_author_sequence[pid]:
            current_data[value_to_index_mapping[author['aid']]] = 1

        data.append(current_data)

    return data
