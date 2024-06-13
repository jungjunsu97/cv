import requests
import datetime

#발급받은 키및 정보를제공하는 api의 기본url
API_KEY = 'dc7a6dea24cd57dca0a9bd5cf400b7c6'  
BASE_URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'

#현재 상영중인 영화 목록을 가저오는 함수
def get_current_movies():
    yesterday = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y%m%d')
    params = {
        'key': API_KEY,       #api키
        'targetDt': yesterday, # 조회할 날짜
        'itemPerPage': 10, #가져올 영화개수
        'wideAreaCd': '0105001'  # Optional: 특정 지역의 박스오피스 정보를 가져옵니다.
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get('boxOfficeResult', {}).get('dailyBoxOfficeList', [])
    else:
        print("Error:", response.status_code, response.reason)
        return []

def main():
    movies = get_current_movies()
    if not movies:
        print("No current movies found.")
        return
    
    print(f"Current Movies ({(datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y-%m-%d')}):")
    for i, movie in enumerate(movies):
        print(f"{i + 1}. {movie['movieNm']} (Accumulate Audience: {movie['audiAcc']})")

if __name__ == '__main__':
    main()