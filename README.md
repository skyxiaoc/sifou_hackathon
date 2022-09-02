
# tf-bert-seq2seq

通过 `tensorflow bert seq2seq` 实现QA问答系统

## 依赖

    python >= 3.6
    tensorflow 1.14.0
    bert


## 下载bert预训练模型

    $ wget -c https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip
    $ unzip chinese_L-12_H-768_A-12.zip 
    

## 下载bert源代码
下载 [**bert**](https://github.com/google-research/bert) 放入项目目录**bert**下，

    $ git clone https://github.com/google-research/bert.git
    
## 数据样例

{"question": "孩子3岁的标准体重是多少", "answer": " 想要知道孩子的标准体重可以使用小程序内标准体重应用"}
{"question": "孩子老不吃饭怎么办", "answer": "多半是装的，打一顿就好了"}


## 运行

### 训练

    $ python3 model.py --task=train \
        --is_training=True \
        --epoch=100 \
        --size_layer=256 \
        --bert_config=chinese_L-12_H-768_A-12/bert_config.json \
        --vocab_file=chinese_L-12_H-768_A-12/vocab.txt \
        --num_layers=2 \
        --learning_rate=0.001 \
        --batch_size=16 \
        --checkpoint_dir=result





![](media/15744775485612.jpg)

### 预测

    $ python3 model.py --task=predict \
        --is_training=False \
        --epoch=100 \
        --size_layer=256 \
        --bert_config=chinese_L-12_H-768_A-12/bert_config.json \
        --vocab_file=chinese_L-12_H-768_A-12/vocab.txt \
        --num_layers=2 \
        --learning_rate=0.001 \
        --batch_size=16 \
        --checkpoint_dir=result


**Just For Fun!!**

