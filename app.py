
import streamlit as st

st.set_page_config(page_title="白雪薬膳教室＊気血水体質チェック", page_icon="❄️", layout="centered")

st.markdown(
    "<h1 style='color: #d88ca4;'>白雪薬膳教室＊気血水体質チェック</h1>",
    unsafe_allow_html=True
)

# 例として気虚タイプのチェックリスト（25個）
kikyo_questions = [
    "すぐに疲れる", "息切れしやすい", "声が小さい", "風邪をひきやすい", "汗をかきやすい",
    "食欲があまりない", "食後に眠くなる", "お腹が張る", "軟便または下痢気味", "顔色が青白い",
    "手足がだるい", "集中力が続かない", "寒がり", "動くとすぐに疲れる", "倦怠感が強い",
    "立ちくらみしやすい", "気力がない", "無気力になることが多い", "朝がつらい", "元気が出ない",
    "横になると楽になる", "舌の色が淡い", "脈が弱い", "顔に艶がない", "免疫力が弱いと感じる"
]

score = 0
st.subheader("【気虚タイプ】チェック")
for q in kikyo_questions:
    if st.checkbox(q):
        score += 1

if st.button("診断結果を見る"):
    st.subheader("診断結果")
    st.write(f"あなたの気虚スコアは {score} 点です。")
    if score >= 13:
        st.success("あなたは『気虚タイプ』の傾向が強いです。")
        st.write("→ 胃腸をいたわり、やさしい食事を心がけましょう。")
    else:
        st.info("気虚の傾向はそれほど強くありません。")
