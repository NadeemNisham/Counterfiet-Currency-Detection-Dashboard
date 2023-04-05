const identifyDiv = document.getElementById('identify-des');
const classifyDiv = document.getElementById('classify-des');
const sumUpDiv = document.getElementById('summing-des');
const desDiv = document.getElementById('home-des');

const identifyLink = document.getElementById('identify');
const classifyLink = document.getElementById('classify');
const sumUpLink = document.getElementById('summing');

identifyLink.addEventListener('mouseover', function() {
  desDiv.classList.remove('active');
  identifyDiv.classList.add('active');
})

identifyLink.addEventListener('mouseout', function() {
  identifyDiv.classList.remove('active');
  desDiv.classList.add('active');
})

classifyLink.addEventListener('mouseover', function() {
  desDiv.classList.remove('active');
  classifyDiv.classList.add('active');
})

classifyLink.addEventListener('mouseout', function() {
  classifyDiv.classList.remove('active');
  desDiv.classList.add('active');
})

sumUpLink.addEventListener('mouseover', function() {
  desDiv.classList.remove('active');
  sumUpDiv.classList.add('active');
})

sumUpLink.addEventListener('mouseout', function() {
  sumUpDiv.classList.remove('active');
  desDiv.classList.add('active');
})