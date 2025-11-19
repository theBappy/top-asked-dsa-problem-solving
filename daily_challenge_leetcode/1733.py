

# Tc = O(F * L)
from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        sad_users = set()
        
        for friends in friendships:
            u = friends[0] - 1  # convert this to 0 base indexing
            v = friends[1] - 1

            lang_set = set(languages[u])

            can_talk = False
            for lang in languages[v]:
                if lang in lang_set:
                    can_talk = True
                    break
            if not can_talk:
                sad_users.add(u)
                sad_users.add(v)

        # find max known language among sad users
        language = [0] * (n + 1)
        most_known_lang = 0
        for user in sad_users:
            for lang in languages[user]:
                language[lang] += 1
                most_known_lang = max(most_known_lang, language[lang])

        return len(sad_users) - most_known_lang
