from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Dummy function to simulate GPT response
def simulate_gpt_interaction(prompt, model_type="pretrained"):
    # You can replace this with actual GPT model calls
    if model_type == "pretrained":
        return f"Simulated response for '{prompt}' (pretrained model)"
    else:
        return f"Simulated response for '{prompt}' (fine-tuned model)"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data['prompt']
    conversation = simulate_gpt_interaction(prompt)
    return jsonify(conversation=conversation)

@app.route('/generate_summaries', methods=['POST'])
def generate_summaries():
    data = request.json
    prompt = data['prompt']
    summary_pretrained = simulate_gpt_interaction(prompt, "pretrained")
    summary_finetuned = simulate_gpt_interaction(prompt, "finetuned")
    return jsonify(summary_pretrained=summary_pretrained, summary_finetuned=summary_finetuned)

@app.route('/compare_summaries', methods=['POST'])
def compare_summaries():
    data = request.json
    summary1 = data['summary1']
    summary2 = data['summary2']
    comparison = simulate_gpt_interaction(f"Compare: '{summary1}' with '{summary2}'", "pretrained")
    return jsonify(comparison=comparison)

if __name__ == '__main__':
    app.run(debug=True)
