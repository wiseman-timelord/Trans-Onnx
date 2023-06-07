# script = convert.py

import torch
import json
import os
from transformers import AutoModel, AutoTokenizer
from transformers.convert_graph_to_onnx import convert
from pathlib import Path
from tqdm import tqdm
import multiprocessing
import psutil

# Load settings
with open('settings.json') as f:
    settings = json.load(f)

# Calculate the number of threads
def calculate_threads(percentage):
    print("Calculating threads...")
    total_threads = multiprocessing.cpu_count()
    return total_threads * percentage // 100

# Convert the model to ONNX format
def convert_model(model_dir, output_dir):
    print("Converting model...")
    try:
        # Load the model and tokenizer
        model = AutoModel.from_pretrained(model_dir)
        tokenizer = AutoTokenizer.from_pretrained(model_dir)

        # Create the output directory
        print("Creating output directory...")
        os.makedirs(output_dir, exist_ok=True)

        # Determine the number of threads
        convert_threads = calculate_threads(75)

        # Convert the model with progress bar
        tqdm.get_lock()
        with tqdm(total=100, desc="Converting model",
                  bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}") as pbar:
            convert(framework="pt", model=model, tokenizer=tokenizer, output=Path(output_dir, "model.onnx"),
                    opset=11, use_external_format=True,
                    pipeline_name="fill-mask", num_threads=convert_threads,
                    progress_update=lambda x: pbar.update(x * 100))
            memory = f'{psutil.virtual_memory().used / (1024.0 ** 3):.2f}GB/{psutil.virtual_memory().available / (1024.0 ** 3):.2f}GB'
            pbar.set_postfix_str(f"Memory used/free {memory}", refresh=True)
            print("Model conversion complete..")
    except Exception as e:
        print(f'Failed to convert model: {e}.')

# Main function
def main():
    model_dir = settings['model_dir']
    output_dir = settings['output_dir']
    convert_model(model_dir, output_dir)

# Execute the main function
if __name__ == "__main__":
    main()
