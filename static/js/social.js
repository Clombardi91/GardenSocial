let dataDiv = document.querySelector("#search-data")
let button = document.querySelector("#search-button")
let weatherURL = 'https://api.openweathermap.org/data/2.5/weather?q=Mebane,North Carolina&appid=27f7ac7950d6b41f650c9d0e32b7afc7'

button.addEventListener('click', (event) => {
    fetch(weatherURL)
    .then(response => {
        return response.json()
    })
    .then(data => {
        let text = document.createElement('p')
        text.innerText = `The temperature is ${Math.round((data.main.temp - 273.5) * 9/5 + 32)}`
        dataDiv.appendChild(text)
    })
})