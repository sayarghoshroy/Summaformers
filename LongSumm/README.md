## Code for LongSumm part of the Challenge

Download glove embeddings from - [Link](https://drive.google.com/file/d/10cizSzQq9-jsyS88KgtuTu3volGc0DKN/view?usp=sharing)

- For Training 
    - Training from scratch
        ```python
        python main.py -device 0 -batch_size 32 -model CNN_RNN -seed 1 -save_dir checkpoints/model.pt
        ```
    - Retraining an existing checkpoint
        ```python
        python main.py -device 0 -batch_size 32 -seed 1 -save_dir checkpoints/model_updated.pt -load_dir checkpoints/model.pt
        ```

- For Inference
    ```python
    python main.py -batch_size 1 -device 0 -predict -load_dir checkpoints/model.pt -foldername PATH_TO_PREDICT_FOLDER    
    ```