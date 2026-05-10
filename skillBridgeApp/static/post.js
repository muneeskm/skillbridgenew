document.addEventListener("DOMContentLoaded", function () {

    const locationBtn = document.getElementById("locationBtn");
    const locationInput = document.getElementById("locationInput");
    const showLocation = document.getElementById("showLocation");

    locationBtn.addEventListener("click", function () {

        if (navigator.geolocation) {

            navigator.geolocation.getCurrentPosition(

                function(position) {

                    const lat = position.coords.latitude;
                    const lng = position.coords.longitude;

                    const finalLocation = lat + ", " + lng;

                    const confirmLocation = confirm(
                        "Confirm this location?\n\n" + finalLocation
                    );

                    if (confirmLocation) {

                        locationInput.value = finalLocation;

                        showLocation.innerHTML =
                            "📍 Selected Location: " + finalLocation;

                    }

                },

                function() {

                    alert("Location access denied");

                }

            );

        } else {

            alert("Geolocation not supported");

        }

    });

});