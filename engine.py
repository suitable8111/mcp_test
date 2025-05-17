# 전체 MCP 파이프라인 샘플 코드

import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ------------------------------------------
# 1. 팀 기록 데이터 로드
# ------------------------------------------
team_df = pd.read_csv("kbo_team_hitters.csv")
teams = team_df["팀명"].tolist()

# 사용할 피처
features = [
    "타율", "경기수", "타석", "타수", "득점", "안타",
    "2루타", "3루타", "홈런", "루타", "타점", "희생번트", "희생플라이"
]

# ------------------------------------------
# 2. 가상 대결 데이터 생성 (학습용)
# ------------------------------------------
def generate_match_data(team_df, n=500):
    match_data = []
    for _ in range(n):
        team1, team2 = random.sample(teams, 2)
        stats1 = team_df[team_df["팀명"] == team1][features].values[0]
        stats2 = team_df[team_df["팀명"] == team2][features].values[0]

        diff = stats1 - stats2
        label = 1 if sum(stats1) > sum(stats2) else 0  # 단순 기준: 총합 우위

        row = list(diff) + [team1, team2, label]
        match_data.append(row)

    columns = [f"diff_{f}" for f in features] + ["팀1", "팀2", "승리팀"]
    return pd.DataFrame(match_data, columns=columns)

match_df = generate_match_data(team_df)

# ------------------------------------------
# 3. 모델 학습
# ------------------------------------------
X = match_df[[col for col in match_df.columns if col.startswith("diff_")]]
y = match_df["승리팀"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print(f"✅ 모델 정확도: {accuracy_score(y_test, model.predict(X_test)):.2f}")

# ------------------------------------------
# 4. 예측 함수 (MCP 연결)
# ------------------------------------------
def predict_win(team1, team2):
    stats1 = team_df[team_df["팀명"] == team1][features].values[0]
    stats2 = team_df[team_df["팀명"] == team2][features].values[0]
    diff = stats1 - stats2
    prob = model.predict_proba([diff])[0]
    return {
        team1: round(prob[1] * 100, 2),
        team2: round(prob[0] * 100, 2)
    }

# ------------------------------------------
# 5. 테스트
# ------------------------------------------
if __name__ == "__main__":
    team1 = "LG"
    team2 = "두산"
    result = predict_win(team1, team2)
    print(f"{team1} 승률: {result[team1]}%\n{team2} 승률: {result[team2]}%")
