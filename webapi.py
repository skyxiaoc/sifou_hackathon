# coding:utf-8
from flask import Flask
from flask import jsonify
from flask import request
from seq2seq import Seq2Seq
import tensorflow as tf
import os,random,json
from seq2seq import Seq2Seq
from utils import pad_data,len_check
from args_helper import args
from datetime import datetime
from bert import modeling

app = Flask(__name__)

@app.route('/',methods=["POST"])
def index():
    question = request.form.get("question")
    if question == '':
        return jsonify({"code": 0, "message": "问题为空"})

    text = question

    inputs = ['[CLS]'] + list(text) + ['[SEP]']
    #inputs =  list(text)
    inputs_ids = model.tokenizer.convert_tokens_to_ids(inputs)
    segment_ids = [0] * len(inputs_ids)
    input_mask = [1] * len(inputs_ids)

    predicted2 = sess.run(model.predicting_ids, feed_dict={
        model.input_ids: [inputs_ids],
        model.input_mask: [input_mask],
        model.segment_ids: [segment_ids],
        model.dropout: 1.0
    })
    answer = ''.join([rev_dictionary_output[n] for n in predicted2[0] if n not in [0]])
    print(answer)
    return jsonify({"code": 1, "message": answer})

"""
app.run()实现了flask程序在开发环境下运行起来,并且默认ip和端口是127.0.0.1:5000
"""
if __name__ == '__main__':
    model = Seq2Seq(256,
                    2,
                    0.001,
                    'chinese_L-12_H-768_A-12/vocab.txt',
                    'chinese_L-12_H-768_A-12/bert_config.json',
                    False,
                    )
    dictionary_output, rev_dictionary_output = model.tokenizer.vocab, model.tokenizer.inv_vocab
    dictionary_input, rev_dictionary_input = model.tokenizer.vocab, model.tokenizer.inv_vocab
    sess = tf.Session()
    tf.device("/cpu:0")
    ckpt = tf.train.get_checkpoint_state('result')
    if ckpt and tf.train.checkpoint_exists(ckpt.model_checkpoint_path):
        tf.logging.info("restore model from patch: %s", ckpt.model_checkpoint_path)  # 加载预训练模型
        saver = tf.train.Saver(max_to_keep=4)
        saver.restore(sess, ckpt.model_checkpoint_path)
    else:
        tf.logging.error("model path wrong !!")

    app.run()

