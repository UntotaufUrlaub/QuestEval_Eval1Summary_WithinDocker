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
qg_batch_size = os.getenv("QG_BATCH_SIZE")
qg_batch_size = int(qg_batch_size) if qg_batch_size is not None else None
clf_batch_size = os.getenv("CLF_BATCH_SIZE")
clf_batch_size = int(clf_batch_size) if clf_batch_size is not None else None

questeval = QuestEval(isCuda=isCuda, use_cache=False,
                     qg_batch_size=qg_batch_size,
                     clf_batch_size=clf_batch_size
                     )

score = questeval.corpus_questeval(hypothesis=[hypothesis], sources=[source])
print('Result is: ' + str(score['ex_level_scores'][0]))
