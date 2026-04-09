document.addEventListener('DOMContentLoaded', () => {

  // login
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      console.log("submit déclenché");
      console.log(email, password);

      const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });
      console.log(response);

      if (response.ok) {
        const data = await response.json();
        document.cookie = `token=${data.access_token}; path=/`;
        window.location.href = 'index.html';
      } else {
        alert('login failed');
      }
    });
  }

  // cookies
  function getCookie(name) {
    const cookies = document.cookie.split(';');
    let token = null;

    cookies.forEach((cookie) => {
      const clean = cookie.trim();

      if (clean.startsWith(name + '=')) {
        const parts = clean.split('=');
        token = parts[1];
      }
    });

    return token;
  }

  // Place list -> cards creation
  const placesList = document.getElementById('places-list');

  if (placesList) {
    console.log('index détecté');

    const token = getCookie('token');
    console.log(token);

    let allPlaces = [];
    const priceFilter = document.getElementById('price-filter');

    function displayPlaces(places) {
      placesList.innerHTML = '';
      places.forEach(place => {
        const card = document.createElement('div');
        card.className = 'place-card';

        const img = document.createElement('img');
        img.src = place.image_url || 'images/appartment.png';
        img.alt = place.title;
        img.className = 'place-card-img';

        const title = document.createElement('h2');
        title.textContent = place.title;

        const price = document.createElement('p');
        price.className = 'place-price';
        price.textContent = `${place.price}€ / night`;

        const button = document.createElement('a');
        button.textContent = "View Details";
        button.href = `place.html?id=${place.id}`;
        button.className = "details-button";

        card.appendChild(img);
        card.appendChild(title);
        card.appendChild(price);
        card.appendChild(button);

        placesList.appendChild(card);
      });
    }

    async function fetchPlaces() {
      const response = await fetch('http://127.0.0.1:5000/api/v1/places/', {
        method: 'GET',
        headers: { 'Authorization': `Bearer ${token}` },
      });
      console.log(response.status);
      if (response.ok) {
        const data = await response.json();
        console.log(data);
        allPlaces = data;
        displayPlaces(allPlaces);
      } else {
        alert('Failed to fetch places');
      }
    }

    // Price filter
    if (priceFilter) {
      ['10', '50', '100', 'all'].forEach(val => {
        const option = document.createElement('option');
        option.value = val;
        option.textContent = val === 'all' ? 'All' : `${val}€`;
        priceFilter.appendChild(option);
      });

      priceFilter.addEventListener('change', (event) => {
        const selected = event.target.value;
        if (selected === 'all') {
          displayPlaces(allPlaces);
        } else {
          const maxPrice = parseFloat(selected);
          const filtered = allPlaces.filter(p => p.price <= maxPrice);
          displayPlaces(filtered);
        }
      });
    }

    fetchPlaces();
  }

  // Place.html
  const placePage = document.getElementById('place-details');

  if (placePage) {
    const params = new URLSearchParams(window.location.search);
    const placeId = params.get('id');
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');
    const addReviewLink = document.getElementById('add-review-link');

    if (addReviewLink) {
      addReviewLink.href = `add_review.html?id=${placeId}`;
    }

    if (addReviewSection) {
      addReviewSection.style.display = token ? 'block' : 'none';
    }

    async function fetchPlace() {
      const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`);

      if (response.ok) {
        const data = await response.json();
        const place = data;

        const img = document.createElement('img');
        img.src = place.image_url || 'images/appartment.png';
        img.alt = place.title;
        img.className = 'place-detail-img';

        const title = document.createElement('h1');
        title.textContent = data.title;

        const price = document.createElement('p');
        price.textContent = `Price per night: ${data.price} €`;

        const description = document.createElement('p');
        description.textContent = `Description: ${data.description}`;

        const latitude = document.createElement('p');
        latitude.textContent = `Latitude: ${data.latitude}`;

        const longitude = document.createElement('p');
        longitude.textContent = `Longitude: ${data.longitude}`;

        placePage.innerHTML = '';

        // 1. Image
        placePage.appendChild(img);

        // 2. Titre
        placePage.appendChild(title);

        // 3. Description
        placePage.appendChild(description);

        // 4. Infos (price, lat, lon)
        placePage.appendChild(price);
        placePage.appendChild(latitude);
        placePage.appendChild(longitude);

        // 5. Amenities
        if (place.amenities && place.amenities.length > 0) {
          const amenitiesTitle = document.createElement('h3');
          amenitiesTitle.textContent = 'Amenities';

          const amenitiesList = document.createElement('ul');
          amenitiesList.className = 'amenities-list';
          place.amenities.forEach(a => {
            const li = document.createElement('li');
            li.textContent = a.name;
            amenitiesList.appendChild(li);
          });

          placePage.appendChild(amenitiesTitle);
          placePage.appendChild(amenitiesList);
        }

        // 6. Reviews
        fetchReviews(placeId);
      } else {
        alert('Failed to fetch place');
      }
    }

    async function fetchReviews(placeId) {
      try {
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}/reviews/`);
        const reviewsSection = document.getElementById('reviews');

        if (!reviewsSection) return;
        reviewsSection.innerHTML = '';

        if (response.ok) {
          const reviews = await response.json();

          const reviewsTitle = document.createElement('h2');
          reviewsTitle.textContent = 'Reviews';
          reviewsSection.appendChild(reviewsTitle);

          if (reviews.length === 0) {
            const noReviews = document.createElement('p');
            noReviews.className = 'error-msg';
            noReviews.textContent = 'No reviews yet. Be the first!';
            reviewsSection.appendChild(noReviews);
            return;
          }

          reviews.forEach(review => {
            const card = document.createElement('div');
            card.className = 'review-card';

            const rating = document.createElement('p');
            rating.className = 'review-rating';
            rating.textContent = '★'.repeat(review.rating) + '☆'.repeat(5 - review.rating);

            const text = document.createElement('p');
            text.className = 'review-text';
            text.textContent = review.text;

            card.appendChild(rating);
            card.appendChild(text);
            reviewsSection.appendChild(card);
          });
        }
      } catch (err) {
        console.error('Failed to fetch reviews:', err);
      }
    }

    if (placeId) {
      fetchPlace();
    } else {
      placePage.innerHTML = '<p class="error-msg">No place selected.</p>';
    }
  }

  // Add-review
  const reviewForm = document.getElementById('review-form');

  if (reviewForm) {
    const token = getCookie('token');
    if (!token) {
      window.location.href = 'index.html';
    } else {
      const params = new URLSearchParams(window.location.search);
      const placeId = params.get('id');

      reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const comment = document.getElementById('review').value;
        const rating = parseInt(document.getElementById('rating').value, 10);

        const response = await fetch('http://127.0.0.1:5000/api/v1/reviews/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify({
            text: comment,
            rating: rating,
            place_id: placeId
          })
        });

        if (response.ok) {
          alert('Review submitted successfully!');
          reviewForm.reset();
          window.location.href = `place.html?id=${placeId}`;
        } else {
          const errorData = await response.json();
          alert(errorData.error || 'Failed to submit review.');
        }
      });
    }
  }

});