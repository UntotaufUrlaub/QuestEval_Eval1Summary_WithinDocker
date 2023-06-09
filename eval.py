from questeval.questeval_metric import QuestEval
import os
import ast

source = os.getenv('DOCUMENT')
hypothesis = os.getenv('SUMMARY')
device = os.getenv('Device')
if device == 'cpu':
    isCude = False
elif device == 'gpu':
    isCuda = True
else:
    raise ValueError(f"Unknown devise: {device}")

questeval = QuestEval( isCuda=isCuda)

score = questeval.corpus_questeval(hypothesis=[hypothesis], sources=[source])
print('Result is: ' + str(score['ex_level_scores'][0]))
