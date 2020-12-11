"""
%tensorflow_version 1.x
!pip install -q gpt-2-simple
"""
import gpt_2_simple as gpt2
from datetime import datetime

gpt2.download_gpt2(model_name="124M")

file_name = "EEG-concentrating.csv" # add your file here

sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              dataset=file_name,
              steps=1000, #update steps as necessary 
              restore_from='latest', # to continue from previous
              run_name='eeg-concentrating-1',
              print_every=1,
              sample_every=100,
              save_every=500,
              overwrite=True
              )

"""
#If using Colab:
gpt2.copy_checkpoint_to_gdrive(run_name='classical-piano-1')
"""

# Generation loop:

gpt2.copy_checkpoint_from_gdrive(run_name='eeg-concentrating-1')
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='eeg-concentrating-1')

#Examples of generation:
print("Generating without previous data as input")
for x in range(1, 10):
  gpt2.generate(sess, run_name='eeg-concentrating-1', length=100)

print("----FINISHED----")
print(" ")

print("Generating with final 50 characters as input")
print("Looks for an END flag, or just keeps running forever if there isn't one. Let this run for as long as you need.")

def remove_last_line_from_string(s):
  return s[:s.rfind('\n')]

prediction = gpt2.generate(sess, run_name='eeg-concentrating-1', return_as_list=True, length=1024)[0]
prediction = remove_last_line_from_string(prediction)
print(prediction)

run = True
while(run):
  end = ("\n".join(prediction.split("\n")[-50:]))
  if "END" in prediction:
    run = False
  prediction = gpt2.generate(sess, run_name='eeg-concentrating-1', prefix=end, return_as_list=True, length=1024)[0]
  prediction = ("\n".join(prediction.split("\n")[50:])) #remove first 50 lines
  prediction = remove_last_line_from_string(prediction) #remove last line, might be broken
  print(prediction)
