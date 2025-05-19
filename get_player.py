import requests
from bs4 import BeautifulSoup
import csv
import datetime
import os
import pandas as pd
import subprocess

url_person_hitter = "https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx?sort=HRA_RT"

url_team_runner = "https://www.koreabaseball.com/Record/Team/Runner/Basic.aspx"
url_team_defense = "https://www.koreabaseball.com/Record/Team/Defense/Basic.aspx"
url_team_pitcher = "https://www.koreabaseball.com/Record/Team/Pitcher/Basic1.aspx"
url_team_hitter = "https://www.koreabaseball.com/Record/Team/Hitter/Basic1.aspx"

url_recent_winning = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"

def fetch_kbo_hitter_data(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 한글 깨짐 방지
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.select_one("table")
    rows = table.select("tbody tr")

    players = []

    for row in rows:
        cols = [td.text.strip() for td in row.select("td")]
        
        player = {
            "순위": cols[0],
            "팀명": cols[1],
            "타율": cols[2],
            "경기수": cols[3],
            "타석": cols[4],
            "타수": cols[5],
            "득점": cols[6],
            "안타": cols[7],
            "2루타": cols[8],
            "3루타": cols[9],
            "홈런": cols[10],
            "루타": cols[11],
            "타점": cols[12],
            "희생번트": cols[13],
            "희생플라이": cols[14],
        }
        players.append(player)


    return players

def fetch_kbo_defense_data(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 한글 깨짐 방지
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.select_one("table")
    rows = table.select("tbody tr")

    players = []

    for row in rows:
        cols = [td.text.strip() for td in row.select("td")]
        
        player = {
            "순위": cols[0],
            "팀명": cols[1],
            "경기": cols[2],
            "실책": cols[3],
            "견제사": cols[4],
            "풋아웃": cols[5],
            "어시스트": cols[6],
            "병살": cols[7],
            "수비율": cols[8],
            "포일": cols[9],
            "도루허용": cols[10],
            "도루실패": cols[11],
            "도루저지율": cols[12],
        }
        players.append(player)


    return players

def fetch_kbo_pitcher_data(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 한글 깨짐 방지
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.select_one("table")
    rows = table.select("tbody tr")

    players = []

    for row in rows:
        cols = [td.text.strip() for td in row.select("td")]
        
        player = {
            "순위": cols[0],
            "팀명": cols[1],
            "평균자책점": cols[2],
            "게임": cols[3],
            "승리": cols[4],
            "패배": cols[5],
            "세이브": cols[6],
            "홀드": cols[7],
            "승률": cols[8],
            "이닝": cols[9],
            "피안타": cols[10],
            "홈런": cols[11],
            "볼넷": cols[12],
            "사구": cols[13],
            "삼진": cols[14],
            "실점": cols[14],
            "자책점": cols[14],
            "이닝당출루허용": cols[14],
        }
        players.append(player)


    return players

def fetch_kbo_runner_data(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 한글 깨짐 방지
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.select_one("table")
    rows = table.select("tbody tr")

    players = []

    for row in rows:
        cols = [td.text.strip() for td in row.select("td")]
        
        player = {
            "순위": cols[0],
            "팀명": cols[1],
            "경기": cols[2],
            "도루시도": cols[3],
            "도루성공": cols[4],
            "도루실패": cols[5],
            "도루성공률": cols[6],
            "주루사": cols[7],
            "견재사": cols[8],
        }
        players.append(player)


    return players

def fetch_kbo_recent_winning_data(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 한글 깨짐 방지
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.select_one("table")
    rows = table.select("tbody tr")

    players = []

    for row in rows:
        cols = [td.text.strip() for td in row.select("td")]
        
        player = {
            "순위": cols[0],
            "팀명": cols[1],
            "경기": cols[2],
            "승": cols[3],
            "패": cols[4],
            "무": cols[5],
            "승률": cols[6],
            "게임차": cols[7],
            "최근10경기": cols[8],
            "연속": cols[9],
            "홈": cols[10],
            "원정": cols[11],
        }
        players.append(player)


    return players

def fetch_kbo_recent_winning_data(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 한글 깨짐 방지
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.select_one("table")
    rows = table.select("tbody tr")

    players = []

    for row in rows:
        cols = [td.text.strip() for td in row.select("td")]
        
        player = {
            "순위": cols[0],
            "팀명": cols[1],
            "경기": cols[2],
            "승": cols[3],
            "패": cols[4],
            "무": cols[5],
            "승률": cols[6],
            "게임차": cols[7],
            "최근10경기": cols[8],
            "연속": cols[9],
            "홈": cols[10],
            "원정": cols[11],
        }
        players.append(player)


    return players

def fetch_kbo_between_team_data(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 한글 깨짐 방지
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.select("table")[1]
    rows = table.select("tbody tr")

    players = {}
    
    a_team = table.select("tbody tr")[0].select("td")[0].text
    b_team = table.select("tbody tr")[1].select("td")[0].text
    c_team = table.select("tbody tr")[2].select("td")[0].text
    d_team = table.select("tbody tr")[3].select("td")[0].text
    e_team = table.select("tbody tr")[4].select("td")[0].text
    f_team = table.select("tbody tr")[5].select("td")[0].text
    g_team = table.select("tbody tr")[6].select("td")[0].text
    h_team = table.select("tbody tr")[7].select("td")[0].text
    i_team = table.select("tbody tr")[8].select("td")[0].text
    j_team = table.select("tbody tr")[9].select("td")[0].text
    teams = [
        #'팀명',
        a_team,
        b_team,
        c_team,
        d_team,
        e_team,
        f_team,
        g_team,
        h_team,
        i_team,
        j_team,
    ]
    
    for index,row in enumerate(rows):
        cols = [td.text.strip() for td in row.select("td")]
        
        player = {
            '팀명':teams[index],
            a_team: cols[1],
            b_team: cols[2],
            c_team: cols[3],
            d_team: cols[4],
            e_team: cols[5],
            f_team: cols[6],
            g_team: cols[7],
            h_team: cols[8],
            i_team: cols[9],
            j_team: cols[10],
        }
        players[teams[index]] = player

    players['팀명'] = player
    return players

def save_to_csv(data, filename="kbo.csv"):
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        if isinstance(data,list):
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        elif isinstance(data,dict):
            writer = csv.DictWriter(f, fieldnames=data)
            writer.writeheader()
            for index, key in enumerate(data.keys()):
                if index == 10:
                    break
                writer.writerow(data[key])
                
            #writer.writerows(data)

def save_daily_record(base_dir="data/records"):
    today = datetime.date.today().isoformat()
    
    recent_winning = fetch_kbo_recent_winning_data(url_recent_winning)
    between_team = fetch_kbo_between_team_data(url_recent_winning)
    
    save_to_csv(between_team,filename=f"{base_dir}/kbo_between_team_{today}.csv")
    save_to_csv(recent_winning,filename=f"{base_dir}/kbo_recent_winning_{today}.csv")
    
    git_commit_and_push(today)
    
def git_commit_and_push(, date_str: str):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"자동 업데이트: {date_str} 전적 데이터"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"[{date_str}] Git 커밋 및 푸시 완료")
    except subprocess.CalledProcessError as e:
        print(f"[{date_str}] Git 오류 발생: {e}")
        
def load_all_records(base_dir="data/records"):
    records = []
    for file in sorted(os.listdir(base_dir)):
        if file.endswith(".csv"):
            date = file.split("_")[-1].replace(".csv", "")
            df = pd.read_csv(os.path.join(base_dir, file))
            df["date"] = date
            records.append(df)
    return pd.concat(records, ignore_index=True)


def update_team_records():
    today = datetime.date.today().isoformat()

    # 기존 CSV 경로 및 새 저장 경로
    raw_path = "kbo_between_team.csv"  # 원본 or 수동 갱신
    save_dir = "record_history"
    os.makedirs(save_dir, exist_ok=True)

    df = pd.read_csv(raw_path)
    save_path = os.path.join(save_dir, f"record_{today}.csv")
    df.to_csv(save_path, index=False)
    print(f"[{today}] 기록 저장 완료: {save_path}")
    
if __name__ == "__main__":
    save_daily_record()
    
