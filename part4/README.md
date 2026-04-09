# HBnB Frontend Application

## 📋 Overview

Part4 is a complete frontend web application for the HBnB platform (AirBnB clone). It allows users to browse property listings, view details, and leave reviews. The interface communicates with the HBnB REST API through asynchronous `fetch` requests.

## 🎯 Main Features

### 1. **Authentication**
- Login page with email and password
- JWT token management via cookies
- Redirect to login page if not authenticated
- Secure token storage in browser cookies

### 2. **Place List**
- Dynamic display of all available places
- Card for each place showing title and price
- Price filtering system (optional)
- Direct access link to each place's details

### 3. **Place Details**
- Complete information: title, description, price, GPS coordinates
- List of associated amenities
- Reviews section with star ratings
- Link to add a new review

### 4. **Review System**
- Add reviews with text and rating (1-5 stars)
- Display existing reviews with visual rating
- Authentication validation before adding a review
- Automatic redirect after submission

### 5. **Responsive Design**
- Responsive interface (mobile-first)
- Consistent styling with CSS variables
- Intuitive and modern navigation

## 📁 File Structure

```
part4/
├── index.html              # Homepage with places list
├── login.html              # Login page
├── place.html              # Specific place details
├── add_review.html         # Review submission form
├── scripts.js              # JavaScript logic and API calls
├── styles.css              # CSS styles with variables
├── images/                 # Folder for graphic resources
│   ├── logo.png           # Application logo
│   ├── appartment.png     # Apartment property image
│   ├── cosy.png           # Cozy apartment image
│   ├── loft.png           # Loft property image
│   └── studio.png         # Studio apartment image
└── README.md              # Project documentation
```

## 🛠️ Technologies Used

- **HTML5**: Semantic page structure
- **CSS3**: Styling with CSS variables, flexbox, and animations
- **JavaScript (ES6+)**: Event handling, async/await, DOM manipulation
- **REST API**: Communication with HBnB backend via `fetch`
- **JWT**: Token-based authentication

## 🚀 Quick Start

### Prerequisites

1. **HBnB backend running** on `http://127.0.0.1:5000`
2. **Modern web browser** with ES6 and Fetch API support
3. **Local HTTP server** (optional for development)

### Installation and Commands to Run

#### Step 1: Start the HBnB Backend

In a terminal, navigate to the backend folder and launch the Flask application:

```bash
cd part3/hbnb
python3 run.py
```

The backend will start on `http://127.0.0.1:5000`

#### Step 2: Create Test Data via API

In another terminal (with backend running), create data via the API:

**1. Create an admin user (one time only):**

```bash
# Create the admin user
sqlite3 part3/hbnb/development.db <<EOF
INSERT INTO users (id, first_name, last_name, email, password, is_admin, created_at, updated_at) 
VALUES (
  'admin-001',
  'Admin',
  'User',
  'admin@example.com',
  '\$2b\$12\$O9h2iHhYz.1sSNVF0/K1O.V9QeIS5KlsNQursTQy24gpl/DQK7umm',
  1,
  datetime('now'),
  datetime('now')
);
EOF
```

> Note: The hashed password corresponds to "admin123". You can modify the email and password as needed.

**2. Login to get a token:**

```bash
curl -X POST http://127.0.0.1:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@example.com", "password": "admin123"}' | jq -r '.access_token'
```

Note the JWT token returned (we'll use it as `TOKEN` in the following commands).

**3. Create amenities:**

```bash
# Replace TOKEN with the token obtained above
TOKEN="your_token_here"

curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "WiFi"}' | jq

curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Air Conditioning"}' | jq

curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Parking"}' | jq

curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Swimming Pool"}' | jq
```

**4. Create an owner user (with admin token):**

```bash
TOKEN="your_token_here"

curl -X POST http://127.0.0.1:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "password123"
  }' | jq '.id'
```

Note the owner's ID (USER_ID).

**5. Create places (with owner token):**

First, login with the owner account:

```bash
curl -X POST http://127.0.0.1:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "john.doe@example.com", "password": "password123"}' | jq -r '.access_token'
```

Then use this token to create places:

```bash
TOKEN="owner_token"

curl -X POST http://127.0.0.1:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "title": "Cozy apartment downtown",
    "description": "Charming apartment with a view of the main square.",
    "price": 79.99,
    "latitude": 48.8566,
    "longitude": 2.3522,
    "amenities": []
  }' | jq

curl -X POST http://127.0.0.1:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "title": "Modern loft near the park",
    "description": "Large bright loft, ideal for a family weekend.",
    "price": 120.00,
    "latitude": 48.8638,
    "longitude": 2.3499,
    "amenities": []
  }' | jq

curl -X POST http://127.0.0.1:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "title": "Quiet studio by the river",
    "description": "Cozy studio, perfect for solo travelers.",
    "price": 55.50,
    "latitude": 48.8606,
    "longitude": 2.3376,
    "amenities": []
  }' | jq
```

#### Step 3: Serve the Frontend

In a third terminal, navigate to the frontend folder:

```bash
cd part4
```

Launch a local HTTP server:

**Option 1 - With Python 3:**
```bash
python3 -m http.server 8000
```

**Option 2 - With Node.js:**
```bash
npx http-server
```

**Option 3 - With Node.js (locally installed http-server):**
```bash
http-server -p 8000
```

#### Step 4: Access the Application

Open your browser and navigate to:
- `http://localhost:8000`

#### Summary of Commands (3 Different Terminals)

**Terminal 1 - Flask Backend:**
```bash
cd part3/hbnb && python3 run.py
```

**Terminal 2 - Create Data (from part3/hbnb):**
```bash
# 1. Create the admin user
sqlite3 development.db <<EOF
INSERT INTO users (id, first_name, last_name, email, password, is_admin, created_at, updated_at) 
VALUES ('admin-001', 'Admin', 'User', 'admin@example.com', '\$2b\$12\$O9h2iHhYz.1sSNVF0/K1O.V9QeIS5KlsNQursTQy24gpl/DQK7umm', 1, datetime('now'), datetime('now'));
EOF

# 2. Login and retrieve the token
TOKEN=$(curl -s -X POST http://127.0.0.1:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@example.com", "password": "admin123"}' | jq -r '.access_token')

# 3. Create amenities
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "WiFi"}' | jq

# 4. Create an owner user
USER_ID=$(curl -s -X POST http://127.0.0.1:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "password": "password123"}' | jq -r '.id')

# 5. Login with the owner and create places
OWNER_TOKEN=$(curl -s -X POST http://127.0.0.1:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "john.doe@example.com", "password": "password123"}' | jq -r '.access_token')

curl -X POST http://127.0.0.1:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OWNER_TOKEN" \
  -d '{"title": "Cozy apartment", "price": 79.99, "latitude": 48.8566, "longitude": 2.3522, "amenities": []}' | jq
```

**Terminal 3 - Frontend:**
```bash
cd part4 && python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## 📄 Page Descriptions

### 📍 index.html
**Homepage - Places List**
- Display all places with graphic cards
- Advanced price filter search
- Navigation to each place's details
- Login link in the header

### 🔐 login.html
**Authentication Page**
- Login form (email + password)
- Send credentials to `/api/v1/auth/login`
- Store JWT token in cookies
- Redirect to homepage after successful login

### 🏠 place.html
**Place Details**
- Fetch place ID from URL parameters (`?id=`)
- Display all place information
- List associated amenities
- Display existing reviews with rating
- Button to add a new review

### ⭐ add_review.html
**Review Submission Form**
- Fields: review text + rating (1-5 stars)
- Fetch place ID from URL
- Submit review to `/api/v1/reviews/`
- Redirect to place after success

## 🔌 API Integration

### Used Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/login` | User authentication |
| GET | `/api/v1/places/` | Get all places |
| GET | `/api/v1/places/{id}` | Get place details |
| GET | `/api/v1/places/{id}/reviews/` | Get place reviews |
| POST | `/api/v1/reviews/` | Create a new review |

### Required Headers

```javascript
// Authentication
Authorization: Bearer {token}
Content-Type: application/json
```

## 🎨 Color Palette

The design uses custom CSS variables (see `styles.css`):

| Variable | Color | Usage |
|----------|-------|-------|
| `--pink-600` | #b85a7a | Main accent color |
| `--pink-800` | #7a2f4d | Dark color/text |
| `--bg` | #fdf2f6 | Main background |
| `--surface` | #ffffff | Content surfaces |
| `--text` | #3a2030 | Main text |

## 🔧 Main JavaScript Functions

### `getCookie(name)`
Retrieves a cookie value by its name.

### `fetchPlaces()`
Fetches and displays all places with card creation.

### `fetchPlaceDetails()`
Fetches and displays complete place information.

### `fetchReviews(placeId)`
Fetches and displays reviews for a given place.

### Event Handling
- Login: form submission → API call `/auth/login`
- Add review: form submission → API call `/reviews/`

## ⚠️ Error Handling

- **Authentication error**: Redirect to login page
- **Fetch error**: User alert messages
- **Invalid/expired token**: Delete cookie and redirect

## 📌 Important Notes

1. **CORS**: The backend API must accept CORS requests from the frontend origin
2. **Token expiration**: JWT tokens should be managed on the backend
3. **HTTP Protocol**: Requests use `http://127.0.0.1:5000` - adapt for production
4. **Cookies**: Cookies store the token (SameSite, Secure to configure for production)

## 🔐 Security Recommendations

For production:

1. **HTTPS mandatory**: Replace `http://` with `https://`
2. **Secure cookie flags**:
   ```javascript
   document.cookie = `token=${token}; path=/; secure; samesite=strict`;
   ```
3. **Content Security Policy (CSP)**: Add CSP headers
4. **Client-side validation**: Validate all user inputs
5. **Restrictive CORS**: Limit authorized origins

## 🧪 Manual Testing

### Complete Flow Test

1. **Open the homepage**
   - ✓ Places list displays
   - ✓ See cards with title and price

2. **Click "View Details"**
   - ✓ Redirect to place.html with correct ID
   - ✓ Full details displayed

3. **Add review without authentication**
   - ✓ Redirect to login.html

4. **Authenticate**
   - ✓ Email and password accepted
   - ✓ Token created and stored
   - ✓ Redirect to index.html

5. **Add a review**
   - ✓ Form is accessible
   - ✓ Submission successful
   - ✓ Review appears in list



---
 
**Last Updated**: April 2026  
**Author**: Adele MEGELINK
