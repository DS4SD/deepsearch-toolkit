from transformers.pipelines.token_classification import AggregationStrategy

from deepsearch.model.examples.hf_ner_annotator.model import HuggingFaceNERAnnotator
from deepsearch.model.server.config import Settings
from deepsearch.model.server.model_app import ModelApp


def run():
    settings = Settings(api_key="example123")
    app = ModelApp(settings)
    app.register_model(
        model=HuggingFaceNERAnnotator(
            config=HuggingFaceNERAnnotator.Config(
                model_name_or_path="elastic/distilbert-base-cased-finetuned-conll03-english",
            ),
        ),
        name="elastic-distilbert",
    )
    app.register_model(
        model=HuggingFaceNERAnnotator(
            config=HuggingFaceNERAnnotator.Config(
                model_name_or_path="elastic/distilbert-base-cased-finetuned-conll03-english",
                aggregation_strategy=AggregationStrategy.AVERAGE,
            ),
        ),
        name="elastic-distilbert-avg",
    ),
    app.register_model(
        model=HuggingFaceNERAnnotator(
            config=HuggingFaceNERAnnotator.Config(
                model_name_or_path="StanfordAIMI/stanford-deidentifier-base",
                aggregation_strategy=AggregationStrategy.AVERAGE,
            )
        ),
        name="stanford-deidentifier-avg",
    )
    app.register_model(
        model=HuggingFaceNERAnnotator(
            config=HuggingFaceNERAnnotator.Config(
                model_name_or_path="xlm-roberta-large-finetuned-conll03-english",
                aggregation_strategy=AggregationStrategy.AVERAGE,
            )
        ),
        name="xlm-roberta-avg",
    )
    app.run()


if __name__ == "__main__":
    run()
