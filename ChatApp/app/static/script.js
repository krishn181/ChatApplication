const group = JSON.parse(document.getElementById("group_name").textContent)

const ws = new WebSocket("ws://" +
    window.location.host +
    "/ws/sws/" +
    group +
    "/")

ws.onopen = function () {
    console.log("Connecting to server.....")
}

ws.onmessage = function (event) {
    console.log("Message from server...", event)
    console.log("message .....", event.data)
    const data = JSON.parse(event.data)
    document.getElementById("chat-container").value += data.msg + "\n"

}
ws.onclose = function () {
    console.log("Close Connection....")
}
document.getElementById("submit-text").onclick = function () {
    const messageDom = document.getElementById("message-field")
    const message = messageDom.value
    ws.send(JSON.stringify({ 'msg': message }));
    messageDom.value = ''
}