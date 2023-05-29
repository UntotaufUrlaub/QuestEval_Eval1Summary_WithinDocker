from questeval.questeval_metric import QuestEval
import os
import ast

source = os.getenv('DOCUMENT')
hypothesis = os.getenv('SUMMARY')

questeval = QuestEval()

score = questeval.corpus_questeval(hypothesis=[hypothesis], sources=[source])
print('Result is: ' + str(score['ex_level_scores'][0]))
