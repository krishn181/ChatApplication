# 💬 Real-Time Chat Application

A simple real-time chat application built using **Django Channels and WebSockets**.

The main purpose of this project is to understand how **WebSocket communication** works in Django and how **Django Channels' In-Memory Channel Layer** can be used to send messages between connected clients.

## 🚀 Features

* Real-time message sending using WebSockets
* Group-based communication
* Django Channels integration
* In-Memory Channel Layer
* Messages are delivered instantly to connected users in the same group
* Simple HTML, CSS and JavaScript frontend

## 🛠️ Tech Stack

* **Python**
* **Django**
* **Django Channels**
* **WebSockets**
* **InMemoryChannelLayer**
* **HTML**
* **CSS**
* **JavaScript**

## ⚙️ How It Works

The application uses a WebSocket connection between the browser and the Django server.

```text
Browser
   │
   │ WebSocket
   ▼
Django Channels
   │
   ▼
WebSocket Consumer
   │
   ▼
InMemoryChannelLayer
   │
   ▼
Chat Group
   │
   ▼
Connected Clients
```

When a user sends a message:

1. The browser sends the message through the WebSocket.
2. Django Channels receives the message.
3. The WebSocket consumer sends the message to the channel group.
4. The **InMemoryChannelLayer** broadcasts the message to connected clients in that group.
5. Users in the same group receive the message in real time.

## 🔌 WebSocket

The application uses a WebSocket route for chat communication.

Example:

```text
ws://127.0.0.1:8000/ws/sc/<group_name>/
```

For example:

```text
ws://127.0.0.1:8000/ws/sc/general/
```

Users connected to the same group can send and receive messages in real time.

## 🧠 In-Memory Channel Layer

This project uses Django Channels' **InMemoryChannelLayer**.

It allows different WebSocket connections to communicate through channel groups without requiring an external service such as Redis.

Example configuration:

```python
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
```

### Why use InMemoryChannelLayer?

It is useful for:

* Learning Django Channels
* Local development
* Testing WebSocket functionality
* Small demonstration projects

> **Note:** InMemoryChannelLayer stores channel-layer data in application memory, so it is not intended for production deployments with multiple server processes.

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/krishn181/ChatApplication.git
```

### 2. Go to the project directory

```bash
cd ChatApplication
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install django channels daphne
```

### 6. Run the server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 📚 Concepts Covered

This project focuses on learning:

* WebSockets
* Django Channels
* ASGI
* WebSocket Consumers
* Channel Groups
* InMemoryChannelLayer
* Real-time communication
* WebSocket routing
* Sending messages between connected clients

## 🔮 Future Improvements

Possible future improvements include:

* Redis Channel Layer
* User authentication
* Private messaging
* Message history
* Typing indicator
* Message timestamps

## 👨‍💻 Author

**Krishnpal Singh**

GitHub: [@krishn181](https://github.com/krishn181)

---

⭐ A simple project built to understand real-time communication using Django Channels and WebSockets.
