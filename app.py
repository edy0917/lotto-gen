import os
from PIL import Image, ImageDraw, ImageFont
import datetime

# 1. 데이터 수집 함수 (예시로 텍스트 리스트 생성)
def get_twitter_data():
    # 실제 구현 시 여기서 트위터 수집 라이브러리를 사용합니다.
    # 현재는 예시 데이터를 생성합니다.
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    tweets = [
        f"📅 날짜: {today}",
        "🔥 오늘의 인기 키워드: #로또 #당첨운",
        "💬 주요 의견: 오늘 번호 조합 대박이네요!",
        "🚀 리트윗 많은 글: 이번 주 명당 정보 공유합니다.",
        "✨ AI 분석 결과: 행운의 숫자는 7, 24, 38"
    ]
    return tweets

# 2. 이미지 생성 함수
def create_image(data):
    # 배경 이미지 생성 (800x600, 하늘색 배경)
    img = Image.new('RGB', (800, 600), color=(235, 245, 255))
    d = ImageDraw.Draw(img)
    
    # 폰트 설정 (GitHub 서버에는 한글 폰트가 없으므로 나중에 폰트 파일도 같이 올려야 함)
    # 여기서는 기본 폰트를 사용하지만, 한글 출력려면 .ttf 파일이 필요합니다.
    try:
        font = ImageFont.truetype("NanumGothic.ttf", 25)
    except:
        font = ImageFont.load_default()

    # 텍스트 그리기
    margin = 50
    offset = 100
    d.text((margin, 50), "오늘의 트위터 요약 리포트", fill=(0, 50, 150))
    
    for line in data:
        d.text((margin, offset), line, fill=(50, 50, 50), font=font)
        offset += 60

    # images 폴더가 없으면 생성
    if not os.path.exists('images'):
        os.makedirs('images')
        
    # 이미지 저장
    img.save('images/today_summary.png')
    print("이미지 생성 완료: images/today_summary.png")

if __name__ == "__main__":
    tweets = get_twitter_data()
    create_image(tweets)
