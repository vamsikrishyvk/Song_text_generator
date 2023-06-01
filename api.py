from flask import Flask,request,jsonify
from inference import generate_lyrics
import gpt_2_simple as gpt2

app = Flask(__name__)

@app.route('/song_generator',methods=['POST'])
def process_request():
    data = request.json
    generated_lyrics = generate_lyrics(str(data['prefix']))
    output = {'output':generated_lyrics}
    return jsonify(output)

if __name__ == '__main__':
    app.run()


