

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

  //cookies
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

  //Place list -> cards creation
  const placesList = document.getElementById('places-list');

  if (placesList) {
    console.log('index détecté');

    const token = getCookie('token');
    console.log(token);

    async function fetchPlaces() {
    const response = await fetch('http://127.0.0.1:5000/api/v1/places/', {
      method: 'GET',
      headers: {'Authorization': `Bearer ${token}`},
    })
    console.log(response.status);
    if (response.ok) {
      const data = await response.json();
      console.log(data);

    
    data.forEach(place => {
      const card = document.createElement('div');
      card.className = 'place-card';

      const title = document.createElement('h1');
      title.textContent = place.title;

      const price = document.createElement('p');
      price.textContent = `Price per night : ${place.price}€`;

      const button = document.createElement('a');
      button.textContent = "View Details";
      button.href = `place.html?id=${place.id}`;
      button.className = "details-button";

      card.appendChild(title);
      card.appendChild(price);
      card.appendChild(button);

      placesList.appendChild(card);
      });
    } else {
      alert('Failed to fetch places')
    }
    }
    fetchPlaces();

  }
  //Place.html
  const placePage = document.getElementById('place-details');

  if (placePage) {
    const params = new URLSearchParams(window.location.search);
    const placeId = params.get('id');
    const addReviewLink = document.getElementById('add-review-link');
    if (addReviewLink) {
      addReviewLink.href = `add_review.html?id=${placeId}`; 
    }

    async function fetchPlace() {
    const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`);

    if (response.ok) {
      const data = await response.json();

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

      placePage.appendChild(title);
      placePage.appendChild(price);
      placePage.appendChild(description);
      placePage.appendChild(latitude);
      placePage.appendChild(longitude);

    } else {
        alert('Failed to fetch place');
    }
    }
    fetchPlace();
  }

  //Add-review
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
      headers: { 'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`},
      body: JSON.stringify({
        text: comment,
        rating: rating,
        place_id: placeId
      })
    });

      if (response.ok) {
        window.location.href = `place.html?id=${placeId}`;
      } else {
        const errorData = await response.json();
        alert(errorData.error);
      }
    });
  }
  }
})