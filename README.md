One needs to run api.py as well as post_api.py , in order to get inference , argparse can be used to pass arguments for inference , can also change / modify the code as well for input , model screenshots of run can be found in gdrive: 
metrics : you can check with N-grams whether its using the words / ngrams from the train data or not , to better justify the generation .

docker command to build image from Dockerfile : docker built -t lyric_gen .
command to run a docker : docker run -d -p 8000:8000 lyric_gen

Pretrained Text generation model can be finetuned with gpt-2-simple also can be done with huggingface .![Screenshot from 2023-06-01 12-32-28](https://github.com/vamsikrishyvk/Song_text_generator/assets/60051414/8fc0644a-4d62-44a4-b986-a52046179662)
![Screenshot from 2023-06-01 12-33-44](https://github.com/vamsikrishyvk/Song_text_generator/assets/60051414/f5949c63-4360-4084-ac9f-6f816b11a1eb)
![Screenshot from 2023-06-01 12-34-47](https://github.com/vamsikrishyvk/Song_text_generator/assets/60051414/06c69d79-d373-4ee8-9a76-619e402a4cba)


![Screenshot from 2023-06-01 12-35-29](https://github.com/vamsikrishyvk/Song_text_generator/assets/60051414/f8153895-6610-49f2-9141-665a5bb7db06)

model checkpoint :
![chkpt_run](https://github.com/vamsikrishyvk/Song_text_generator/assets/60051414/6e3ae29e-5699-424c-ba4a-518c1856ce15)
