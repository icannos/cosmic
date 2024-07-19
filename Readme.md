
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
from cosmic import COSMICScorer



# load a dataframe with text and summaries
# with columns: text, summary
pd = pd.read_csv('data.csv') 

scorer = COSMICScorer()
scorer.score(pd['text'].tolist(), pd['summary'].tolist())
```

### Experiments and analysis

All the experiments and analysis are provided in `summarization_evaluation/'