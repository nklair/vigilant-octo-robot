from sklearn.cluster import KMeans
import numpy as np

def task7(pid_to_title_year_conf, pid_to_keyword, pid_to_author_sequence):
    data = format_data(pid_to_title_year_conf, pid_to_keyword, pid_to_author_sequence)
    print(sklearn_kmeans(data))

def format_data(pid_to_title_year_conf, pid_to_keyword, pid_to_author_sequence):
    data = []
    for pid in pid_to_title_year_conf:
        tyc = None
        keywords = None
        author_info = None
        try:
            tyc = pid_to_title_year_conf[pid]
            keywords = list(pid_to_keyword[pid])
            author_info = pid_to_author_sequence[pid]
        except:
            continue
       
        if len(keywords) < 1 or len(author_info) < 1:
            continue

        current_row = []
        current_row.append(string_hash(tyc['year']))
        current_row.append(int(tyc['year'])) 
        current_row.append(string_hash(tyc['conf']))
        current_row.append(string_hash(keywords[0]))
        current_row.append(string_hash(author_info[0]['aid']))

        data.append(current_row)

    return data

def sklearn_kmeans(data):
    x = np.array(data)
    kmeans = KMeans().fit(x)
    return kmeans.cluster_centers_

def string_hash(s):
    val = 0
    s = s.strip()
    for character in s:
        val += ord(character)

    return val
