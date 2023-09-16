import assemblyai as aai


def analyse_audio(FILE_URL):
    # replace with your API token
    aai.settings.api_key = (
        f"deacc26566c14ea1b48e51f4c99afbb6"  # TODO put this into secrets
    )

    # URL of the file to transcribe
    config = aai.TranscriptionConfig(
        iab_categories=True,
        summarization=True,
        summary_model=aai.SummarizationModel.informative,  # optional
        summary_type=aai.SummarizationType.bullets,  # optional
    )

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL, config=config)

    # Get the parts of the transcript that were tagged with topics
    for result in transcript.iab_categories.results:
        print(result.text)
        print(f"Timestamp: {result.timestamp.start} - {result.timestamp.end}")

    for label in result.labels:
        print(label.label)  # topic
        print(label.relevance)  # how relevant the label is for the portion of text

    # Get a summary of all topics in the transcript
    for label, relevance in transcript.iab_categories.summary.items():
        print(f"Audio is {relevance * 100}% relevant to {label}")

    print(transcript.summary)

    response = {
        "summary": transcript.summary,
        "results": transcript.iab_categories.results,
    }

    return response


if __name__ == "__main__":
    print("Running standalone script")
    # FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
    FILE_URL = (
        "data/onlymp3.to - Streamlit LLM Hackathon-TlVM8fO02_c-192k-1694869901.mp3"
    )
    response = analyse_audio(FILE_URL)
    print("Response:", response)
