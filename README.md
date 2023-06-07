<BR># Trans-Onnx - Status: Alpha, requires coding assistance.
<BR>A WSL Python based, Transformers to Onnx converter.
<BR>
<BR>The program consists of three scripts: "merge.py," "convert.py," and "run.bat," along with a "settings.json" file. The purpose of the program is to merge and convert model files to the ONNX format for machine learning tasks.
<BR>
<BR>The "run.bat" script serves as the entry point for executing the program. It sets the input and output directories, checks the workspace folder, and ensures the model and output directories exist. It allows the user to select a model from the input directory and updates the "settings.json" file accordingly. Then, it executes the "merge.py" and "convert.py" scripts using WSL (Windows Subsystem for Linux).
<BR>
<BR>The "merge.py" script merges multiple model files into a single file. It loads the settings from "settings.json" and calculates the number of threads for merging. It collects the model files from the specified directory, merges them using a progress bar, and saves the merged file in the "./workspace" directory.
<BR>
<BR>The "convert.py" script converts the model to the ONNX format. It loads the settings from "settings.json," calculates the number of threads for conversion, and initializes the model and tokenizer. It creates the output directory and converts the model using the specified number of threads and a progress bar. The converted model is saved in the output directory.
<BR>
<BR>The "settings.json" file stores configuration parameters such as the model directory, the first binary file, and the maximum position embeddings.
<BR>
<BR>Overall, the program automates the process of merging and converting model files, providing a convenient way to prepare models for machine learning tasks.
