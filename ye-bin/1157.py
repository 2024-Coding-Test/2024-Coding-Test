word = input().upper()
word_set = set(word)
cnt = []

for i in range(len(word_set)):
    cnt[i] = word.count(word_set[i])
        
print('?') if cnt.count(max(cnt)) > 2 else print(word_set[cnt.index(max(cnt))])