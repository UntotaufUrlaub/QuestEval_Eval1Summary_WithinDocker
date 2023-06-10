from questeval.questeval_metric import QuestEval
import os

source = os.getenv('DOCUMENT')
hypothesis = os.getenv('SUMMARY')
metric_type = os.getenv('TYPE')
device = os.getenv('Device')
if device == 'cpu':
    isCude = False
elif device == 'gpu':
    isCuda = True
else:
    raise ValueError(f"Unknown devise: {device}")
qg_batch_size = os.getenv("QG_BATCH_SIZE")
qg_batch_size = int(qg_batch_size) if qg_batch_size is not None else None
clf_batch_size = os.getenv("CLF_BATCH_SIZE")
clf_batch_size = int(clf_batch_size) if clf_batch_size is not None else None

questeval = QuestEval(task="summarization", do_weighter=True, isCuda=isCuda,
                      qg_batch_size=qg_batch_size,
                      clf_batch_size=clf_batch_size
                      )

score = questeval.compute_all(hypothesis, source)
if metric_type is None:
    print('Results are: ' + str(score['scores']))
else:
    print('Result is: ' + str(score['scores'][metric_type]))
