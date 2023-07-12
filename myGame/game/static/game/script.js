//{% csrf_token %}

let player_name = ""
let player_team = ""
let opponent_team = ""

function getInfo(){
    player_name = document.getElementById('playerName').value
    player_team = document.getElementById('playerTeam').value
    opponent_team = document.getElementById('opponentTeam').value

    if(player_team === opponent_team)
        alert(player_name + " you have selected same teams")
}

function resetInfo(){
    player_name = ""
    player_team = ""
    opponent_team = ""
    document.getElementById('playerName').value = ""
    document.getElementById('playerTeam').value = ""
    document.getElementById('opponentTeam').value = ""
}

function open_about_page(){
    let u = "/about/"
    window.open(u, "_self")
}
function sendEmail(){
    let email = 'sk21eeb0b52@student.nitw.ac.in';

    let mailtoLink = 'mailto:' + email;
    window.location.href = mailtoLink;
}

let player_won_toss = false
function toss(){
    let container = document.getElementById('toss-time')
    let existing_div = document.getElementById('head-tail-container')
    let newDiv = document.createElement("div")
    newDiv.className = "toss-outcome-div"


    let player_toss_choice = ""
    player_toss_choice = document.getElementById('head').value
    if(player_toss_choice === "")
        player_toss_choice = document.getElementById('tail').value

    let randomToss = ""
    let num = Math.floor(Math.random() * 10)
    if(num > 5)
        randomToss = "heads"
    else
        randomToss = "tails"

    if(player_toss_choice === randomToss){
          let newButtons = document.createElement("div")
          newButtons.textContent = "You won the toss, chose what to do"
          newButtons.className = "head-tail-container"

         let newButton1 = document.createElement("button")
         newButton1.textContent = "BAT"
         newButton1.className = "head"
         newButtons.appendChild(newButton1)

         let newButton2 = document.createElement("button")
         newButton2.textContent = "BOWL"
         newButton2.className = "head"
         newButtons.appendChild(newButton2)

        container.replaceChild(newButtons, existing_div)

        newButton1.addEventListener('click', function(){
            let data = {
                toss: 'player',
                bat: 'player',
            }

            alert("You won the toss and chose to bat first")
            let url = '/toss/?toss=' + encodeURIComponent(data.toss) + '&bat_first=' + encodeURIComponent(data.bat)
            window.location.href = url;
        })
        newButton2.addEventListener('click', function(){
            let data = {
                toss: 'player',
                bat: 'computer',
            }
            alert("You won the toss and chose to bowl first")
            let url = '/toss/?toss=' + encodeURIComponent(data.toss) + '&bat_first=' + encodeURIComponent(data.bat)
            window.location.href = url
        })
    }
    else{
        let comp_choice = Math.floor(Math.random() * 10)
        if(comp_choice > 5){
            let data = {
                toss: 'computer',
                bat: 'computer',
            }
            alert("Computer won the toss and chose to bat first")
            let url = '/toss/?toss=' + encodeURIComponent(data.toss) + '&bat_first=' + encodeURIComponent(data.bat)
            window.location.href = url
        }
        else{
            let data = {
                toss: 'computer',
                bat: 'player',
            }
            alert("Computer won the toss and chose to bowl first")
            let url = '/toss/?toss=' + encodeURIComponent(data.toss) + '&bat_first=' + encodeURIComponent(data.bat)
            window.location.href = url
        }
    }
}

let compInput

let first_innings_total = 0
let second_innings_total = 0

let player_won = false
let tied_game = false

let total = 0

let target = 0

//WHEN PLAYER IS BATTING FIRST
function batting_first_game_play(inp){
    compInput = Math.floor(Math.random() * 6) + 1
    if(compInput === inp){
        first_innings_total = total
        target = total + 1
        let url = '/batting_first/?target=' + encodeURIComponent(target) + '&first_innings=' + encodeURIComponent(first_innings_total)
        window.location.href = url
    }
    else{
        total += inp
        document.getElementById("score").textContent = total
    }
}
function bowling_second_game_play(inp){
    compInput = Math.floor(Math.random() * 6) + 1

    target = document.getElementById("target-tag").innerText
    console.log(compInput)

    if(compInput === inp){
        second_innings_total = total
        if(total == target-1){
            alert("Tied")
            tied_game = true;
        }
        else if(total < target){
            alert("You won")
            player_won = true;
        }
        if(tied_game){
            let url = '/bowling_second/?result=' + encodeURIComponent('tie') + '&second_innings=' + encodeURIComponent(second_innings_total)
            window.location.href = url
        }
        else if(player_won){
            let url = '/bowling_second/?result=' + encodeURIComponent('player') + '&second_innings=' + encodeURIComponent(second_innings_total)
            window.location.href = url
        }
        return
    }
    else{
        total += compInput
        document.getElementById("score").textContent = total
    }
    if(total >= target){
        second_innings_total = total
        alert("You lost the game")
        player_won = false;
        let url = '/bowling_second/?result=' + encodeURIComponent('computer') + '&second_innings=' + encodeURIComponent(second_innings_total)
        window.location.href = url
        return
    }
}

// WHEN PLAYER IS BOWLING FIRST
function bowling_first_game_play(inp){
    compInput = Math.floor(Math.random() * 6) + 1

    if(compInput === inp){
        first_innings_total = total
        target = total + 1
        let url = '/bowling_first/?target=' + encodeURIComponent(target) + '&first_innings=' + encodeURIComponent(first_innings_total)
        window.location.href = url
    }
    else{
        total += compInput
        document.getElementById("score").textContent = total
    }
}
function batting_second_game_play(inp){
    compInput = Math.floor(Math.random() * 6) + 1

    target = document.getElementById("target-tag").innerText
    console.log(compInput)

    if(compInput === inp){
        second_innings_total = total
        if(total == target-1){
            alert("Tied")
            tied_game = true;
        }
        else if(total < target){
            alert("lost")
            player_won = false;
        }
        if(tied_game){
            let url = '/batting_second/?result=' + encodeURIComponent('tie') + '&second_innings=' + encodeURIComponent(second_innings_total)
            window.location.href = url
        }
        else if(!player_won){
            let url = '/batting_second/?result=' + encodeURIComponent('computer') + '&second_innings=' + encodeURIComponent(second_innings_total)
            window.location.href = url
        }
        return
    }
    else{
        total += inp
        document.getElementById("score").textContent = total
    }
    if(total >= target){
        second_innings_total = total
        alert("You won the game")
        player_won = true;
        let url = '/bowling_second/?result=' + encodeURIComponent('player') + '&second_innings=' + encodeURIComponent(second_innings_total)
        window.location.href = url
        return
    }
}