import streamlit as st
from backend.video_downloader import download_video
from backend.llm_summariser import analyse_audio
from backend.text_to_speech import text_to_speech


st.title("YouTube Video Summariser")

video_url = st.text_input(
    label="Enter video link", value="https://www.youtube.com/watch?v=5O46Rqh5zHE"
)

if st.button(label="Summarise", use_container_width=True):
    video_title = download_video(video_url)
    llm_response = analyse_audio("data/audio.mp3")
    summary_text = llm_response["summary"]
    transcript = llm_response["results"]

    label_relevance = "\n".join(
        [
            f"{label}: {round(relevance * 100,1)}%"
            for label, relevance in llm_response["label_relevance"].items()
        ]
    )

    st.subheader(video_title)
    tab1, tab2, tab3 = st.tabs(["Summary", "Topics", "Transcript"])
    with tab1:
        st.markdown(summary_text)
        text_to_speech(summary_text)
    with tab2:
        for label, relevance in llm_response["label_relevance"].items():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(label)
            with col2:
                st.progress(relevance)
            with col3:
                st.write(f"{round(relevance * 100, 2)}%")
    with tab3:
        for item in transcript:
            st.markdown(
                f"""
                Timestamp: {item.timestamp.start} - {item.timestamp.end}
                
                Text: {item.text}                     
                """
            )
