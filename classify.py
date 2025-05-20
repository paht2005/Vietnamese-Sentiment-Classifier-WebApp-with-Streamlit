# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import torch
from torch.nn.functional import softmax

def classify_text(text, tokenizer, model):
    if not text.strip():
        return "⚠️ Vui lòng nhập văn bản."

    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = softmax(outputs.logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
        confidence = round(probs[0][pred].item() * 100, 2)

    label_map = {0: "😠 Tiêu cực", 1: "😐 Trung lập", 2: "😄 Tích cực"}
    return f"📌 Kết quả: {label_map[pred]} (Độ tin cậy: {confidence}%)"
