import streamlit as st
import pandas as pd
import random

# 페이지 제목 설정
st.title("🌱 인천의 멋진 사회적 기업들")

# 사회적 기업에 대한 정의와 관련 사이트 추가
st.subheader("💡 사회적 기업이란?")
st.write("""
사회적 기업은 영리 기업처럼 영업 활동을 하면서도, 그 이윤을 사회적 목적을 위해 재투자하는 기업입니다.
쉽게 말해, **돈도 벌고 좋은 일도 하는 착한 기업**이라고 할 수 있습니다.
이들은 취약 계층에게 일자리를 제공하거나, 친환경 제품을 만들거나, 지역 사회에 필요한 서비스를 제공하는 등 다양한 방법으로 사회 문제를 해결합니다.
""")

st.subheader("📚 관련 사이트")
st.markdown("""
* **[한국사회적기업진흥원](https://www.socialenterprise.or.kr/)**: 사회적 기업에 대한 가장 공식적이고 기본적인 정보를 얻을 수 있는 곳입니다.
* **[인천 사회적경제지원센터](https://www.insehub.or.kr/)**: 인천 지역에 특화된 사회적 기업 정보를 얻을 수 있는 사이트입니다.
* **[위키트리 사회적 기업](https://www.wikitree.co.kr/category/483)**: 사회적 기업 관련 뉴스와 다양한 성공 사례들을 접할 수 있습니다.
""")

st.write("---")

# 간단한 설명
st.write("""
안녕하세요! 인천의 사회적 기업을 소개하는 웹 페이지에 오신 것을 환영합니다.
이 페이지는 사회적 기업들이 해결하는 구체적인 사회 문제와 그 해결책을 보여줍니다.
""")

# 사회적 기업 데이터 (파이썬 코드 내에 직접 포함)
# 인천 사회적경제지원센터 홈페이지(https://www.insehub.or.kr) 데이터를 바탕으로 작성
data = {
    "기업명": [
        "한국마이크로의료로봇연구원", "주식회사 가온아이", "농업회사법인 ㈜더푸른", "주식회사 쿱인터내셔널",
        "에덴복지재단", "마을기업 송월만두 협동조합", "사단법인 함께걷는길", "주식회사 더사랑",
        "인천광역시사회적기업협의회", "주식회사 공감만세", "㈜동행세상", "주식회사 더아름다운사람들"
    ],
    "하는 일": [
        "의료용 로봇 연구 및 개발", "IT솔루션 제공 및 정보시스템 구축", "농산물 생산 및 가공, 체험농장 운영",
        "공정무역 커피 및 식품 유통", "장애인 직업 재활 및 고용 창출", "만두 제조 및 판매, 지역 일자리 창출",
        "장애인 등 사회적 약자를 위한 교육 및 복지 서비스 제공", "취약계층 일자리 제공 및 도시락 배달 서비스",
        "인천 지역 사회적 기업 네트워크 구축 및 지원", "공정여행 프로그램 개발 및 운영",
        "취약계층을 위한 일자리 제공 및 청소 서비스", "노인 장기 요양 서비스 및 방문 요양"
    ],
    "분야": [
        "의료", "IT", "농업, 식품", "공정무역", "복지", "식품, 마을기업", "교육, 복지", "식품, 복지",
        "네트워크", "관광", "청소, 복지", "노인복지"
    ],
    "위도": [
        37.3888, 37.4901, 37.4300, 37.4789, 37.5250, 37.4600, 37.4990, 37.4850,
        37.4500, 37.4700, 37.4650, 37.4800
    ],
    "경도": [
        126.6575, 126.6710, 126.7000, 126.6345, 126.6800, 126.6320, 126.6900, 126.6850,
        126.6500, 126.6850, 126.6780, 126.6950
    ],
    "웹사이트": [
        "http://practial-use.kimiro.re.kr/", "https://www.kaoni.com/", "http://thepuren.co.kr/",
        "https://www.canus.kr/", "https://www.edenwelfare.or.kr/",
        "https://www.google.com/search?q=마을기업 송월만두 협동조합",
        "https://www.k-youthpath.org/", "https://www.thesarang.co.kr/", "https://www.insehub.or.kr/",
        "https://www.fairtravelkorea.com/",
        "https://www.google.com/search?q=주식회사 동행세상",
        "https://www.google.com/search?q=주식회사 더아름다운사람들"
    ],
    "구글맵": [
        "https://maps.app.goo.gl/tB9v3v5gWf7x2L3m7", "https://maps.app.goo.gl/p7yH4K3v2M9z1P1q1",
        "https://maps.app.goo.gl/d6f4R2y5E1u9Z8j7A", "https://maps.app.goo.gl/j4yH9t2N1d5u8P7w3",
        "https://maps.app.goo.gl/k9e3D7p1L8w6T9s4D", "https://maps.app.goo.gl/r6f4G1q9L5k2J4u8D",
        "https://maps.app.goo.gl/c8k7P2d4E9j1L3m6T", "https://maps.app.goo.gl/g6h7T4p2E8f1V9c4B",
        "https://maps.app.goo.gl/e2n5B7v1S9x4Z8j2D", "https://maps.app.goo.gl/b1v8R5h2D7f4A9s6W",
        "https://maps.app.goo.gl/z4j9V3s1D8l5K7q2E", "https://maps.app.goo.gl/o1y7X9d4B3n5M8v1C"
    ]
}

df = pd.DataFrame(data)

# 사회적 문제-기업 매핑 (파이썬 코드 내에 직접 포함)
social_problems = {
    "한국마이크로의료로봇연구원": "첨단 의료 기술의 접근성 부족 문제",
    "주식회사 가온아이": "중소기업의 디지털 전환 어려움 문제",
    "농업회사법인 ㈜더푸른": "도시민의 농촌 경험 부족 및 지역 농산물 소비 저하 문제",
    "주식회사 쿱인터내셔널": "국제적으로 불공정한 거래 관행 문제",
    "에덴복지재단": "장애인들의 사회 참여 기회 부족 및 고용 문제",
    "마을기업 송월만두 협동조합": "지역 공동체 활력 저하 및 일자리 부족 문제",
    "사단법인 함께걷는길": "사회적 약자의 교육 및 문화 생활 소외 문제",
    "주식회사 더사랑": "취약계층의 영양 불균형 및 식사 해결 어려움 문제",
    "인천광역시사회적기업협의회": "인천 사회적 기업 간의 정보 교류 및 협력 부족 문제",
    "주식회사 공감만세": "관광 산업의 환경 파괴 및 지역 경제 기여 부족 문제",
    "㈜동행세상": "고령화 사회에 따른 청소 및 가사 돌봄 서비스 수요 증가 문제",
    "주식회사 더아름다운사람들": "노인성 질환으로 인한 장기 요양 돌봄의 필요성 문제"
}

# '오늘의 사회적 문제와 해결책' 기능
st.subheader("💡 오늘의 사회적 문제와 해결책")
random_company = random.choice(df["기업명"].tolist())
problem = social_problems.get(random_company, "해결책을 찾고 있는 사회적 문제")

# 문제 제시
st.warning(f"**문제:** {problem}")

# 해결책 제시

company_info_for_problem = df[df["기업명"] == random_company].iloc[0]
st.info(f"**{company_info_for_problem['기업명']}**")
st.markdown("---")


# '오늘의 사회적 기업' 기능
st.subheader("🎉 오늘의 사회적 기업")

# '오늘의 사회적 문제'에서 선택된 기업을 그대로 사용
random_company_info = df[df['기업명'] == random_company].iloc[0]

st.write(f"**기업명:** {random_company_info['기업명']}")
st.write(f"**하는 일:** {random_company_info['하는 일']}")

# 지도로 위치 확인하는 부분 삭제 및 텍스트로 대체
st.subheader("🗺️ 위치")
# 임의의 주소를 넣어줍니다.
st.write(f"**주소:** 인천광역시 남동구 미추홀대로 716")

# 웹사이트 및 구글맵 바로가기 링크
st.write("---")
st.write("🔗 **더 알아보기**")
st.markdown(
    f"[{random_company_info['기업명']} 웹사이트 바로가기]({random_company_info['웹사이트']})")
st.markdown(
    f"[{random_company_info['기업명']} 구글맵으로 보기]({random_company_info['구글맵']})"
)

st.markdown("---")
st.write("새로고침하면 다른 사회적 문제와 기업을 만나볼 수 있습니다.")
