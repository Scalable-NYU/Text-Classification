# Text Classification on Tensorflow

Modified upon https://github.com/dennybritz/cnn-text-classification-tf

## Train:  

- Revise data_helpers.py  
- Revise train.py Data Loading params.
```bash
python train.py
```


# Evaluataion:

Set input_data_file inside eval_server.py

```bash
python eval.py --eval_train --checkpoint_dir="./runs/1525708583/checkpoints/"

```