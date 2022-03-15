import streamlit as st
import pandas as pd
from tgod import get_map  
gdf = get_map.get_boundary('county')
st.dataframe(gdf.head())

data = pd.read_csv('data.csv', encoding='big5') 
# st.markdown(data.iloc[0].values)
data.drop([0], axis=0, inplace=True)

columns = {

}

# data.rename()
st.dataframe(data.head())
# st.markdown(data.columns.tolist())
st.markdown(data['COUNTY'].value_counts().index)

name = [
    '縣市代碼',
    '縣市名稱',
    '鄉鎮市區代碼',
    '鄉鎮市區名稱',
    '平日夜間停留人數',
    '平日上午活動人數',
    '平日下午活動人數',
    '平日日間活動人數',
    '假日夜間停留人數',
    '假日上午活動人數',
    '假日下午活動人數',
    '假日日間活動人數',
    '平日早晨旅次',
    '平日中午旅次',
    '平日午後旅次',
    '平日晚上旅次',
    '假日早晨旅次',
    '假日中午旅次',
    '假日午後旅次',
    '假日晚上旅次',
    '資料時間'
]

col_names= [
    'COUNTY_ID', 
    'COUNTY', 
    'TOWN_ID', 
    'TOWN', 
    'NIGHT_WORK', 
    'DAY_WORK(7:0013:00)', 
    'DAY_WORK(13:0019:00)', 
    'DAY_WORK', 
    'NIGHT_WEEKEND', 
    'DAY_WEEKEND(7:0013:00)', 
    'DAY_WEEKEND(13:0019:00)', 
    'DAY_WEEKEND', 
    'MORNING_WORK', 
    'MIDDAY_WORK', 
    'AFTERNOON_WORK', 
    'EVENING_WORK', 
    'MORNING_WEEKEND', 
    'MIDDAY_WEEKEND', 
    'AFTERNOON_WEEKEND', 
    'EVENING_WEEKEND', 
    'INFO_TIME'
]