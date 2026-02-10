// const API_BASE = "http://127.0.0.1:8000";

// function addUserMessage(text) {
//   const chat = document.getElementById("chat");
//   chat.innerHTML += `<div class="msg-user">🧑 You: ${text}</div>`;
//   chat.scrollTop = chat.scrollHeight;
// }

// function addAgentMessage(text) {
//   const chat = document.getElementById("chat");
//   chat.innerHTML += `<div class="msg-agent">🤖 Agent:\n${text}</div>`;
//   chat.scrollTop = chat.scrollHeight;
// }

// async function send() {
//   const input = document.getElementById("msg");
//   const msg = input.value.trim();
//   if (!msg) return;

//   addUserMessage(msg);
//   input.value = "";

//   try {
//     const res = await fetch(`${API_BASE}/agent/chat`, {
//       method: "POST",
//       headers: {"Content-Type": "application/json"},
//       body: JSON.stringify({ message: msg })
//     });

//     if (!res.ok) {
//       addAgentMessage("Error: Backend not reachable.");
//       return;
//     }

//     const data = await res.json();
//     addAgentMessage(data.response || JSON.stringify(data, null, 2));

//   } catch (err) {
//     addAgentMessage("Connection error. Is backend running?");
//   }
// }


// 🔗 LIVE BACKEND (Render)
const API_BASE = "https://skylark-ops-ai-agent.onrender.com";

function addUserMessage(text) {
  const chat = document.getElementById("chat");
  chat.innerHTML += `<div class="msg-user">🧑 You: ${text}</div>`;
  chat.scrollTop = chat.scrollHeight;
}

function addAgentMessage(text) {
  const chat = document.getElementById("chat");
  chat.innerHTML += `<div class="msg-agent">🤖 Agent:\n<pre>${text}</pre></div>`;
  chat.scrollTop = chat.scrollHeight;
}

async function send() {
  const input = document.getElementById("msg");
  const msg = input.value.trim();
  if (!msg) return;

  addUserMessage(msg);
  input.value = "";

  try {
    const res = await fetch(`${API_BASE}/agent/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg })
    });

    if (!res.ok) {
      addAgentMessage("❌ Backend error. Please try again.");
      return;
    }

    const data = await res.json();

    // Handle both formats safely
    const output =
      data.response ||
      data.message ||
      JSON.stringify(data, null, 2);

    addAgentMessage(output);

  } catch (err) {
    addAgentMessage("⚠️ Connection error. Backend may be sleeping (Render free tier). Try again in 10 seconds.");
  }
}
