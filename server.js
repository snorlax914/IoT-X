const express = require('express')
const app = express()

app.listen(8080, function() {
    console.log('listening on 8080')
})

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html')
})

app.get('/reset.css', function(req, res) {
    res.sendFile(__dirname + '/reset.css')
})

app.get('/style.css', function(req, res) {
    res.sendFile(__dirname + '/style.css')
})

app.get('/scripts.js', function(req, res) {
    res.sendFile(__dirname + '/scripts.js')
})

app.get('/0.jpg', function(req, res) {
    res.sendFile(__dirname + '/0.jpg')
})

app.get('/1.jpg', function(req, res) {
    res.sendFile(__dirname + '/1.jpg')
})

app.get('/2.jpg', function(req, res) {
    res.sendFile(__dirname + '/2.jpg')
})

app.get('/3.jpg', function(req, res) {
    res.sendFile(__dirname + '/3.jpg')
})

app.get('/4.jpg', function(req, res) {
    res.sendFile(__dirname + '/4.jpg')
})

app.get('/5.jpg', function(req, res) {
    res.sendFile(__dirname + '/5.jpg')
})

app.get('/fire.txt', function(req, res) {
    res.sendFile(__dirname + '/fire.txt')
})