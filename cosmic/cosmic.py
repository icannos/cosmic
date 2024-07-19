from typing import Tuple, List

import torch
from .estimators.knife_estimator import KNIFEEstimator, KNIFEArgs

from sentence_transformers import SentenceTransformer


def embedd_sourcetexts_and_summaries(
    text_1: List[str], text_2: List[str], model
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    :param df: a pandas dataframe with at least the columns 'text' and 'summary'
    :param model: a sentence transformer model
    :return: a tuple of two torch tensors, one for the text embeddings and one for the summary embeddings
    """

    text_embeddings = model.encode(text_1, convert_to_tensor=True)
    summary_embeddings = model.encode(text_2, convert_to_tensor=True)

    return text_embeddings, summary_embeddings


class CosmicScorer:
    def __init__(self, embedding_model: str):

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.embedding_model = embedding_model
        self.model = SentenceTransformer(self.embedding_model)

        self.knife_args = KNIFEArgs(device=self.device)

    def __call__(self, *args, **kwargs):
        return self.score(*args, **kwargs)

    def score(self, text_1: List[str], text_2: List[str]) -> float:
        """
        :param text_1: a list of strings
        :param text_2: a list of strings
        :return: a float representing the mutual information between text_1 and text_2
        """

        text_embeddings, summary_embeddings = embedd_sourcetexts_and_summaries(
            text_1, text_2, self.model
        )

        knife_estimator = KNIFEEstimator(
            self.knife_args,
            text_embeddings.shape[1],
            summary_embeddings.shape[1],
        )

        mi, _, _ = knife_estimator.eval(text_embeddings, summary_embeddings)

        return mi
