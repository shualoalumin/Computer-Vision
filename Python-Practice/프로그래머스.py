import requests
from bs4 import BeautifulSoup
import pandas as pd

# 기본 URL 설정
base_url = "https://dics.co.kr/bbs/board.php?bo_table=dinews&page="

# 결과를 저장할 리스트
admission_data = []

# 페이지 범위 설정 (2-21페이지까지)
for page_num in range(1, 22):
    url = f"{base_url}{page_num}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # 게시물 리스트 선택 (HTML 구조에 따라 적절히 수정 필요)
        articles = soup.select(".list_subject a")
        
        for article in articles:
            title = article.text.strip()
            link = article.get("href")
            
            # 진학 정보만 선택
            if "진학" in title or "장학금" in title:
                admission_data.append({"Title": title, "Link": link})
    else:
        print(f"페이지 {page_num}에 접근할 수 없습니다.")

# DataFrame으로 변환 후 엑셀로 저장
df = pd.DataFrame(admission_data)
df.to_excel("DICS_admission_results.xlsx", index=False)

print("크롤링 완료 및 엑셀 저장 완료.")
