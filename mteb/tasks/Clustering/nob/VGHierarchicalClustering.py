from __future__ import annotations

from mteb.abstasks.AbsTaskClusteringFast import AbsTaskClusteringFast
from mteb.abstasks.TaskMetadata import TaskMetadata

N_SAMPLES = 2048


def split_labels(record: dict) -> dict:
    record["labels"] = record["labels"].split(",")[:2]
    return record


class VGHierarchicalClusteringP2P(AbsTaskClusteringFast):
    max_document_to_embed = N_SAMPLES
    max_fraction_of_documents_to_embed = None

    metadata = TaskMetadata(
        name="VGHierarchicalClusteringP2P",
        dataset={
            "path": "navjordj/VG_summarization",
            "revision": "d4c5a8ba10ae71224752c727094ac4c46947fa29",
        },
        description="Articles and their classes (e.g. sports) from VG news articles extracted from Norsk Aviskorpus.",
        reference="https://huggingface.co/datasets/navjordj/VG_summarization",
        type="Clustering",
        category="p2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["nob-Latn"],
        main_score="v_measure",
        date=("2020-01-01", "2024-12-31"),  # best guess
        domains=["News", "Non-fiction", "Written"],
        license="cc-by-nc-4.0",
        annotations_creators="derived",
        dialect=[],
        task_subtypes=["Thematic clustering"],
        sample_creation="found",
        bibtex_citation=r"""
@mastersthesis{navjord2023beyond,
  author = {Navjord, J{\\o}rgen Johnsen and Korsvik, Jon-Mikkel Ryen},
  school = {Norwegian University of Life Sciences, {\\AA}s},
  title = {Beyond extractive: advancing abstractive automatic text summarization in Norwegian with transformers},
  year = {2023},
}
""",
        prompt="Identify the categories (e.g. sports) of given articles in Norwegian",
    )

    def dataset_transform(self) -> None:
        self.dataset = self.dataset.rename_columns(
            {"article": "sentences", "classes": "labels"}
        )
        self.dataset = self.dataset.map(split_labels)
        # Subsampling the dataset
        self.dataset["test"] = self.dataset["test"].train_test_split(
            test_size=N_SAMPLES, seed=self.seed
        )["test"]


class VGHierarchicalClusteringS2S(AbsTaskClusteringFast):
    max_document_to_embed = N_SAMPLES
    max_fraction_of_documents_to_embed = None

    metadata = TaskMetadata(
        name="VGHierarchicalClusteringS2S",
        dataset={
            "path": "navjordj/VG_summarization",
            "revision": "d4c5a8ba10ae71224752c727094ac4c46947fa29",
        },
        description="Articles and their classes (e.g. sports) from VG news articles extracted from Norsk Aviskorpus.",
        reference="https://huggingface.co/datasets/navjordj/VG_summarization",
        type="Clustering",
        category="p2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["nob-Latn"],
        main_score="v_measure",
        date=("2020-01-01", "2024-12-31"),  # best guess
        domains=["News", "Non-fiction", "Written"],
        license="cc-by-nc-4.0",
        annotations_creators="derived",
        dialect=[],
        task_subtypes=["Thematic clustering"],
        sample_creation="found",
        bibtex_citation=r"""
@mastersthesis{navjord2023beyond,
  author = {Navjord, J{\\o}rgen Johnsen and Korsvik, Jon-Mikkel Ryen},
  school = {Norwegian University of Life Sciences, {\\AA}s},
  title = {Beyond extractive: advancing abstractive automatic text summarization in Norwegian with transformers},
  year = {2023},
}
""",
        prompt="Identify the categories (e.g. sports) of given articles in Norwegian",
    )

    def dataset_transform(self) -> None:
        self.dataset = self.dataset.rename_columns(
            {"ingress": "sentences", "classes": "labels"}
        )
        self.dataset = self.dataset.map(split_labels)
        # Subsampling the dataset
        self.dataset["test"] = self.dataset["test"].train_test_split(
            test_size=N_SAMPLES, seed=self.seed
        )["test"]
