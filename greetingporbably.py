import streamlit as st

st.title("رادار المشاعر المطور 🌈")

gender = st.radio("هل أنت:", ("ولد", "بنت"))
status = st.selectbox("بماذا تشعر الآن؟", ("سعيد", "حزين", "بردان"))

if st.button("اكتشف شكلك!"):
    if status == "سعيد":
        st.balloons()  # احتفال بالبالونات
        st.success("اكيد شربت/ي شاي بلبن!")
    elif status == "حزين":
        st.info("اشرب/ي شاي بلبن هتكون/ي احسن")
    elif status == "بردان":
                st.info("اشرب/ي هوت شوكلت ")
        st.snow()  # تأثير الثلج السحري
