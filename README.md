<BR># Trans-Onnx  
<BR>To merge and convert, model files to the ONNX format for machine learning tasks, through use of, Windows Batch & WSL Python.
<BR>
<BR>Status: Alpha, requires coding assistance, mostly created project for someone to fork and develop a little further to complete with some know how. Will be of interest to someone wishing to automate the process of converting large number of linux friendly transformers based language models to windows friendly onnx based models, for use on windows based language model applications. 
<BR>The program is the result of 5 mostly long sessions of GPT4 with Link Reader plugin, and consists of three scripts: "merge.py," "convert.py," and "run.bat," along with a "settings.json" file. 
<BR>
<BR>The program has been reinvented from a pure python version of the application I made, however, I discovered that python does not release the memory from the merging process, even after implementing all the garbage removal code I could, it still would not release the memory after merging, so, best to run the scripts seperately through a batch. Additionally, WSL and Powershell, commands are used.  
<BR>
<BR>The "run.bat" script serves as the entry point for executing the program. It sets the input and output directories, checks the workspace folder, and ensures the model and output directories exist. It allows the user to select a model from the input directory and updates the "settings.json" file accordingly. Then, it executes the "merge.py" and "convert.py" scripts using WSL (Windows Subsystem for Linux).
<BR>
<BR>The "merge.py" script merges multiple "*.bin" files found in the typical transformers libraries into a single file. It loads the settings from "settings.json" and calculates the number of threads for merging. It collects the model files from the specified directory, merges them using a progress bar, and saves the merged file in the "./workspace" directory.
<BR>
<BR>The "convert.py" script converts the model to the ONNX format. It loads the settings from "settings.json," calculates the number of threads for conversion, and initializes the model and tokenizer. It creates the output directory and converts the model using the specified number of threads and a progress bar. The converted model is saved in the output directory.
<BR>
<BR>The "settings.json" file stores configuration parameters such as the model directory, the first binary file, and the maximum position embeddings.
<BR>
<BR>Overall, the program automates the process of merging and converting model files, providing a convenient way to prepare models for machine learning tasks.
<BR>
<BR>Assistance required:
<BR>GPT4 or GPT4+Web, may be able to fix it with the correct prompt, or otherwise programmer may be able to see whats wrong, create fork, the push fixed code to me.
<BR>Program is currently unable..
<BR>1) To copy the name of the selected folder to "model_dir" in "settings.json". 
<BR>2) To find the first "*.bin" file in the selected model folder and input its name into "first_bin_file" in the "settings.json" 
<BR>3) To copy the values for "max_sequence_length" from the "config.json" in the selected model folder to the "max_position_embeddings" in the "settings.json".
<BR>However the rest of the program is mostly researched and present.
