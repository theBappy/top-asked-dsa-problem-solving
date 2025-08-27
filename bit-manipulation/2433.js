var findArray = function(pref) {
    const n = pref.length
    for(let i = n-1; i > 0; i--){
        pref[i] = pref[i] ^ pref[i-1]
    }
    return pref
};