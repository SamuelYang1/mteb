from __future__ import annotations

from mteb.abstasks.AbsTaskRetrieval import AbsTaskRetrieval
from mteb.abstasks.TaskMetadata import TaskMetadata

_EVAL_SPLIT = "test"


class CosQARetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="CosQA",
        description="The dataset is a collection of natural language queries and their corresponding code snippets. The task is to retrieve the most relevant code snippet for a given query.",
        reference="https://arxiv.org/abs/2105.13239",
        dataset={
            "path": "CoIR-Retrieval/cosqa",
            "revision": "bc5efb7e9d437246ce393ed19d772e08e4a79535",
        },
        type="Retrieval",
        category="p2p",
        modalities=["text"],
        eval_splits=[_EVAL_SPLIT],
        eval_langs=["eng-Latn", "python-Code"],
        main_score="ndcg_at_10",
        date=("2021-05-07", "2021-05-07"),
        domains=["Programming", "Written"],
        task_subtypes=["Code retrieval"],
        license="mit",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@misc{huang2021cosqa20000webqueries,
  archiveprefix = {arXiv},
  author = {Junjie Huang and Duyu Tang and Linjun Shou and Ming Gong and Ke Xu and Daxin Jiang and Ming Zhou and Nan Duan},
  eprint = {2105.13239},
  primaryclass = {cs.CL},
  title = {CoSQA: 20,000+ Web Queries for Code Search and Question Answering},
  url = {https://arxiv.org/abs/2105.13239},
  year = {2021},
}
""",
    )
