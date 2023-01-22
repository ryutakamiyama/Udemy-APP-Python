#  command + / でコメントアウト＆解除が可能

import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image #この3つのライブラリは今使ってないのでコメントアウト
import time

st.title("Streamlit 超入門")
st.write("プログレスバーの表示")

"START!!"

latest_interation = st.empty() #空（から）を追加する
bar = st.progress(0)

for i in range(100) : 
    latest_interation.text(f"Iteration {i + 1}") #f文 
    bar.progress(i + 1) #プログレスバーを表示する（この場合はiに1をfor構文の数だけ足していく）
    time.sleep(0.1) #0.1秒ごとに追加されるのを意味する。

"DONE!!"


#【インタラクティブなWidgetシリーズ】
#【レイアウトを整える】

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示") #.buttonでボタンを配置する
if button : #ボタンが押されたら(True)
    right_column.write("ここは右カラムです。")

expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ1の内容を書く")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ2の内容を書く")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ3の内容を書く")


# text = st.text_input(
#     "あなたの好きな趣味を教えてください")
# "あなたの趣味：", text

# condition = st.slider("あなたの今の調子は？", 0, 100, 50) #(最低値, 最大値, デフォルトの値)
# "あなたの　コンディション：", condition

# text = st.sidebar.text_input(
#     "あなたの好きな趣味を教えてください")
#     #sidebarを入れることで位置をサイドに変更できる

# "あなたの趣味：", text

# condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50) #(最低値, 最大値, デフォルトの値)
# "あなたの　コンディション：", condition

# option = st.selectbox(
#     "あなたが好きな数字を教えてください", 
#     list(range(1,11))
# )
# "あなたの好きな数字は", option,  "です。"

#【Streamlitの基本的な使い方シリーズ】
# if st.checkbox("Show Image") :
#     image = Image.open("/Users/rkamiyama/Desktop/スクリーンショット 2021-09-30 12.37.38.png")
#     st.image(image, caption = "Kamiyama's TOIEC",use_column_width = True)
    # use_column_width = True で実際の画面の幅に合わせて画像を表示してくれる。
#check boxにチェックが入ることをTrue、入っていないのをfalaseで返すので、if文にするとチェックを入れると表示される

#df = pd.DataFrame(
#    np.random.rand(20, 3),#縦に20行、横に３列のテーブルを作成するという意
#    columns= ["a", "b", "c"]
#)

#df =pd.DataFrame(
#    np.random.rand(100, 2)/[50,50] + [35.69, 139.70], 
#    columns= ["lat", "lon"] 
#)
    #map用にするために、数字を小さくするために割り算している（数字は任意）。足しているのは新宿付近の座標数値
    #lattitude & lontitude(緯度と軽度)

#st.map(df)

#st.line_chart(df)
    #折れ線グラフを挿入する。
#st.area_chart(df)
    #エリアチャートを挿入する。

# st.dataframe(df.style.highlight_max(axis=0))
    #writeでもデータフレームの表現は可能だが、幅や高さの指定ができない
    #行を指定するときはaxis = 1 を指定

# st.table(df.style.highlight_max(axis=0))

    #静的なデータテーブルを見たい場合はTableを使用する

    #下は参考（文字の大きさとバックコロンによるテキスト表示）

#"""
# 章
## 節
### 項

# ```Python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

#"""


