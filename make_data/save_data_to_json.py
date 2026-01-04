import numpy as np
import json

dat=np.load('/home/maria/ProjectionSort/data/hybrid_neural_responses_reduced.npy')
ts=dat[:,2]
print(ts.shape)
target_path='/home/maria/ThesisSVG/SummaryFigure/data/mouse_embedding.json'