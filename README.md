# defect-detection
Detection and Identification of Welding Defects Through Deep Learning Models
# 🛠️ Weld Defect Detection using YOLOv5 and YOLOv8

This project implements deep learning-based detection of weld defects using the YOLO (You Only Look Once) object detection models.

## 📄 Overview
We trained YOLOv5 and YOLOv8 on a custom dataset of welded metal parts labeled with three defect classes:
- **Spatter**
- **Gap**
- **Misalignment**

## 🧠 Technical Details
- Annotated using **LabelImg**, organized into `train/` and `val/` datasets (80/20 split)
- Training conducted with **Ultralytics** frameworks
- Configured using `data.yaml` with class definitions and paths
- Training parameters include customizable **epochs**, **batch sizes**, and **image resolutions**
- Supports **GPU-accelerated training** via PyTorch

## 🧪 Inference
You can test the trained model on new images with confidence score visualization using:
```bash
yolo task=detect mode=predict model=yolov8m_custom.pt show=True conf=0.5 source="your_image.jpg"
