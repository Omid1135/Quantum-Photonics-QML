# Quantum-Photonics-QML
This is an educational project on Quantum Machine Learning (QML) applied to photonics. This repository features a Pennylane implementation of a VQC trained to simulate the behavior of a quantum beam splitter, ideal for students and beginners in QML.
**************
QML-Photonics-BeamSplitter-Learning
 Quantum Machine Learning (QML) in Photonics: Training a Beam Splitter
This repository hosts an educational project that demonstrates a fundamental application of Quantum Machine Learning (QML) in the field of quantum photonics. It showcases how a variational quantum circuit (VQC) can be trained to accurately mimic the behavior of a photonic beam splitter using a hybrid quantum-classical optimization approach.

This project was developed as a hands-on teaching example to help students and enthusiasts grasp core QML concepts and their relevance to real-world quantum systems.

 Project Goal
The primary goal of this project is to:

Illustrate the concept of Variational Quantum Circuits (VQCs).
Showcase how classical optimizers can be used to train quantum circuits.
Provide a concrete example of QML applied to a physical system (a photonic beam splitter).
Serve as an accessible educational resource for those beginning their journey in QML and quantum optics.
 What the Project Does
The project consists of a Python script that performs the following steps:

Defines an "Ideal" Quantum Beam Splitter: A simple Pennylane quantum circuit simulates an ideal beam splitter using a single RY (Y-rotation) gate. The rotation angle (theta) controls the splitting ratio of a photon between two paths (represented by qubit states ∣0⟩ and ∣1⟩).
Generates Training Data: Probabilistic outputs from this ideal beam splitter are collected across various theta values to form the training dataset.
Builds a QML Model: A second variational quantum circuit is defined with trainable parameters (weights). This model's goal is to learn the input-output relationship of the ideal beam splitter.
Trains the Model: A classical Gradient Descent optimizer is used to iteratively adjust the model's weights, minimizing a Mean Squared Error (MSE) cost function between the model's predictions and the "real data."
Visualizes Results: After training, the project plots the predicted probabilities from the trained QML model against the ideal beam splitter's probabilities, demonstrating the learning success.
 Getting Started
To run this project on your local machine, follow these steps:

Clone the repository:

Bash

git clone https://github.com/YourGitHubUsername/QML-Photonics-BeamSplitter-Learning.git
cd QML-Photonics-BeamSplitter-Learning
(Remember to replace YourGitHubUsername with your actual GitHub username!)

Create a Conda environment (recommended):

Bash

conda create -n qml-photonics python=3.9
conda activate qml-photonics
Install the necessary dependencies:

Bash

pip install pennylane numpy matplotlib
Run the main script:

Bash

python main_qml_beamsplitter.py
(Assuming your main script is named main_qml_beamsplitter.py. If it's named something else, adjust accordingly.)

 Project Structure
.
├── main_qml_beamsplitter.py # The core Python script containing the QML project
└── README.md              # This file
 Technologies Used
Python
PennyLane: For building and simulating quantum circuits.
NumPy: For numerical operations.
Matplotlib: For plotting results.
 Educational Value & Further Exploration
This example serves as a foundation for understanding:

The hybrid quantum-classical algorithm paradigm.
The role of variational quantum circuits in QML.
Quantum gates (e.g., RY gate) and their physical interpretations.
Basic optimization techniques in the context of quantum computing.
Consider extending this project by:

Experimenting with different optimizers (e.g., Adam, Adagrad).
Adding more parameters or gates to the VQC.
Introducing noise models to simulate a more realistic photonic device.
Exploring more complex photonic components (e.g., phase shifters, Mach-Zehnder interferometers).
 Contributing
Contributions are welcome! If you have suggestions for improvements, new features, or find any issues, please feel free to open an issue or submit a pull request.

 License
This project is open-source and available under the MIT License.
