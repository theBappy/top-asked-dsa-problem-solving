//Approach - Simply sort and simulate
//T.C : O(E log E + E * N), N = number of users , E = number of events
//S.C : O(N + E)


class Solution {
    // Function to process a MESSAGE event
    applyMessageEvent(event, mentionCount, offlineTime) {
        const timestamp = parseInt(event[1]);
        const ids = event[2].split(' '); // Split IDs in the message

        for (const id of ids) {
            if (id === "ALL") {
                // Increment mention count for all users
                for (let i = 0; i < mentionCount.length; i++) {
                    mentionCount[i]++;
                }
            } else if (id === "HERE") {
                // Increment mention count for users currently online
                for (let i = 0; i < mentionCount.length; i++) {
                    if (offlineTime[i] === 0 || offlineTime[i] + 60 <= timestamp) {
                        mentionCount[i]++;
                    }
                }
            } else {
                // Handle individual user ID in format "idX"
                const userIndex = parseInt(id.slice(2)); // Extract X from "idX"
                mentionCount[userIndex]++;
            }
        }
    }

    countMentions(numberOfUsers, events) {
        const mentionCount = new Array(numberOfUsers).fill(0);
        const offlineTime = new Array(numberOfUsers).fill(0);

        // Sort events by timestamp; OFFLINE should come before MESSAGE if timestamp is equal
        events.sort((a, b) => {
            const t1 = parseInt(a[1]);
            const t2 = parseInt(b[1]);
            if (t1 === t2) {
                return a[0] === "OFFLINE" ? -1 : 1; // OFFLINE first
            }
            return t1 - t2;
        });

        for (const event of events) {
            if (event[0] === "MESSAGE") {
                this.applyMessageEvent(event, mentionCount, offlineTime);
            } else if (event[0] === "OFFLINE") {
                const timestamp = parseInt(event[1]);
                const userId = parseInt(event[2]);
                offlineTime[userId] = timestamp;
            }
        }

        return mentionCount;
    }
}
