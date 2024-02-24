Detecting COVID-19 with Chest X-Rays using PyTorch

This project implements a chest X-ray image classification model to detect COVID-19, normal, and viral pneumonia using PyTorch. The model is trained on the COVID-19 Radiography Database, a large dataset of chest X-ray images.

Tools and Libraries:

PyTorch: Deep learning framework used for building and training the neural network.
Torchvision: Provides pre-trained models, datasets, and image transformations for computer vision tasks.
NumPy: Numerical computing library for array manipulation and calculations.
Matplotlib: Visualization library for plotting images and training progress.
Pillow (PIL Fork): Image processing library for reading, resizing, and converting images.
Random: Module for generating random numbers for data augmentation.
shutil: File system manipulation module for creating directories and moving files.
torchutils: Utilities for data loading and management.
Steps:

Data Preparation:

Download the COVID-19 Radiography Database from Kaggle.
Organize the dataset into folders for training, validation, and test sets.
Preprocess the images by resizing, applying random horizontal flips, converting to tensors, and normalizing the pixel values.
Create custom ChestXRayDataset and DataLoader classes for efficient data handling.

Model Design:
Use a pre-trained ResNet18 model from torchvision as the base architecture.
Freeze the convolutional layers (optional) to prevent overfitting.
Replace the final fully-connected layer with a new layer with 3 output neurons corresponding to the three classes.

Training:
Define a loss_fn (CrossEntropyLoss) and optimizer (Adam) for calculating the loss and updating model weights.
Implement a train function to iterate through training epochs, calculate loss, update weights, and evaluate performance on the validation set.
Train the model until a stopping criterion (e.g., accuracy threshold) is met.

Evaluation:
Use a separate test set to assess the model's generalization performance.
Calculate accuracy, precision, recall, and other relevant metrics.
Visualize predictions using show_images function to identify potential errors or biases.
