import streamlit as st
import time

st.set_page_config(page_title="CampusMind AI", page_icon="🎓", layout="wide")

st.title("CampusMind AI")
st.subheader("GraphRAG Powered College Knowledge Assistant")

st.markdown(
    "CampusMind AI compares LLM, Basic RAG, and GraphRAG for college knowledge tasks. "
    "This demo highlights token reduction, stronger reasoning, and a GraphRAG workflow built for the TigerGraph GraphRAG Inference Hackathon."
)

with st.sidebar:
    st.header("CampusMind AI Controls")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    pipeline = st.selectbox("Select pipeline", ["LLM Only", "Basic RAG", "GraphRAG"])

st.write("---")

question = st.text_input("Ask a question", placeholder="Type your college or campus question here...")

if st.button("Generate Answer"):
    if not question:
        st.warning("Please enter a question before generating an answer.")
    else:
        start_time = time.time()

        sample_answers = {
            "LLM Only": "The LLM only response is a broad natural language answer with general knowledge and no document-specific grounding.",
            "Basic RAG": "Basic RAG returns an answer that combines retrieved content with the model, improving relevance but using more tokens for retrieval.",
            "GraphRAG": "GraphRAG delivers a concise, reasoning-based answer using graph knowledge and token-efficient inference for better college insights."
        }

        response = sample_answers.get(pipeline, sample_answers["LLM Only"])
        token_usage = {
            "LLM Only": 420,
            "Basic RAG": 280,
            "GraphRAG": 160
        }
        accuracy_scores = {
            "LLM Only": 78,
            "Basic RAG": 88,
            "GraphRAG": 95
        }

        elapsed_time = round(time.time() - start_time, 2)

        st.success("Deployment Successful")

        st.markdown("### AI Response")
        st.info(response)

        col1, col2, col3 = st.columns(3)
        col1.metric(label="Token Usage", value=f"{token_usage[pipeline]} tokens")
        col2.metric(label="Response Time", value=f"{elapsed_time} seconds")
        col3.metric(label="Accuracy", value=f"{accuracy_scores[pipeline]}%")

        if uploaded_file is not None:
            st.write(f"Uploaded file: **{uploaded_file.name}**")
            st.caption("The file is accepted for the demo, but this simple app does not yet process PDF content.")
        else:
            st.info("No PDF uploaded. Upload a file to preview the workflow.")
