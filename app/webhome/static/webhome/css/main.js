// Select elements
const btnBot = document.querySelector('.bot');
const btnClose = document.querySelector('.close');
const chatBotDiv = document.querySelector('.chatBot');

// Add buttons event listeners
// Open var
let open = false;

btnBot.onclick = ()=>{
    if(!open){
        chatBotDiv.style.display = 'block';
        btnBot.style.bottom = '94px';
        btnBot.style.right = '247px';
        btnBot.style.width = '33px';
        btnBot.style.zIndex = '1';
        // Change var value to true
        open = true;
    }else{
        chatBotDiv.style.display = 'none';
        btnBot.style.bottom = '10px';
        btnBot.style.right = '10px';
        btnBot.style.width = '50px';
        open = false;
    }
}

btnClose.onclick = ()=>{
    chatBotDiv.style.display = 'none';
    btnBot.style.bottom = '10px';
    btnBot.style.right = '10px';
    btnBot.style.width = '50px';
    open = false;
}