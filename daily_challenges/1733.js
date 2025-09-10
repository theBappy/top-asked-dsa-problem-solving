/**
 * @param {number} n
 * @param {number[][]} languages
 * @param {number[][]} friendships
 * @return {number}
 */
var minimumTeachings = function (n, languages, friendships) {
    const sadUsers = new Set();

    for (const friends of friendships) {
        const u = friends[0] - 1; 
        const v = friends[1] - 1;

        const langSet = new Set(languages[u]);

        let canTalk = false;
        for (const lang of languages[v]) {
            if (langSet.has(lang)) {
                canTalk = true;
                break;
            }
        }
        if (!canTalk) {
            sadUsers.add(u);
            sadUsers.add(v);
        }
    }

   
    const language = new Array(n + 1).fill(0);
    let mostKnownLang = 0;
    for (const user of sadUsers) {
        for (const lang of languages[user]) {
            language[lang] += 1;
            mostKnownLang = Math.max(mostKnownLang, language[lang]);
        }
    }

    return sadUsers.size - mostKnownLang;

};