
# import gensim
# from gensim.models import Word2Vec
# from nltk.tokenize import word_tokenize
# import numpy as np

# x = ["Accepting", "Ambitious", "Authentic",
#   "Brave", "Caring", "Challenging", "Cheerful",
#   "Collaborative", "Communicator", "Creative", "Curious",
#   "Decisive", "Dedicated", "Detailed", "Determined",
#   "Enthusiastic", "Flexible", "Friendly", "Funny",
#   "Hard-working", "Helpful", "Honest", "Integrity",
#   "Kind", "Leader", "Logical", "Loyal",
#   "Motivated", "Nurturing", "Open-minded", "Optimistic",
#   "Persistent", "Practical", "Problem-solver", "Resilient",
#   "Responsible", "Self-controlled", "Strong", "Supportive",
#   "Team-player", "Trustworthy", "Versatile", "Well-organised"]
  

import numpy as np
values_dict = {'Accepting': np.array([ 0.06428725, -0.13155352, -0.0321486 ], dtype=np.float32), 
  'Ambitious': np.array([-0.00389444, -0.08164057, -0.0109958 ], dtype=np.float32), 
  'Authentic': np.array([ 0.02690884, -0.12021685, -0.10309633], dtype=np.float32), 
  'Brave': np.array([-0.16074964, -0.03111786, -0.13517387], dtype=np.float32), 
  'Caring': np.array([ 0.08306323, -0.0216064 ,  0.03223721], dtype=np.float32), 
  'Challenging': np.array([-0.03650258, -0.03971388,  0.12708753], dtype=np.float32), 
  'Cheerful': np.array([-0.08263457,  0.02397639, -0.02726813], dtype=np.float32), 
  'Collaborative': np.array([ 0.01774076, -0.04113457, -0.07959463], dtype=np.float32), 
  'Communicator': np.array([-0.10602044, -0.05155713,  0.02281729], dtype=np.float32), 
  'Creative': np.array([-0.09139125,  0.14582069, -0.08788797], dtype=np.float32), 
  'Curious': np.array([-0.01939319, -0.09517483,  0.15877329], dtype=np.float32), 
  'Decisive': np.array([-0.07646149,  0.09162694, -0.06120358], dtype=np.float32), 
  'Dedicated': np.array([ 0.1435031 , -0.02945057,  0.08400583], dtype=np.float32), 
  'Detailed': np.array([-0.09391214, -0.09656535,  0.04453101], dtype=np.float32), 
  'Determined': np.array([ 0.12501657,  0.13705763, -0.05373069], dtype=np.float32), 
  'Enthusiastic': np.array([ 0.14191411, -0.03596821, -0.05008933], dtype=np.float32), 
  'Flexible': np.array([-0.15329061, -0.00236517,  0.09270877], dtype=np.float32), 
  'Friendly': np.array([0.00126645, 0.1350122 , 0.03622277], dtype=np.float32), 
  'Funny': np.array([ 0.1432402 ,  0.1186475 , -0.01591853], dtype=np.float32), 
  'Hard-working': np.array([-0.00365656, -0.07400345, -0.11064011], dtype=np.float32), 
  'Helpful': np.array([-0.1104922 ,  0.10520843, -0.14713043], dtype=np.float32), 
  'Honest': np.array([ 0.06489957, -0.04282324,  0.12899074], dtype=np.float32), 
  'Integrity': np.array([-0.14234246,  0.03319981,  0.14125317], dtype=np.float32), 
  'Kind': np.array([-0.01800544,  0.11379769, -0.09873065], dtype=np.float32), 
  'Leader': np.array([ 0.15200578, -0.00726446, -0.00307272], dtype=np.float32), 
  'Logical': np.array([ 0.0148541 , -0.13476855,  0.09444422], dtype=np.float32), 
  'Loyal': np.array([-0.01991683,  0.01132811, -0.02648761], dtype=np.float32), 
  'Motivated': np.array([ 0.04550078, -0.03857772, -0.0868635 ], dtype=np.float32), 
  'Nurturing': np.array([ 0.02241381, -0.13906482,  0.12420508], dtype=np.float32), 
  'Open-minded': np.array([ 0.08205283,  0.1599562 , -0.13433826], dtype=np.float32), 
  'Optimistic': np.array([-0.13759395,  0.08519354, -0.12256126], dtype=np.float32), 
  'Persistent': np.array([ 0.15811232, -0.08052292,  0.12302719], dtype=np.float32), 
  'Practical': np.array([-0.15533376,  0.1510607 ,  0.06361027], dtype=np.float32), 
  'Problem-solver': np.array([0.16521293, 0.06232329, 0.05846072], dtype=np.float32), 
  'Resilient': np.array([ 0.11831702,  0.02591503, -0.05135284], dtype=np.float32), 
  'Responsible': np.array([-0.10043201,  0.07642348,  0.07369573], dtype=np.float32), 
  'Self-controlled': np.array([ 0.16265516,  0.05805578, -0.03081367], dtype=np.float32), 
  'Strong': np.array([-0.06774265,  0.04157138, -0.10642529], dtype=np.float32), 
  'Supportive': np.array([ 0.08563083, -0.16280797,  0.00973908], dtype=np.float32), 
  'Team-player': np.array([-0.13552563, -0.12775017,  0.0408115 ], dtype=np.float32), 
  'Trustworthy': np.array([-0.10171342, -0.04982075,  0.00759074], dtype=np.float32), 
  'Versatile': np.array([-0.10564943,  0.11260317,  0.14714815], dtype=np.float32), 
  'Well-organised': np.array([-0.11328536,  0.01449533, -0.11352558], dtype=np.float32)}


cluster_centroids =[[-0.04977357, -0.02877725, -0.02636996],
                    [ 0.05722304,  0.00576233,  0.00946908],
                    [-0.01488634,  0.07766376,  0.01205709],
                    [ 0.02096947,  0.0497361 , -0.06257594],
                    [-0.01756257, -0.01770724,  0.05824161]]