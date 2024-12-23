# YOLOv-MRZ Project

## Overview

This project aims to utilize the YOLO (You Only Look Once) model for detecting and segmenting Machine Readable Zones (MRZ) on identity documents. The project provides utilities for training, predicting, and processing images using pretrained and custom-trained YOLO models.

## Project Structure

- `notebooks/`
  - `yolov_mrz_train.ipynb`: Jupyter notebook for training the YOLO model on MRZ data, including prediction and segmentation tasks.
  - `ipynb_utils.py`: Utility functions for Jupyter notebooks, such as finding the project root.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd yolov_mrz
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training

To train the YOLO model on your MRZ dataset, open and run all cells in `notebooks/yolov_mrz_train.ipynb`. Ensure you have configured the `mrz_train_config.yml` with the correct dataset paths and parameters.

### Prediction

Use the trained model to predict MRZs in your images. Load the model and run the prediction cells in `yolov_mrz_train.ipynb`.

### Segmentation

Segmentation tasks can be performed using the segmentation model loaded in the notebook. Follow the instructions in the `Segmentation` section of the notebook to process images.

## Utilities

- `cwd_to_root`: Sets the current working directory to the project root, helping with relative paths.
- `crop_bbox`: Crops the bounding box from an image using the prediction results.
- `auto_rotate`: Automatically corrects image skew by rotating it to the best angle based on given limits.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.


