# 💬 Vietnamese Sentiment Classifier Web App

A beautiful and simple Streamlit web app for classifying Vietnamese text into **Positive**, **Neutral**, or **Negative** sentiments using a fine-tuned **PhoBERT** model.
Built with ❤️ for NLP in Vietnamese!
![demo](/demo.png)

---

## 📌 Table of Contents

1. [✨ Project Overview](#-project-overview)  
2. [🚀 Features](#-features)  
3. [🗂️ Project Structure](#-project-structure)
4. [🧰 Tech Stack](#-tech-stack)
5. [⚙️ Installation](#-installation)  
6. [✅ Example Output](#-example-output)  
7. [🧠 How Confidence is Calculated](#-how-confidence-is-calculated)  
8. [📄 License](#-license)
9. [🤝 Contributing](#-contributing)
10. [📬 Contact](#-contact)

---

## ✨ Project Overview

This project is a Vietnamese Sentiment Classifier that allows users to:
- Input Vietnamese text (sentence or paragraph)
- Classify the emotional tone: **Positive**, **Neutral**, or **Negative**
- Display the result clearly with confidence score
- Run completely offline using pre-trained Transformer models from Hugging Face
---

## 🚀 Features

- Vietnamese language support
- Clean, responsive Streamlit UI
- Powered by `wonrax/phobert-base-vietnamese-sentiment`
- Accurate sentiment classification with confidence
- Fast and easy to use

---
## 🗂️ Project Structure
```
├── __pyache__/
├── streamlit_app.py            # Main UI app
├── model_loader.py             # Load PhoBERT model + tokenizer
├── classify.py                 # Handle inference and softmax confidence
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

```
---

## 🧰 Tech Stack

| Feature                | Tool/Library                                       |
|------------------------|----------------------------------------------------|
| UI                     | Streamlit                                          |
| NLP Model              | `wonrax/phobert-base-vietnamese-sentiment`         |
| Transformer            | Hugging Face Transformers                          |
| Backend Logic          | PyTorch                                            |


---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/vietnamese-sentiment-classifier.git
cd vietnamese-sentiment-classifier
pip install -r requirements.txt
streamlit run streamlit_app.py
```
---
## ✅ Example Output
- ✍️ Input: "Tôi không thích sản phẩm này"
- ✅ Output: 😠 Tiêu cực (Độ tin cậy: 98.81%)

--- 
## 🧠 How Confidence is Calculated
The model returns logits (raw prediction scores). To convert these to human-readable probabilities, we use the Softmax function:


```bash
from torch.nn.functional import softmax

probs = softmax(logits, dim=1)
confidence = probs[0][predicted_class]

```
This gives us a value from `0 → 1`, representing the **model’s certainty** for the predicted label.
We multiply by `100` and round for UI display.

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

--- 
## 🤝 Contributing
Feel free to:
- Submit PRs with enhancements
- Report bugs or issues
- Suggest new features (e.g., more labels, LLM integration)

--- 

## 📬 Contact
Contact for work: **Nguyễn Công Phát** – congphatnguyen.work@gmail.com
