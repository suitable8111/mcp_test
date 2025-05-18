import pandas as pd

# CSV 불러오기
df = pd.read_csv("kbo_between_team.csv")

# 팀 리스트 정리
teams = df['팀명'].tolist()

# 팀 간 전적을 딕셔너리 형태로 정리
def get_match_record_dict(df):
    record_dict = {}
    for i, row in df.iterrows():
        team_a = row['팀명']
        for team_b in teams:
            record = row[team_b]
            if record == '■' or pd.isna(record):
                continue
            win, lose, draw = map(int, record.split('-'))
            record_dict[(team_a, team_b)] = {'win': win, 'lose': lose, 'draw': draw}
    return record_dict

record_dict = get_match_record_dict(df)

# 두 팀 간 승률 예측
def predict_win_rate(team1, team2):
    rec = record_dict.get((team1, team2)) or record_dict.get((team2, team1))
    if not rec:
        return f"{team1} vs {team2}: 기록 없음"

    total_games = rec['win'] + rec['lose'] + rec['draw']
    if total_games == 0:
        return f"{team1} vs {team2}: 경기 없음"

    if (team1, team2) in record_dict:
        win_rate = rec['win'] / total_games
        return f"{team1}의 승률: {win_rate:.2%} ({rec['win']}승 {rec['lose']}패 {rec['draw']}무)"
    else:
        win_rate = rec['lose'] / total_games
        return f"{team1}의 승률: {win_rate:.2%} ({rec['lose']}승 {rec['win']}패 {rec['draw']}무)"

# 테스트
print(predict_win_rate("LG", "한화"))
print(predict_win_rate("두산", "NC"))
print(predict_win_rate("한화", "LG"))
print(predict_win_rate("두산", "한화"))
