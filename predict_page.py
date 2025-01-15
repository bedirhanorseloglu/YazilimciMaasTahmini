import streamlit as st
import pickle
import numpy as np


# Yazdığımız not defterini(.ipynb) kullanabilmek için yazdığımız fonks
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

dec_tree_reg = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]


def show_predict_page():
    st.title("Yazılım Mühendisi Maaş Tahmini")

    st.write("""### Maaşı tahmin etmek için bazı bilgilere ihtiyacımız var""")

    countries = (
    "Australia",
    "Brazil",
    "Canada",
    "France",
    "Germany",
    "India",
    "Italy",
    "Netherlands",
    "Spain",
    "Ukraine",
    "United Kingdom of Great Britain and Northern Ireland",
    "United States of America",
    )


    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Ülke", countries)   # seçim yapmak için kutucuk
    education = st.selectbox("Eğitim Seviyesi", education) # seçim yapmak için kutucuk

    expericence = st.slider("Deneyim SÜresi", 0, 50, 3) # deneyimi işaretlemek için slider. 0-50 arası ve deafult değeri 3

    ok = st.button("Maaş Hesapla")  # "Maaş Hesapla" butonuna tıkladığında arka planı(SalaryPrediction.ipynb) çalıştır 
    if ok:
        # modele yeni bir girdi ekleyeceğiz:
        X = np.array([[country, education, expericence ]])  # 3 adet sütunumuz vardı "country , education level , YearsCodePro"
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        # girdiye göre en yüksek tahmini aldığımız karar ağaçları ile tahminde bulunacağız
        salary = dec_tree_reg.predict(X)
        st.subheader(f"Tahmini maaş: ${salary[0]:.2f}")
