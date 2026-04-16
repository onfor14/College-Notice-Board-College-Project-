// notices.js — Shared logic for loading and rendering notices

// Category color mapping
const categoryColors = {
  'exam': '#e74c3c',
  'event': '#8e44ad',
  'library': '#16a085',
  'sports': '#d35400',
  'general': '#2980b9',
};

function getCategoryColor(cat) {
  return categoryColors[(cat || "").toLowerCase()] || '#555f7e';
}

// 🔷 LOAD NOTICES
async function loadNotices() {
  const container = document.getElementById('noticeList');

  try {
    const res = await fetch('http://127.0.0.1:5000/notices', {
      method: 'GET',
      credentials: 'include'
    });

    const notices = await res.json();

    if (!notices.length) {
      container.innerHTML = '<p class="loading-text">No notices yet.</p>';
      return;
    }

    container.innerHTML = notices.map(n => `
      <div class="notice-card">
        <div class="notice-card-top">
          <span class="notice-category" style="background:${getCategoryColor(n.category)}">${n.category}</span>
          <span class="notice-date">Added: ${n.date_added}</span>
        </div>
        <h3 class="notice-title">${n.title}</h3>
        <p class="notice-desc">${n.description}</p>
        <div class="notice-footer">
          <span class="last-date">⏳ Last Date: <b>${n.last_date}</b></span>
        </div>
      </div>
    `).join('');

  } catch (err) {
    console.error("Error loading notices:", err);
    container.innerHTML = "<p>Error loading notices</p>";
  }
}

// 🔷 LOGIN FUNCTION (IMPORTANT FIX)
async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  console.log("Login clicked");

  try {
    const res = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      credentials: "include",
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    console.log(data);

    if (data.success) {
      if (data.role === "admin") {
        window.location.href = "admin.html";
      } else {
        window.location.href = "student.html";
      }
    } else {
      alert(data.message || "Login failed");
    }

  } catch (err) {
    console.error(err);
    alert("Server error");
  }
}