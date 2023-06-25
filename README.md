# Breaking-Lenghty-Audio-File-for-ASR

# Audio Segmentation for Automatic Speech Recognition (ASR)

This repository contains a Python script that demonstrates how to break large audio files into smaller segments for Automatic Speech Recognition (ASR) tasks. The script utilizes the `pydub` library to process audio files and segment them based on a specified segment length.

## Requirements

To run this project, you need the following dependencies:

- Python (version 3.6 or above)
- `pydub` library

## Getting Started

Follow the instructions below to set up and run the project:

1. Clone this repository to your local machine or download the source code as a ZIP file.
2. Ensure that you have the required dependencies installed on your system.
3. Open a terminal or command prompt and navigate to the project directory.

## Usage

The `audio_segmentation.py` file contains the code for segmenting audio files. The script requires you to set the following parameters:

- `segment_length`: The desired length of each segment in milliseconds.
- `audio_folder`: The path to the folder containing the audio files to be segmented.
- `output_folder`: The path to the folder where the segmented audio files will be saved.

Update these parameters in the script according to your requirements. Once you have set the parameters, run the script by executing the following command in your terminal or command prompt:

```shell
python audio_segmentation.py
```

The script will loop through each audio file in the specified `audio_folder` and segment them into smaller audio files of the specified length. The segmented files will be saved in separate folders, with each folder named after the original audio file.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## Acknowledgments

This project was created as a utility tool for breaking audio files into segments for ASR tasks. Thanks to the developers of the `pydub` library for providing a simple and efficient audio processing solution.

If you have any questions or need further assistance, please feel free to contact me.

Happy audio segmentation!
