import assemblyai as aai
import toml
import random

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_apikey(connector, item):
    logger = logging.getLogger(f"{__name__}.get_apikey")
    logger.debug(f"Getting API key from secrets.toml [{connector}][{item}]")
    secrets = toml.load(".streamlit/secrets.toml")
    result = secrets[connector][item]
    return result


def cycled_apikey():
    logger = logging.getLogger(f"{__name__}.cycled_apikey")
    key_index = random.randint(1, 2)
    api_key = get_apikey("ai-assembly", f"api_key_{key_index}")
    logger.debug(f"Using API Key index {key_index}")
    logger.debug(f"API Key is {api_key}")
    return api_key


def analyse_audio(FILE_URL):
    logger = logging.getLogger(f"{__name__}.analyse_audio")
    logger.info("Running AI Assembly LLM model")
    # replace with your API token
    aai.settings.api_key = cycled_apikey()

    # URL of the file to transcribe
    config = aai.TranscriptionConfig(
        iab_categories=True,
        summarization=True,
        summary_model=aai.SummarizationModel.informative,  # optional
        # summary_type=aai.SummarizationType.gist,  # does not work out of the box
        # summary_type=aai.SummarizationType.headline,  # works
        # summary_type=aai.SummarizationType.paragraph,  # optional
        summary_type=aai.SummarizationType.bullets,  # works
        # summary_type=aai.SummarizationType.bullets_verbose,
    )

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL, config=config)

    # TODO remove for now, for performance reasons
    # # Get the parts of the transcript that were tagged with topics
    # for result in transcript.iab_categories.results:
    #     print(result.text)
    #     print(f"Timestamp: {result.timestamp.start} - {result.timestamp.end}")

    #     for label in result.labels:
    #         print(label.label)  # topic
    #         print(label.relevance)  # how relevant the label is for the portion of text

    # Get a summary of all topics in the transcript

    logger.debug(transcript.summary)

    response = {
        "summary": transcript.summary,
        "label_relevance": transcript.iab_categories.summary,
        "results": transcript.iab_categories.results,
    }

    return response


if __name__ == "__main__":
    print("Running standalone script")
    # FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
    FILE_URL = "data/is it good now  Visconti Homo Sapiens Fountain Pen Review.mp3"
    response = analyse_audio(FILE_URL)
    print("Response:", response)
