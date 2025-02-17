const loginForm = document.getElementById("login-form")
const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}


function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    const options = {
        method: "POST",
        headers : {
            ContentType: "application/json",
        },
        body: JSON.stringify(loginObjectData),
    }
    fetch(loginEndpoint, options).then(response => {
        console.log(response.body)
        return response.json()
    }).then(x => {
        console.log(x)
    }).catch(err => {
        console.log('error', err)
    })
}
