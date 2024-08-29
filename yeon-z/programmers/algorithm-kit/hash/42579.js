// 베스트앨범
// 이전 코드
function solution(genres, plays) {
    var answer = [];
    const hash = {};
    const arr = [];
    let compare = [];

    for(let i = 0 ; i < genres.length ; i++) {
        compare.push({key: genres[i], value: plays[i], index: i});
        if(hash[genres[i]] === undefined) hash[genres[i]] = plays[i];
        else hash[genres[i]] += plays[i];
    }

    let keys = Object.keys(hash);
    keys.forEach( k => arr.push({key: k, value: hash[k]}));

    while(keys.length > 0) {
        arr.sort(function(a,b) {
            return b.value - a.value;
        })

        let first = arr.length !== 0 ? arr.shift().key : false;
        if(first === false) return answer;

        compare.sort(function(a,b) {
            return a.key === first ? -1 : 1;
        })

        let bestCandi = compare.map((c) => {
            if(c.key === first) return c;
        }).filter((b) => { return b !== undefined});

        compare = compare.filter((c) => c.key !== first);

        bestCandi.sort((a,b) => {
            if(b.value !== a.value) return b.value - a.value;
            return a.index - b.index;
        });
        bestCandi = bestCandi.filter((d,index) => index < 2);

        bestCandi.forEach((b) => {
            answer.push(b.index);
        })

        delete hash[first];
    }
    return answer;
}