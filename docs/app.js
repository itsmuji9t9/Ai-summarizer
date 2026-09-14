document.getElementById('summarizeBtn').addEventListener('click', async () => {
    const textInput = document.getElementById('inputText').value;
    const outputSection = document.getElementById('outputSection');
    const outputText = document.getElementById('outputText');
    const loadingAnim = document.getElementById('loadingAnim');
    const summarizeBtn = document.getElementById('summarizeBtn');
    const btnText = document.getElementById('btnText');
    const btnSpinner = document.getElementById('btnSpinner');
    
    if (!textInput.trim()) {
        outputSection.classList.remove('hidden');
        outputText.classList.remove('hidden');
        outputText.innerHTML = "<span style='color: #ef4444;'>Hold your horses! Paste some text first.</span>";
        return;
    }

    // Trigger Playful UI States
    summarizeBtn.disabled = true;
    btnText.textContent = "Squeezing..."; 
    btnSpinner.classList.remove('hidden');
    
    outputSection.classList.remove('hidden');
    outputText.classList.add('hidden');
    loadingAnim.classList.remove('hidden');

    try {
        // REPLACE THIS URL WITH YOUR LIVE RENDER LINK
        const response = await fetch('https://ai-summarizer-vjyt.onrender.com/api/summarize', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: textInput })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

        const data = await response.json();
        outputText.innerHTML = marked.parse(data.summary);
        
    } catch (error) {
        outputText.innerHTML = `<span style='color: #ef4444;'>Uh oh, the backend took a nap. Is Render awake?</span>`;
        console.error(error);
    } finally {
        // Reset States
        summarizeBtn.disabled = false;
        btnText.textContent = "Summarize";
        btnSpinner.classList.add('hidden');
        loadingAnim.classList.add('hidden');
        outputText.classList.remove('hidden');
    }
});
