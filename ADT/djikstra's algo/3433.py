from typing import List

class Solution:
    def applyMessageEvent(self, event: List[str], mention_count: List[int], offline_time: List[int]):
        timestamp = int(event[1])
        ids = event[2].split()  # Split IDs in the message

        for id_ in ids:
            if id_ == "ALL":
                # Increment mention count for all users
                for i in range(len(mention_count)):
                    mention_count[i] += 1
            elif id_ == "HERE":
                # Increment mention count for users who are currently online
                for i in range(len(mention_count)):
                    # User is online if offline_time is 0 or offline time + 60 <= current timestamp
                    if offline_time[i] == 0 or offline_time[i] + 60 <= timestamp:
                        mention_count[i] += 1
            else:
                # Handle individual user ID in format "idX"
                user_index = int(id_[2:])  # Extract X from "idX"
                mention_count[user_index] += 1

    def countMentions(self, number_of_users: int, events: List[List[str]]) -> List[int]:
        mention_count = [0] * number_of_users
        offline_time = [0] * number_of_users

        # Sort events by timestamp; OFFLINE should come before MESSAGE if timestamp is equal
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))

        for event in events:
            if event[0] == "MESSAGE":
                self.applyMessageEvent(event, mention_count, offline_time)
            elif event[0] == "OFFLINE":
                timestamp = int(event[1])
                user_id = int(event[2])
                offline_time[user_id] = timestamp

        return mention_count
