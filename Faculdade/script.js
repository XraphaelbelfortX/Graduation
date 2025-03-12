const socket = new WebSocket('ws://192.168.249.52:3000');

socket.onopen = () => {
    console.log('Conectando ao servidor WebSocket.');

};

socket.onmessage = (event) => {
    document.getElementById('resposta').innerHTML += `<p>${event.data}</p>`;

};

socket.onerror = (error) => {
    console.error('Erro no WebSocket:', error);
};

socket.onclose = () => {
    console.log('Conexão encerrada.');
};

function enviarMensagem() {
    const mensagem = document.getElementById('mensagem').value;
    if (mensagem.trin() !== "") {
        socket.send(mensagem);
        document.getElementById('mensagem').value = "";
    }
}
