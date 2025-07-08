
# 🎯 Cross-Camera Player Mapping

A computer-vision system that maps the same player across multiple camera views using detection, tracking, and deep feature-based re-identification.



## 📌 Features

• Player detection with YOLOv5  
• Player tracking with DeepSort  
• Feature embedding via ResNet  
• Cross-camera matching using cosine similarity  
• Easily customizable for sports analytics

## 📂 Project Structure

Cross-Camera-Player_Mapping/
├── cam_1/                # Camera 1 input frames  
├── cam_2/                # Camera 2 input frames  
├── weights/              # YOLOv5 & ResNet pretrained models  
├── detection.py          # Player detection logic  
├── tracker.py            # Tracking logic (DeepSort)  
├── feature_extraction.py # Deep feature embedding  
├── similarity.py         # Cosine similarity calculations  
├── test.py               # Main pipeline execution  
└── requirements.txt      # Python dependencies

## ⚙️ Installation

# 1. Clone the repository
git clone https://github.com/pranjalshrivastavaa/Cross-Camera-Player_Mapping.git
cd Cross-Camera-Player_Mapping

# 2. Install Python packages (Python 3.8+ required)
pip install -r requirements.txt

## 🚀 How to Run

# Run the main pipeline
python test.py

# Make sure:
- Input frames are inside cam_1/ and cam_2/
 - Model weights are available in weights/

## 📊 How It Works

1. Detect players using YOLOv5 in both camera views  
2. Track them over time using DeepSort  
3. Extract feature embeddings with ResNet  
4. Match players using cosine similarity  
5. Visualize results across cameras

## 🧠 Models Used

• YOLOv5 — Player detection  
• DeepSort — Multi-object tracking  
• ResNet — Deep feature extraction  
• Cosine Similarity — Player matching

## 📄 License

Licensed under the MIT License

## 🙋 Author

Pranjal Shrivastava  
GitHub: https://github.com/pranjalshrivastavaa

Feel free to contribute or open an issue!
```
