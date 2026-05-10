// Payment page functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize payment page
    console.log('Payment page loaded');
    
    // You can add Stripe, Razorpay or other payment gateway integration here
    // For now, this is a placeholder for payment functionality
});

// Function to process payment
function processPayment() {
    console.log('Processing payment...');
    // Add payment processing logic here
}

// Function to validate payment form
function validatePaymentForm() {
    // Add form validation logic here
    return true;
}
document.getElementById("showLocationBtn").addEventListener("click", function () {

    const customerLocation = "{{ job.location }}";

    if (customerLocation) {

        window.open(
            "https://www.google.com/maps/search/" + customerLocation,
            "_blank"
        );

    } else {

        alert("Location not available");

    }

});