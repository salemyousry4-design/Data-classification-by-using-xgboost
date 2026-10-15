import pandas as pd
import streamlit as st
from xgboost import XGBClassifier

# Page configuration
st.set_page_config(
    page_title="Breast Cancer Prediction App", page_icon="🎗️", layout="wide"
)

st.title("🎗️ Breast Cancer Prediction App")
st.write(
    "This application predicts whether a tumor is benign or malignant based on"
    " cell characteristics using an XGBoost model."
)

# Load dataset and train the model directly
dataset = pd.read_csv("Data.csv")
dataset["Class"] = dataset["Class"].map({2: 0, 4: 1})

X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

classifier = XGBClassifier()
classifier.fit(X, y)

# Sidebar layout for user input
st.sidebar.header("User Input Parameters")


def user_input_features():
  clump = st.sidebar.slider("Clump Thickness", 1, 10, 5)
  uni_size = st.sidebar.slider("Uniformity of Cell Size", 1, 10, 5)
  uni_shape = st.sidebar.slider("Uniformity of Cell Shape", 1, 10, 5)
  marginal_adh = st.sidebar.slider("Marginal Adhesion", 1, 10, 5)
  single_epithelial = st.sidebar.slider("Single Epithelial Cell Size", 1, 10, 5)
  bare_nuclei = st.sidebar.slider("Bare Nuclei", 1, 10, 5)
  bland_chromatin = st.sidebar.slider("Bland Chromatin", 1, 10, 5)
  normal_nucleoli = st.sidebar.slider("Normal Nucleoli", 1, 10, 5)
  mitoses = st.sidebar.slider("Mitoses", 1, 10, 1)

  data = {
      "Clump Thickness": clump,
      "Uniformity of Cell Size": uni_size,
      "Uniformity of Cell Shape": uni_shape,
      "Marginal Adhesion": marginal_adh,
      "Single Epithelial Cell Size": single_epithelial,
      "Bare Nuclei": bare_nuclei,
      "Bland Chromatin": bland_chromatin,
      "Normal Nucleoli": normal_nucleoli,
      "Mitoses": mitoses,
  }
  features = pd.DataFrame(data, index=[0])
  return features


df_input = user_input_features()

# Display current user inputs
st.subheader("Current Input Values:")
st.dataframe(df_input)

# Prediction button and result display
if st.button("Predict", type="primary"):
  prediction = classifier.predict(df_input)
  prediction_proba = classifier.predict_proba(df_input)

  st.subheader("Prediction Results:")
  if prediction[0] == 1:
    st.error(
        "⚠️ Warning: The predicted result is **Malignant**. Please consult a"
        " doctor."
    )
  else:
    st.success("✅ The predicted result is **Benign**.")

  st.write(
      f"Prediction Confidence:"
      f" **{prediction_proba[0][prediction[0]]*100:.2f}%**"
  )
