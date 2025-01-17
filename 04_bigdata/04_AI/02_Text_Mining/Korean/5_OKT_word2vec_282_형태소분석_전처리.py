import codecs
from konlpy.tag import Twitter
from konlpy.tag import Okt
from gensim.models import word2vec  # word2vec: 문장 내부의 단어를 벡터로 변환하는 도구

# utf-16 인코딩으로 파일을 열고 글자를 출력하기
fp = codecs.open("박근혜_국정연설문_2016.txt", "r", encoding="utf-8")
# fp = codecs.open("문재인_국정연설문_2017.txt", "r", encoding="utf-8")
text = fp.read()

# 텍스트를 한 줄씩 저리하기
# twitter = Twitter()
okt = Okt()
results = []
lines = text.split("\r\n")
for line in lines:
    # 형태소 분석하기
    # 단어의 기본형 사용
    malist = okt.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        # 어미 / 조사 / 구두점 등은 대상에서 제외
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            r.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl)
# 파일로 출력하기
# wakati_file = 'hong.wakati'
wakati_file = 'park.wakati'
# wakati_file = 'moon.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))
# Word2Vec 모델 만들기
data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save('park.model')
# model.save('moon.model')
print("\n\n================ 분석완료 ================")
