
## LongSumm Training and Inference

Huaipeng Zhao's Implementation of SummaRuNNer is available [here](https://github.com/hpzhao/SummaRuNNer).

Pretrained Glove embeddings can be found [here](https://drive.google.com/file/d/10cizSzQq9-jsyS88KgtuTu3volGc0DKN/view?usp=sharing).

- Training 
    - Training from scratch
        ```bash
        python main.py -device 0 -batch_size 32 -model CNN_RNN -seed 1 -save_dir checkpoints/model.pt
        ```
    - Retraining an existing checkpoint
        ```bash
        python main.py -device 0 -batch_size 32 -seed 1 -save_dir checkpoints/model_updated.pt -load_dir checkpoints/model.pt
        ```

- Inference
    ```bash
    python main.py -batch_size 1 -device 0 -predict -load_dir checkpoints/model.pt -foldername PATH_TO_GENERATED_SUMMARIES_FOLDER    
    ```
	Structure of the Directory with Generated Summaries should of the form:
  
	```
	├── Directory with Generated Summaries
	│   ├── Document1
	│   │   ├── Section1.txt
	│   │   ├── Section2.txt
	│   │   ├── Section3.txt
	│   │   ├── Section4.txt
	│   ├── Document2
	│   │   ├── Section1.txt
	│   │   ├── Section2.txt
	│   │   ├── Section3.txt
	│   │   ├── Section4.txt
	...
	```
	
	---
