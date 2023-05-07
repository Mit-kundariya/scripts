// Open whatsapp web
// Open user's chat window which you want to spam 
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
	document.querySelector("button._35EW6 > span").click(); 			
}

function spam(){
	var text = "hi";       
	var input = document.querySelector("#main > footer > div._3pkkz > div._1Plpp > div._3F6QL > div._2S1VP");
	var counter = 1; 											
	while(counter <= 5){									
		dispatch(input, text); 								
		counter++;
	}
}

spam()
