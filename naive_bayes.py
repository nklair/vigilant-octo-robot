class NaiveBayes:
    def __init__(self):
        self.conferences = set()
        self.keyword_count = 0
        self.conference_count = 0
        self.keyword_counts_map = {}
        self.conf_counts_map = {}
        self.conference_to_keyword_to_count = {}
                
    def train(self, pid_to_conf, pid_to_keywords):
        for pid in pid_to_conf:
            conf = pid_to_conf[pid]
            keywords = pid_to_keywords[pid]
            
            self.conference_count += 1
            self.conferences.add(conf)

            if conf not in self.conf_counts_map:
                self.conf_counts_map[conf] = 0
            self.conf_counts_map[conf] += 1

            for keyword in keywords:
                self.keyword_count += 1
                
                if keyword not in self.keyword_counts_map:
                    self.keyword_counts_map[keyword] = 0
                self.keyword_counts_map[keyword] += 1

                if conf not in self.conference_to_keyword_to_count:
                    self.conference_to_keyword_to_count[conf] = {}
                if keyword not in self.conference_to_keyword_to_count[conf]:
                    self.conference_to_keyword_to_count[conf][keyword] = 0
                self.conference_to_keyword_to_count[conf][keyword] += 1

    def classify(self, keyword):

        if keyword not in self.keyword_counts_map:
            return None

        conference_percentages = {}
        for conf in self.conferences:
            keywords_at_conference = 0
            for word in self.conference_to_keyword_to_count[conf]:
                keywords_at_conference += self.conference_to_keyword_to_count[conf][word]

            keyword_given_conference = 0
            try:
                keyword_given_conference = self.conference_to_keyword_to_count[conf][keyword] / keywords_at_conference
            except:
                pass

            p_conf = self.conf_counts_map[conf] / self.conference_count

            p_keyword = self.keyword_counts_map[keyword] / self.keyword_count

            conference_percentages[conf] = keyword_given_conference * p_conf / p_keyword

        max_conf = None
        max_conf_p = -1
        for conf in conference_percentages:
            if conference_percentages[conf] > max_conf_p:
                max_conf = conf
                max_conf_p = conference_percentages[conf]

        return max_conf
