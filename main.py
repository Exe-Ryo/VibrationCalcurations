import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

def page1():
  st.title("加振_入力振動比較")
  path1 = st.text_input("CSVファイルパスを入力 Part1", "//tec-hls08/モータ評価/★PJT開発(Name_YYMM_内容)/土井_2205_966K_OTS_ランダム加振/02_試験データ/03_データ・解析（MG1_動力線あり）/Output/【左右】1G[[10~2000]]_Power.csv")
  path2 = st.text_input("CSVファイルパスを入力 Part1", "//tec-hls08/モータ評価/★PJT開発(Name_YYMM_内容)/土井_2205_966K_OTS_ランダム加振/02_試験データ/04_データ・解析（MG1_動力線なし）/Output/【左右】1G[[10~2000]]_Power.csv")
  
  if st.button("CSVファイルを読み込み"):
    if os.path.isfile(path1) and os.path.isfile(path2):
      df1 = pd.read_csv(path1)
      df2 = pd.read_csv(path2)
      name1 = os.path.basename(path1)
      name2 = os.path.basename(path2)
      
      col1,col2 = st.columns(2)
      # 水平方向に2分割した画面にそれぞれデータフレームを表示
      col1.write(name1)
      col2.write(name2)
      col1.dataframe(df1, width = None, height = 100)
      col2.dataframe(df2, width = None, height = 100)
      
      col = min(len(df1.columns),len(df2.columns))
      
      tabs = st.tabs(list(df1.columns[1:]))
      
      x = df1.iloc[:,0]
      
      for i in range(col - 1):
        print(tabs[i])
        with tabs[i]:
          y1 = df1.iloc[:,i + 1]
          y2 = df2.iloc[:,i + 1]
          
          fig, ax = plt.subplot(figsize = (5, 2))
          plt.title("Ch" + str(i + 1) + " 比較" , fontname = "MS Gothic")
          
          ax.plot(x, y1, x, y2)
          ax.set_xlim(0, 2500, 250)
          ax.set_ylim(0, 25, 5)
          
          # 補助目盛を表示
          ax.minorticks_on()
          ax.grid(which="major", color="black", alpha=0.5)
          ax.grid(which="minor", color="gray", linestyle=":")
          
          ax.legend([name1,name2], prop={"family":"MS Gothic"})
      else:
        st.write("CSV Read Error!")    
    else:
      st.write("None item")

def page2():
  st.title("開発中・・・ 加振_制御グラフ描画")

def page3():
  st.title("開発中・・・ 加振_クロストーク描画")

def page4():
  st.title("開発中・・・ そのほか")

pages = dict(
  page1 = "加振_入力振動比較",
  page2 = "加振_制御グラフ描画",
  page3 = "加振_クロストーク描画",
  page4 = "加振_そのほか"
)

page_id = st.sidebar.radio( # st.sidebar.*でサイドバーに表示する
  "起動する機能", 
  ["page1","page2","page3","page4"], 
  format_func = lambda page_id: pages[page_id], # 描画する項目を日本語に変換
)

if page_id == "page1":
  page1()

if page_id == "page2":
  page2()
  
if page_id == "page3":
  page3()

if page_id == "page4":
  page4()
