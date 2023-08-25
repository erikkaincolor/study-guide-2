# Create your classes here
let juggleInterval;
let isJuggling = false;

function moveCursor() {
    let x = 100;
    let y = 100;
    const step = 10;

    juggleInterval = setInterval(() => {
        if (isJuggling) {
            // Move the cursor right
            x += step;
            window.scrollTo(x, y);

            // Check if it's after 5 PM Chicago time
            const now = new Date();
            const chicagoTime = now.toLocaleString('en-US', { timeZone: 'America/Chicago' });
            const hour = new Date(chicagoTime).getHours();
            if (hour >= 17) {
                clearInterval(juggleInterval);
                alert('Juggling stopped after 5 PM Chicago time.');
                return;
            }
        }
    }, 500);
}

// Start juggling when the page loads
moveCursor();

// Listen for the spacebar key press to stop juggling
document.addEventListener('keydown', (event) => {
    if (event.key === ' ') {
        isJuggling = false;
        clearInterval(juggleInterval);
        alert('Juggling stopped.');
    }
});
