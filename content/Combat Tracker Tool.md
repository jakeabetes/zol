---
title: "Combat Tracker Tool"
---

  <div>
    <style>
      h2 {
        font-family: Verdana, sans-serif;
      }

      .action-label {
        font-family: Verdana, sans-serif;
        font-weight: bold;
        margin-left: 1rem;
        position: relative;
        top: 0.4rem;
      }

      .valuebar-label {
        font-family: Verdana, sans-serif;
        font-weight: bold;
      }

      .valuebar-numeric-value {
        font-family: Verdana, sans-serif;
        font-weight: bold;
        font-size: 0.9rem;
      }

      .switch {
        position: relative;
        display: inline-block;
        width: 60px;
        height: 34px;
      }

      .switch input { 
        opacity: 0;
        width: 0;
        height: 0;
      }

      .slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #ccc;
        -webkit-transition: .4s;
        transition: .4s;
      }

      .slider:before {
        position: absolute;
        content: "";
        height: 26px;
        width: 26px;
        left: 4px;
        bottom: 4px;
        background-color: white;
        -webkit-transition: .4s;
        transition: .4s;
      }

      input:checked + .slider {
        background-color: #cc3333;
      }

      input:not(:checked) + .slider {
        background-color: #66cc33;
      }


      input:focus + .slider {
        box-shadow: 0 0 1px #2196F3;
      }

      input:checked + .slider:before {
        -webkit-transform: translateX(26px);
        -ms-transform: translateX(26px);
        transform: translateX(26px);
      }

      /* Rounded sliders */
      .slider.round {
        border-radius: 34px;
      }

      .slider.round:before {
        border-radius: 50%;
      }

      /*valuebar*/
      .valuebarcontainer {
        margin-top: 1rem;
      }
      .valuebar {
        --SliderColor: hsl(100, 60%, 50%);
        -webkit-appearance: none;
        width: 40%;
        height: 8px;
        margin-top: 0.7rem;
        border-radius: 4px;
        margin-bottom: 15px;
        background-color: rgb(200, 200, 200);
      }

      /* --------------------------- webkit browsers */
      .valuebar::-webkit-slider-thumb {
        -webkit-appearance: none;
        width: 18px;
        height: 18px;
        border-radius: 10px;
        background-color: var(--SliderColor);
        overflow: visible;
        cursor: pointer;
      }
      /* -------------------------- Firefox */
      .valuebar::-moz-range-thumb { 
        -moz-appearance: none;
        width: 18px;
        height: 18px;
        border-radius: 10px;
        background-color: var(--SliderColor);
        overflow: visible;
        cursor: pointer;
      }
      .valuebar::-moz-focus-outer { border: 0; }
      /* Remove dotted outline from range input element focused in Firefox */

      /* Next Round Button */
      .next-round {
        width: 40%;
      }

      #next-round-button {
        float: right;
      }

      #next-round-icon {
        stroke: #66cc33;
        -webkit-transition: .4s;
        transition: .4s;
        cursor: pointer;
      }

      #next-round-icon:hover {
        stroke: #cc3333;
        -webkit-transition: .4s;
        transition: .4s;
      }

      /* Strikethrough */
      @keyframes strike{
        0%   { width : 0; }
        100% { width: 100%; }
      }
      .strike {
        position: relative;
      }
      .strike::after {
        content: ' ';
        position: absolute;
        top: 50%;
        left: 0;
        width: 100%;
        height: 2px;
        background: black;
        animation-name: strike;
        animation-duration: 0.4s;
        animation-timing-function: linear;
        animation-iteration-count: 1;
        animation-fill-mode: forwards; 
      }
      
      @keyframes unstrike{
        0%   { width : 100%; }
        100% { width: 0; }
      }
      .unstrike {
        position: relative;
      }
      .unstrike::after {
        content: ' ';
        position: absolute;
        top: 50%;
        left: 0;
        width: 100%;
        height: 2px;
        background: black;
        animation-name: unstrike;
        animation-duration: 0.4s;
        animation-timing-function: linear;
        animation-iteration-count: 1;
        animation-fill-mode: forwards; 
      }
    </style>
    <div>
      <h2>TURN TRACKER</h2>

      <div class="next-round">
        <div id="next-round-button">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#66cc33" id="next-round-icon" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-swords"><polyline points="14.5 17.5 3 6 3 3 6 3 17.5 14.5"/><line x1="13" x2="19" y1="19" y2="13"/><line x1="16" x2="20" y1="16" y2="20"/><line x1="19" x2="21" y1="21" y2="19"/><polyline points="14.5 6.5 18 3 21 3 21 6 17.5 9.5"/><line x1="5" x2="9" y1="14" y2="18"/><line x1="7" x2="4" y1="17" y2="20"/><line x1="3" x2="5" y1="19" y2="21"/></svg>
        </div>
      </div>

      <div>
        <label class="switch">
          <input type="checkbox" id="action-switch">
          <span class="slider round"></span>
        </label>
        <span id="action-label" class="action-label">ACTION</span>
      </div>

      <div>
        <label class="switch">
          <input type="checkbox" id="bonus-action-switch">
          <span class="slider round"></span>
        </label>
        <span id="bonus-action-label" class="action-label">BONUS ACTION</span>
      </div>

      <div>
        <label class="switch">
          <input type="checkbox" id="reaction-switch">
          <span class="slider round"></span>
        </label>
        <span id="reaction-label" class="action-label">REACTION</span>
      </div>

      <div>
        <div class="valuebarcontainer">
          <span class="valuebar-label">MOVEMENT</span>
          <div class="valuebar-wrapper">
            <input type="range" min="0" max="20" value="20" class="valuebar" name="value-range" id="movement-slider">
          </div>
          <span class="valuebar-numeric-value" id="valuebar-numeric-value"></span>
        </div>
      </div>
    </div>
    <script>
    	// get switches
      const actionSwitch = document.getElementById("action-switch");
      const bonusActionSwitch = document.getElementById("bonus-action-switch");
      const reactionSwitch = document.getElementById("reaction-switch");
      const actionSwitchLabel = document.getElementById("action-label");
      const bonusActionSwitchLabel = document.getElementById("bonus-action-label");
      const reactionSwitchLabel = document.getElementById("reaction-label");
      
      // get slider
      const movementSlider = document.getElementById("movement-slider");
      const numericDisplay = document.getElementById("valuebar-numeric-value");
      const movmentSliderColor = document.querySelector('input[name=value-range]');    
      
      // get next round button
      const nextRoundButton = document.getElementById("next-round-button");

			const actionLabelUpdate = function() {
      	if (actionSwitch.checked){
        	actionSwitchLabel.classList.add("strike");
        	actionSwitchLabel.classList.remove("unstrike");
        } else {
        	actionSwitchLabel.classList.remove("strike");
        	actionSwitchLabel.classList.add("unstrike");
        }
      }
      
      const bonusActionLabelUpdate = function() {
      	if (bonusActionSwitch.checked){
        	bonusActionSwitchLabel.classList.add("strike");
        	bonusActionSwitchLabel.classList.remove("unstrike");
        } else {
        	bonusActionSwitchLabel.classList.remove("strike");
        	bonusActionSwitchLabel.classList.add("unstrike");
        }
      }
      
      const reactionLabelUpdate = function() {
      	if (reactionSwitch.checked){
        	reactionSwitchLabel.classList.add("strike");
        	reactionSwitchLabel.classList.remove("unstrike");
        } else {
        	reactionSwitchLabel.classList.remove("strike");
        	reactionSwitchLabel.classList.add("unstrike");
        }
      }

      nextRoundButton.onclick = function() {    
        // reset switches
        if (actionSwitch.checked) {
          actionSwitch.checked = false;
          actionLabelUpdate();
        }

        if (bonusActionSwitch.checked) {
          bonusActionSwitch.checked = false;
          bonusActionLabelUpdate();
        }

        if (reactionSwitch.checked) {
          reactionSwitch.checked = false;
          reactionLabelUpdate();
        }

        movementSlider.value = 20;
        numericDisplay.innerHTML = 100  + "%";
        movmentSliderColor.style.setProperty('--SliderColor', `hsl(100, 60%, 50%)`);
      }
      
      actionSwitch.onchange = actionLabelUpdate;
      bonusActionSwitch.onchange = bonusActionLabelUpdate;
      reactionSwitch.onchange = reactionLabelUpdate;
    </script>

    <script>
      // handle value slider color
      const slider = document.querySelector('input[name=value-range]');    
      const numericSliderDisplay = document.getElementById("valuebar-numeric-value");
      numericSliderDisplay.innerHTML = slider.value*5 + "%"; // Display the default slider value

      // Update the current slider value (each time you drag the slider handle)
			const updateSlider = function() {
        slider.style.setProperty('--SliderColor', `hsl(${slider.value*5}, 60%, 50%)`);
        numericSliderDisplay.innerHTML = this.value*5  + "%";
      }

      slider.oninput = updateSlider;
      slider.onchange = updateSlider;
    </script>
  </div>

*This is a tool to be used by players during Simultaneous Initiative Combat. An alternate-rule form of combat where all players take their turns at the same time. Since that has potential to get confusing, this tool allows players to track their action economy used each round.*
