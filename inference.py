import gpt_2_simple as gpt2
import os
import pandas as pd
import tensorflow as tf
from datetime import datetime

def generate_lyrics(prefix_lines):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,run_name='run1')
    gen_txt = gpt2.generate(sess,temperature=0.7,return_as_list=True,prefix=prefix_lines,truncate="<|endoftext|>")
    return gen_txt[0]
