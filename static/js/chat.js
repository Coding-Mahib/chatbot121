// chat.js

document.addEventListener("DOMContentLoaded", function () {
    const messageContainer = document.querySelector(".chat-messages");
    const userMessageInput = document.querySelector("#user-message");
    const sendButton = document.querySelector("#send-button");

    // Function to append a new message to the chat interface
    function appendMessage(message, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        messageDiv.innerHTML = `<div class="message-content"><p>${message}</p></div>`;
        messageContainer.appendChild(messageDiv);
        messageContainer.scrollTop = messageContainer.scrollHeight; // Scroll to the latest message
    }

    // Event listener for sending a message
    sendButton.addEventListener("click", function () {
        const userMessage = userMessageInput.value;
        if (userMessage.trim() === "") return; // Don't send empty messages

        // Append the user's message to the chat
        appendMessage(userMessage, "sent");

        // Send the message to the server (you need to implement this)
        let xhr = new XMLHttpRequest()
        xhr.onreadystatechange = function(){
        	if(this.readyState === 4 && this.status === 200){
        		let msg = this.responseText;
        		appendMessage(msg, "received");
        	}
        }
        xhr.open('POST', '/api/');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send('text='+userMessage);

        // Clear the input field
        userMessageInput.value = "";
    });
});
