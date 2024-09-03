# 베스트 앨범
# 현재 코드
def solution(genres, plays):
    answer = []
    music = {}

    for i in range(len(genres)):
        if genres[i] not in music:
            music[genres[i]] = {
                'genres': genres[i],
                'plays': [],
                'total': 0
            }

        music[genres[i]]['plays'].append({
            'index': i,
            'cnt': plays[i]
        })
        music[genres[i]]['total'] += plays[i]
    keys = music.keys()

    music_list = []
    for key in keys:
        m = music[key]
        m['plays'].sort(key=lambda x: -x['cnt'])

        music_list.append(m)

    music_list.sort(key=lambda x: -x['total'])

    for item in music_list:
        for idx, m in enumerate(item['plays']):
            if idx < 2:
                answer.append(m['index'])
    return answer
