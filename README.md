# Generational-Loop-GPT2
Simple script to infinite amounts of data from GPT-2 by using last x characters as next input


GPT-2 Simple is required:

pip install -q gpt-2-simple

# Description of code
Lines 1-29:

Imports needed library, GPT-2 simple
Downloads the selected model, in this case we use the 124M parameters model
Selects the file to learn from, and then learns


Lines 30 - 40:

Loads the weights for GPT-2 from the previous learning process
Generates 10 blocks of 100 characters with no prefix (each are not inspired by the last) - the amount of data can be changed by editing the loop as well as the length parameter within gpt2.generate

Lines 41-63:

Same as above, except generate data n times where the prefix for every n>1 generation is the last 50 characters of the previous generation with the exception of the final line of the file. Since it is most likely that the last line of the csv will be broken, we simply delete it rather than hope that GPT2 will also figure this out.  

It is set to stop when "END" is found in the prediction, i.e. you may want to put this flag in if multiple series have starts and ends. If not, then it'll just generate forever, and you can stop it when you're happy with the amount of data that has been output

The first 50 lines are removed before the output is presented in order to prevent the repetition of the prefix twice (it has already been printed at the previous step in the loop)


## To do
1. Add new methods of stopping, i.e. a line counter for a csv or characters in a txt - at the moment we just generate endlessly until a point is reached

2. Experiment with more hyperparameters such as temperature, and the amount of prefix as input 


## Usage
Feel free to use and edit this code as you please, remember to cite the original GPT2 and the library gpt-2-simple
