
COSMIC: Mutual Information for Task-Agnostic Summarization Evaluation
=================================================================

[Abstract](https://arxiv.org/abs/2402.19457) | [Paper](https://arxiv.org/abs/2402.19457) | [Code](https://github.com/icannos/cosmic)


# Readme 

COSMIC metric for summarizers. 

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

### Experiments and analysis

All the experiments and analysis are provided in `summarization_evaluation/'