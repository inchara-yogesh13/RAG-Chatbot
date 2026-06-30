async function sendMessage() {

    const input = document.getElementById("messageInput");
    const messages = document.getElementById("messages");

    const text = input.value.trim();

    if(text==="") return;

    // Show user's message
    messages.innerHTML += `
        <div class="user">
            <p>${text}</p>
        </div>
    `;

    input.value="";

    // Send request to backend
    const response = await fetch("http://127.0.0.1:8000/chat",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:text
        })
    });

    const data = await response.json();

    // Show bot reply
    messages.innerHTML += `
        <div class="bot">
            <p>${data.reply}</p>
        </div>
    `;

    // Scroll to bottom
    messages.scrollTop = messages.scrollHeight;
}
document.getElementById("messageInput")
.addEventListener("keypress", function(event){

    if(event.key==="Enter"){
        sendMessage();
    }

});