from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from get_player import save_daily_record
import uvicorn

app = FastAPI()

# 스케줄러 설정
scheduler = BackgroundScheduler()
scheduler.add_job(save_daily_record, 'interval', days=1)
scheduler.start()

@app.get("/")
def read_root():
    return {"message": "KBO 팀 전적 서버 정상 작동 중"}

# 앱 시작 시 즉시 1회 실행 (선택)
save_daily_record()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
