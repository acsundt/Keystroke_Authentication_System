# Keystroke Authentication System

This project implements a behavioral biometric system using **keystroke dynamics**. It analyzes typing patterns (specifically press/release timing) to distinguish between real users and imposters using a machine learning model.

---

## 📚 Overview

The system collects how users type a password and trains a classifier to verify identity based on typing rhythm. It uses features like dwell time (how long a key is held) and timing between key presses.

---

## 🧠 How It Works

1. **Keystroke Data Collection**
   - User types a password.
   - Press and release timestamps are recorded.
   - Timing features are extracted (e.g., dwell time).

2. **Data Labeling**
   - True user samples are labeled `1`.
   - Imposter (or variation) samples are labeled `0`.

3. **Model Training**
   - A Random Forest Classifier is trained using the labeled data.

4. **Prediction**
   - New keystroke samples are processed and passed to the trained model for prediction.

---

## ❌ Current Limitations

- **Synthetic Data**: The current implementation uses **synthetic data** for training and testing. This means the model is not yet based on actual user input or real-world data. The synthetic data is generated with randomized values, which may not fully represent the performance of the model when working with real user inputs.
  
- **Limited User Sampling**: The system has not yet been fully configured to handle extensive or diverse user sampling. While it supports basic functionality for recording keystrokes, it is not optimized for large-scale user input collection. More work is needed to make it adaptable to varied user behavior, such as handling multiple samples, different typing speeds, or irregular patterns.

---

## 🐍 Dependencies

- Python 3.10+
- `pandas`
- `numpy`
- `scikit-learn`
- `pynput`

Install them with:

```bash
pip install pandas numpy scikit-learn pynput
```
How to run:

```bash
python main.py
```

***Created by Brendan Moore and Aidan Sundt for Loyola University Maryland Hackathon 2025***
