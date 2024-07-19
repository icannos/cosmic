
COSMIC: Mutual Information for Task-Agnostic Summarization Evaluation (ACL 2024, Main/Oral)
=================================================================

[Abstract](https://arxiv.org/abs/2402.19457) | [Paper](https://arxiv.org/abs/2402.19457) | [Code](https://github.com/icannos/cosmic)

COSMIC metric for summarizers. 

You migh also be interested in an extension to evaluate embedders [When is an embedding model better than another?](https://arxiv.org/abs/2406.07640)


## Installation

```bash
pip install git+https://github.com/icannos/cosmic
````

## Usage

```python
import pandas as pd
from cosmic import CosmicScorer


# this only a simple example, there should be at least 20k samples for to get a significant result
source = ['The quick brown fox jumps over the lazy dog', 'Once upon a time, there was a lazy dog', 'I believe the news is fake but the dog is real']
summaries = ['fox jumps over dog', 'a lazy dog', 'news is fake but the dog is real']


scorer = CosmicScorer(batch_size=2, knife_args_dict={'n_epochs' : 10})
scorer.score(source, summaries)


```


# Citation

If you use this code, please cite the following papers:

```
@misc{darrin2024textttcosmicmutualinformationtaskagnostic,
      title={$\texttt{COSMIC}$: Mutual Information for Task-Agnostic Summarization Evaluation}, 
      author={Maxime Darrin and Philippe Formont and Jackie Chi Kit Cheung and Pablo Piantanida},
      year={2024},
      eprint={2402.19457},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2402.19457}, 
}

@misc{darrin2024embeddingmodelpromisinganother,
      title={When is an Embedding Model More Promising than Another?}, 
      author={Maxime Darrin and Philippe Formont and Ismail Ben Ayed and Jackie CK Cheung and Pablo Piantanida},
      year={2024},
      eprint={2406.07640},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2406.07640}, 
}
```

