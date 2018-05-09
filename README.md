# Text Classification on Tensorflow

## Train:  

- Revise data_helpers.py  
- Revise train.py Data Loading params.
```bash
python train.py
```

## Evaluataion:

Set input_data_file inside eval_server.py

Download the most recent trained model from:  
https://drive.google.com/open?id=1RF9yPJF_6WyPM1uiFAQxswaUobONHXq3

```bash
python eval_server.py --checkpoint_dir="./runs/1525708583/checkpoints/" --input_data_file="./data/four_class/class_fou.test"
```

## Class index and label:  
3, World  
2, Sports  
1, Business  
0, Sci/Tech  

## Reference:
- https://github.com/dennybritz/cnn-text-classification-tf
- https://arxiv.org/abs/1408.5882
- Wiki: List of Datasets: https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research

## Further Work:
- Create REST API for TensorFlow models - https://becominghuman.ai/creating-restful-api-to-tensorflow-models-c5c57b692c10
- Try out TensorFlow Serving: https://www.tensorflow.org/serving/
