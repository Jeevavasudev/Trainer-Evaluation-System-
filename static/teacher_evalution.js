// teacher_evaluation.js

const starRating = document.getElementById('starRating');
const ratingInput = document.getElementById('ratingInput');

// Attach event listeners to stars for the rating
starRating.addEventListener('click', (event) => {
    const selectedRating = event.target.getAttribute('data-rating');
    if (selectedRating) {
        // Update the hidden input with the selected rating value
        ratingInput.value = selectedRating;
        // Highlight the stars up to the selected rating
        const stars = starRating.getElementsByClassName('star');
        for (let i = 0; i < stars.length; i++) {
            if (i < selectedRating) {
                stars[i].classList.add('selected');
            } else {
                stars[i].classList.remove('selected');
            }
        }
    }
});
