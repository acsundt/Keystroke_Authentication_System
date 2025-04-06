# Keystroke Dynamics Authentication System

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

