import gradio as gr
from conversation import run_conversation

with gr.Blocks() as demo:
    gr.Markdown("# Multi-Chatbot Conversation Interface")
    gr.Markdown(
        "This interface uses three chatbots: **OPEN AI**, **CLAUDE**, and **OLLAMA**. "
        "The default topic is *'what do you think about humans in one sentence?'*. "
        "You may also enter your own topic below."
    )
    
    with gr.Row():
        topic_input = gr.Textbox(
            label="Conversation Topic", 
            value="what do you think about humans in one sentence?", 
            lines=2
        )
        run_button = gr.Button("Run Conversation")
    
    gr.Markdown("### Model Outputs")
    with gr.Row():
        openai_output = gr.Markdown(label="OPEN AI")
        claude_output = gr.Markdown(label="CLAUDE")
        ollama_output = gr.Markdown(label="OLLAMA")
    
    run_button.click(
        fn=run_conversation, 
        inputs=topic_input, 
        outputs=[openai_output, claude_output, ollama_output],
        show_progress=True
    )
    
demo.launch(inbrowser=True)
