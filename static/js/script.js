
document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('title');
    const count = document.getElementById('charCount');
    if (input && count) {
        input.addEventListener('input', () => {
            count.textContent = input.value.length;
        });
    }
});
