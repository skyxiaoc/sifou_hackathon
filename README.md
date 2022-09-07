
# tf-bert-seq2seq

基于tf-bert-seq2seq实现老人（NLP）意图识别的“宝宝发育咨询抖音小程序”

## 解决的“垂类场景实际问题”：
    1）无法大量及时回复老人发育咨询
    2）一般关键词回复类解决方案对于老人输入能造成的“意图识别”
 
    线上应用：
        抖音短视频、直播、评论区挂载；
        二维码海报转发老年群微信；
        线下应用：
        全国各地的婴幼儿疫苗体检中心
        社区医院扫码

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
## 部署方式
模型通过flask框架共享预测接口，前端通过api方式（post）进行预测。

