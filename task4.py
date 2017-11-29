import fp_growth

def task4(aid_to_author_name, pid_to_author_sequence):
    while True:
        try:
            print("\nWhich action would you like to take?")
            print("\t1. Frequent author sets")
            print("\t2. Advisor-advisee relations")
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
        while True:
            try:
                print("What would you like the minimum support to be?")
                print("> ", end='', flush=True)
                minsup = -1
                minsup = int(input())
                if minsup < 1:
                    print("Error: minimum support must be greater than 0")
                    continue
                break
            except ValueError:
                print("Error: please enter an integer value for the minimum support")

        for author_set in get_closed_sets(frequent_author_sets(pid_to_author_sequence, minsup)):
            author_name_set = map(lambda x: aid_to_author_name[x], author_set)
            print(', '.join(author_name_set))
    elif choice == 2:
        relations = advisor_advisee_relations()
        for author_id in relations.keys():
            author_name = aid_to_author_name[author_id]
            advisee_ids = relations[author_id]
            advisee_names = map(lambda x: aid_to_author_name[x], advisee_ids)
            print(author_name + " -> " + ', '.join(advisee_names))
    else:
        print("This option has not yet been implemented")


def frequent_author_sets(pid_to_author_sequence, minsup):
    paper_authors = get_author_ids_for_papers(pid_to_author_sequence)
    return fp_growth.find_frequent_itemsets(paper_authors.values(), minsup)

# Function to return a dict mapping paper ids to lists of author ids
def get_author_ids_for_papers(pid_to_author_sequence):
    transactions = {}
    for pid in pid_to_author_sequence:
        transactions[pid] = list(map(lambda x: x['aid'], pid_to_author_sequence[pid]))

    return transactions

def get_closed_sets(list_of_sets):
    # Turn the list of sets into a set of sets
    set_of_sets = set(map(lambda x: frozenset(x), list_of_sets))

    # Define a function to determine if a given set is a subset of any other set
    def isSubsetOfAnySets(s):
        for s2 in set_of_sets:
            if s.issubset(s2) and s != s2:
                return True
        return False

    # Filter to find the closed sets
    closed_sets = filter(lambda x: not isSubsetOfAnySets(x), set_of_sets)
    return closed_sets
