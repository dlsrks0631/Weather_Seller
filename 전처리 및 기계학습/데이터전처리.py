# 해당 코드는 진짜 데이터 전처리만 한 코드입니다.
# 원래는 날씨 데이터를 넣고 했어야 했는데 없어서 카드내역만 했습니다.
# 저는 아나콘다로 실행했습니다
# 라인 89에 궁금한 점도 써놓았는데요 봐주시면 감사하겠습니다.

import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler

# 데이터 불러오기 

# 지역이름을 바꾸셔야 해당이름으로 csv파일이 생성됩니다.
name = "강원도"

# 제가 올린 파일을 입력하면 지역별로 데이터 전처리가 가능합니다.
df = pd.read_csv(r"C:\Users\user\Desktop\캡스톤\롯데카드내역_지역(원본)\강원도_data.csv", encoding = 'utf-8')


# 결측치 처리
# 결측치를 처리해 본 결과 결측치가 없지만, 
#지금 결측치처리는 결측치 처리 전후의 검증이 없고 처리 대상이 전체 데이터셋이 아니라 특정 열(sl_am)만 처리해서 
#전체 데이터를 처리하고 처리 전후 검증할 수 있는 코드로 변경했습니다

# 각 열의 결측치 개수를 확인합니다.
missing_values = df.isnull().sum()

# 결측치가 하나라도 있는 경우에만 처리를 수행합니다.
if missing_values.any():
    # SimpleImputer 객체를 생성합니다. 여기서는 'median' 전략을 사용합니다.
    imputer = SimpleImputer(strategy='median')
    
    # 결측치를 중앙값으로 대체합니다.
    df_filled = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    
    # 대체된 데이터 프레임의 결측치를 다시 확인합니다.
    if df_filled.isnull().sum().any():
        print("결측치가 여전히 존재합니다.")
    else:
        print("모든 결측치가 처리되었습니다.")
        # 결측치가 처리된 데이터 프레임을 반환하거나 저장합니다.
        df = df_filled
else:
    print("결측치가 없습니다.")


# 이상치 처리 (IQR 사용)
# 지금 코드처럼 전체 데이터에서 총결제금액에서만 이상치를 검출하는 것보다 업종에 따른 총결제금액의 이상치를 검출하는 것이 좋을 것 같아서 변경했습니다.
# 제가 데이터들의 표준편차(std)와 평균값(mean)를 비교한 결과로 20개의 업종 모두 평균값보다 표준편차가 크므로 데이터가 넓게 분포함을 알수 있습니다.
# 이는 정규분포를 보이는 데이터에 적합한 Z-score보다 비정규 분포를 보이는 데이터에 알맞은 IQR규칙을 사용하는 것이 낫다고 판단하여 변경하였습니다.

# 이 코드는 결제업종에 따른 총결제금액의 이상치를 처리하는 코드입니다.

# 결과를 저장할 DataFrame을 준비합니다.
filtered_df = pd.DataFrame()

# 결제업종의 유니크한 값을 가져옵니다.
unique_categories = df['결제업종'].unique()

for category in unique_categories:
    # 각 결제업종에 해당하는 데이터만 추출합니다.
    category_data = df[df['결제업종'] == category]
    
     # 해당 데이터의 총결제금액의 Q1, Q3 및 IQR을 계산합니다.
    Q1 = category_data['총결제금액'].quantile(0.25)
    Q3 = category_data['총결제금액'].quantile(0.75)
    IQR = Q3 - Q1
    
    # IQR 규칙에 따라 이상치를 필터링합니다.
    filtered_category_data = category_data[~((category_data['총결제금액'] < (Q1 - 1.5 * IQR)) |
                                            (category_data['총결제금액'] > (Q3 + 1.5 * IQR)))]
    
    # 필터링된 데이터를 결과 DataFrame에 추가합니다.
    filtered_df = pd.concat([filtered_df, filtered_category_data], axis=0)

# 필터링된 데이터를 새로운 CSV 파일로 저장합니다.
# name = 지역이름
filtered_df.to_csv(f"{name}_filtered.csv", index=False)


# 이상치처리된 파일읽기
data = pd.read_csv(f"{name}_filtered.csv", encoding = 'utf-8')


# 정규화 (RobustScaler 사용)
# 원래 코드에는 StandardScaler로 정규화를 하고 있는데 이 방법은 데이터가 정규분포에 가까울때 좋다는 gpt의 말과 
# 데이터를 이상치 처리했기 때문에 평균과 표준편차의 값이 많이 차이 나지 않지만 제가 검사해본 결과
# 여전히 평균 값보다 큰 표준편차를 가진 업종들이 있기 때문에 RobustScaler로 변경했습니다 

# 궁금한 점이 결제업종은 스케일링 하지 못했는데 (RobustScaler는 string을 스케일링 못함)
# 그럼 업종은 나중에 인공지능학습 기계학습? 할 때 다른 feature 값들과 연관되어 값을 도출해낼 수 있나요?
# 아직 기계학습 부분은 공부를 못해서,,, 이 부분을 모르겠네요

# 선택한 특성들에 대해서만 스케일링합니다.
features_to_scale = ['성별', '연령대','결혼유무','자녀유무','거주지일치여부','총결제금액','결제개수']

# RobustScaler 인스턴스를 생성합니다.
scaler = RobustScaler()

# 데이터를 스케일링합니다. fit_transform 메소드를 사용하면 됩니다.
# 선택된 특성만 스케일링
data[features_to_scale] = scaler.fit_transform(data[features_to_scale])

# 스케일링된 데이터를 새 CSV 파일로 저장합니다.
data.to_csv(f"{name}_scaled_data.csv", index=False)
