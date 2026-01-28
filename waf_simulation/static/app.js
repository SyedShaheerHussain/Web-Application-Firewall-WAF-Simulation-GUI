async function sendTest() {
const payload = document.getElementById('payload').value;
const res = await fetch('/test', {
method: 'POST',
headers: {'Content-Type': 'application/json'},
body: JSON.stringify({payload})
});
const data = await res.json();
document.getElementById('result').innerText = data.result;
}