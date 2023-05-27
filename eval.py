from questeval.questeval_metric import QuestEval
import os

source = os.getenv('DOCUMENT')
hypothesis = os.getenv('SUMMARY')
metric_type = os.getenv('TYPE')

questeval = QuestEval(task="summarization", do_weighter=True)

score = questeval.compute_all(hypothesis, source)
if metric_type is None:
    print('Results are: ' + str(score['scores']))
else:
    print('Result is: ' + str(score['scores'][metric_type]))
