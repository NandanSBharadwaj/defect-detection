# YOLOv5 Weld Defect Detection - Setup and Training Script (Instructions as comments)

# Step 1: Install Anaconda and required packages
# Open Anaconda Prompt and run:
pip install labelimg

# Step 2: Label images using LabelImg GUI
labelimg
# Use the GUI to label defects: spatter, gap, misalignment

# Step 3: Organize dataset folders
# Create 'images/' and 'labels/' folders
# Within each, create 'train/' and 'val/' subfolders (80% train, 20% val)

# Step 4: Create YAML config file for dataset
# Save the following as 'dataset.yaml':
train: path/to/train
val: path/to/val
nc: 3
names: ["spatter", "gap", "misalignment"]

# Step 5: Install YOLOv5 and dependencies
pip install ultralytics
# Clone YOLOv5 repo from Ultralytics and install requirements:
# git clone https://github.com/ultralytics/yolov5
# cd yolov5
pip install -r requirements.txt

# Step 6: Train the YOLOv5 model
!python train.py --img 415 --batch 4 --epochs 100 --data dataset.yaml --weights yolov5.pt --cache

# Step 7: Run inference (prediction)
!python detect.py --source "image_path" --weights "trained_model_path" --conf 0.25

# Output is stored in: runs/detect/exp
