// Open whatsapp web
// Open user's chat window which you want to spam and type your msg(hi) in chat window, that will get repeated 5 times
// Open developer options by pressing F12 or clicking inspect
// Copy paste below code in console tab and press Enter, it will send "hi" message 5 time

function dispatch(input, message) {
	InputEvent = Event || InputEvent;
	var evt = new InputEvent('input', {						
	bubbles: true,
	composer: true
	});
	input.innerHTML = message;								
	input.dispatchEvent(evt);								
	document.querySelector("button > span").click(); 			
}

function spam(){
	var text = "hi";       
	var input = document.querySelector("#main > footer > div._2lSWV._3cjY2.copyable-area > div > span:nth-child(2) > div > div._1VZX7 > div._3Uu1_");
	var counter = 1; 											
	while(counter <= 5){									
		dispatch(input, text); 								
		counter++;
	}
}

spam()
