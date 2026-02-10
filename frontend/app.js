// async function send() {
//   const msg = document.getElementById("msg").value;

//   const res = await fetch("/agent/chat", {
//     method: "POST",
//     headers: {"Content-Type": "application/json"},
//     body: JSON.stringify({message: msg})
//   });

//   const data = await res.json();
//   document.getElementById("chat").innerHTML +=
//     `<pre>${JSON.stringify(data, null, 2)}</pre>`;
// }

const API_BASE = "http://127.0.0.1:8000";

function addUserMessage(text) {
  const chat = document.getElementById("chat");
  chat.innerHTML += `<div class="msg-user">🧑 You: ${text}</div>`;
  chat.scrollTop = chat.scrollHeight;
}

function addAgentMessage(text) {
  const chat = document.getElementById("chat");
  chat.innerHTML += `<div class="msg-agent">🤖 Agent:\n${text}</div>`;
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
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ message: msg })
    });

    if (!res.ok) {
      addAgentMessage("Error: Backend not reachable.");
      return;
    }

    const data = await res.json();
    addAgentMessage(data.response || JSON.stringify(data, null, 2));

  } catch (err) {
    addAgentMessage("Connection error. Is backend running?");
  }
}
