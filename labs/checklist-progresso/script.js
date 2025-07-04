function updateProgress() {
    const checkboxes = document.querySelectorAll('#checklist input[type="checkbox"]');
    const total = checkboxes.length;
    const checked = Array.from(checkboxes).filter(cb => cb.checked).length;
    const percentage = (checked / total) * 100;
    document.getElementById('progressBar').style.width = percentage + '%';
  }
  