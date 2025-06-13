# YOLOv8 Weld Defect Detection - Setup and Training Script (Instructions as comments)

# Step 1: Install dependencies
pip install labelimg

# Step 2: Label images using LabelImg GUI
# Run in terminal:
labelimg
# Use the GUI to annotate images for spatter, gap, and misalignment

# Step 3: Organize dataset into 'train/' and 'val/' folders
# Move 80% of labeled data to 'train/' and 20% to 'val/'

# Step 4: Create YAML config file for dataset
# Save the following as 'data_custom.yaml':
train: path/to/train
val: path/to/val
nc: 3
names: ["spatter", "gap", "misalignment"]

# Step 5: Install Ultralytics and PyTorch with CUDA support
pip install ultralytics
pip3 install --upgrade torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117

# Step 6: Train the YOLOv8 model
# Run the following command in terminal:
yolo task=detect mode=train epochs=100 data=data_custom.yaml model=yolov8m.pt imgsz=640 batch=4

# Step 7: Run inference on new images
# Replace 'path/to/image' with your test image path
yolo task=detect mode=predict model=yolov8m_custom.pt show=True conf=0.5 source="path/to/image"
