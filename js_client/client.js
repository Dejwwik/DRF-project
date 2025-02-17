const loginForm = document.getElementById("login-form")
const searchForm = document.getElementById("search-form")
const baseEndpoint = "http://localhost:8000/api"
const contentContainer = document.getElementById("content-container")

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}
if (searchForm) {
    searchForm.addEventListener('submit', handleSearch)
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

function handleSearch(event) {
    event.preventDefault()

    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)
    const endpoint = baseEndpoint + "/search/?" + searchParams
    const headers = {
        "Content-Type": "application/json",
    }
    const authToken = localStorage.getItem("access")
    if (authToken){
        headers["Authorization"] = "Bearer" + authToken
    }

    const options = {
        method: "GET",
        headers: headers
    }
    fetch(endpoint, options).then(response => {
        return response.json()
    }).then(data => {
        console.log(data.hits)
        writeToContainer(data)
    }).catch(err => {
        console.log('error', err)
    })
}

function writeToContainer(data){
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function getFetchOptions(method, body) {
    const options = {
        method: method || "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem("access")
        }
    };

    if (body && method !== "GET") {
        options.body = JSON.stringify(body);
    }

    return options;
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
