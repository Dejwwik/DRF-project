const loginForm = document.getElementById("login-form")
const baseEndpoint = "http://localhost:8000/api"
const contentContainer = document.getElementById("content-container")
if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    const options = {
        method: "POST",
        headers : {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(loginObjectData),
    }
    fetch(loginEndpoint, options).then(response => {
        return response.json()
    }).then(authData => {
        handleAuthData(authData, getProductList)
    }).catch(err => {
        console.log('error', err)
    })
}

function writeToContainer(data){
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function getFetchOptions(method, body){
    return {
        method: method === null ? "GET" : method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("access")}`
        },
        body: body ? body : null
    }
}

function handleAuthData(authData, callback) {
    localStorage.setItem("access", authData.access)
    localStorage.setItem("refresh", authData.refresh)
    if (callback){
        callback()
    }
}

function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptions()
    fetch(endpoint, options)
        .then(response => response.json())
        .then(data => writeToContainer(data))
}
