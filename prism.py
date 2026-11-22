import gradio as gr

def ai_assistant(message, history):
    # This is a placeholder response. Soon, we will connect this to real AI models!
    return f"Hello! You said: '{message}'. I am your AI assistant being built right now!"

# Creates a clean chat interface with voice, text, and media upload features
demo = gr.ChatInterface(
    fn=ai_assistant,
    title="Endrit AI Assistant",
    description="Your all-in-one AI for chatting, coding, and media generation.",
    textbox=gr.Textbox(placeholder="Ask me anything, ask for code, or describe a photo/video...", container=False, scale=7),
)

if __name__ == "__main__":
    demo.launch()
