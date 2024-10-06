# Voice Biometry Project

This project is focused on **voice biometrics** for **Kazakh speakers**, utilizing a **Convolutional Neural Network (CNN)** to classify speakers based on their voice features. The project is implemented in **Python**, with **Jupyter Notebook** used as the primary environment for code execution.

## Project Overview

- **Voice Feature Extraction**: The project extracts **Mel Frequency Cepstral Coefficients (MFCC)** from voice recordings as input features.
- **CNN Model**: A **Convolutional Neural Network (CNN)** model is employed for speaker classification based on the extracted MFCCs. Below is a visual representation of the CNN model used.

![CNN Model Photo](/Soileushi_model_CNN.keras.png)

## Dataset Information

- The training and testing dataset consists of:
  - **16 speakers**.
  - Each speaker has **12 audio files**.
  - The audio duration is approximately **1 second** per file.
  - The audio format is **WAV** with a sampling rate of **48 kHz**.
  
### Data Availability

The dataset used in this project is not publicly available. If you wish to replicate or extend this research and need access to the dataset, please contact me at **trrkhfz@gmail.com**. In your message, kindly explain:
- The reason for your interest in the dataset.
- How you intend to use it.

## Dependencies

To run this project, the required Python packages are listed in the `requirements.txt` file. Please ensure you have the necessary libraries installed by running:

```bash
pip install -r requirements.txt
```

**Notice:** if you can't install tensorflow 2.14.0, try to use older Python versions.

## Running the Project

1. Clone the repository.
2. Install the required packages using the `requirements.txt`.
3. Open the Jupyter Notebook and run the code to perform training and testing on the provided data.

## Citation

If you use this code in your research, please cite it as follows:

Khafiz T., "VoiceBiometrics" Zenodo, DOI: [[https://doi.org/10.5281/zenodo.13896129](https://doi.org/10.5281/zenodo.13896129)], 2024.


## Contact

For any questions or if you need access to the dataset, you can contact me via email at **trrkhfz@gmail.com**. Please explain your reason for contacting and how you plan to use the dataset.
