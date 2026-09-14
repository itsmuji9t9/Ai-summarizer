document.getElementById('summarizeBtn').addEventListener('click', async () => {
    const textInput = document.getElementById('inputText').value;
    const outputText = document.getElementById('outputText');
    const loadingAnim = document.getElementById('loadingAnim');
    const summarizeBtn = document.getElementById('summarizeBtn');
    const btnText = document.getElementById('btnText');
    const btnSpinner = document.getElementById('btnSpinner');
    
    if (!textInput.trim()) {
        outputText.innerHTML = "<span style='color: #ef4444;'>Please enter some text to summarize.</span>";
        return;
    }

    // 1. Trigger Loading Animations
    summarizeBtn.disabled = true;
    btnText.textContent = "Generating...";
    btnSpinner.classList.remove('hidden');
    outputText.classList.add('hidden');
    loadingAnim.classList.remove('hidden');

    try {
        const response = await fetch('http://127.0.0.1:8000/api/summarize', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: textInput })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

        const data = await response.json();
        
        // 2. Parse Markdown to HTML
        outputText.innerHTML = marked.parse(data.summary);
        
    } catch (error) {
        outputText.innerHTML = `<span style='color: #ef4444;'>Failed to connect to backend. Is Uvicorn running?</span>`;
        console.error(error);
    } finally {
        // 3. Reset Button and Animations
        summarizeBtn.disabled = false;
        btnText.textContent = "Summarize Text";
        btnSpinner.classList.add('hidden');
        loadingAnim.classList.add('hidden');
        outputText.classList.remove('hidden');
    }
});
