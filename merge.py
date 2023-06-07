# script = merge.py

import os
import json
import torch
from tqdm import tqdm
import gc
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

# Remove files from memory
def remove_files_from_memory(file):
    print("Removing files from memory...")
    try:
        if isinstance(file, dict):
            for key in list(file.keys()):
                del file[key]
        del file
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    except Exception as e:
        print(f"Error while removing files from memory: {str(e)}")

# Merge model files
def merge_model_files(model_dir, num_threads):
    print("Merging model files...")
    files = os.listdir(model_dir)
    merged_model = {}
    for file in tqdm(files):
        if file.endswith('.bin'):
            file_path = os.path.join(model_dir, file)
            model_part = torch.load(file_path, map_location=torch.device('cpu'))
            merged_model.update(model_part)
            remove_files_from_memory(model_part)

    merged_model_path = os.path.join(model_dir, settings['merged_model_filename'])
    torch.save(merged_model, merged_model_path)
    print(f"Merged model saved at: {merged_model_path}")

# Main function
def main():
    model_dir = settings['selected_model_dir']
    percentage = settings['memory_percentage']
    num_threads = calculate_threads(percentage)
    merge_model_files(model_dir, num_threads)

# Execute the main function
if __name__ == '__main__':
    main()
