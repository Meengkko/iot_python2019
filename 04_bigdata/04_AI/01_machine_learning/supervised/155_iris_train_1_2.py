from sklearn import svm, metrics
import random, re

csv = []
with open('iris.csv', 'r', encoding='utf-8') as fp:
    # 한 줄씩 읽어 들이기
    for line in fp:
        line = line.strip()     # 줄바꿈 제거
        cols = line.split(',')  # 쉼표로 자르기
        # 문자열 데이터를 숫자로 변환하기
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

# 가장 앞 줄의 헤더 제거
del csv[0]

# 데이터 셔플하기(섞기)
random.shuffle(csv)
# 학습 전용 데이터와 테스트 전용 데이터 분할하기(2:1 비율)
total_len = len(csv)
train_len = int(total_len * 2 / 3)
train_data = []
train_label = []


for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]
    train_data.append(data)
    train_label.append(label)

# 데이터를 학습시키고 예측하기
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(train_data)

# 정답률 구하기
st_ok = 0
vs_ok = 0
vg_ok = 0

for idx, answer in enumerate(train_label):
    p = pre[idx]
    if p == answer:
        if p == 'Iris-setosa':
            st_ok += 1
        elif p == 'Iris-versicolor':
            vs_ok += 1
        elif p == 'Iris-virginica':
            vg_ok += 1

print("전체 데이터 수: %d" % total_len)
print("학습 전용 데이터 수: %d" % train_len)
print(f"Setosa 정답률 = {st_ok*2}%")
print(f"Versicolor 정답률 = {vs_ok*2}%")
print(f"Verginica 정답률 = {vg_ok*2}%")
