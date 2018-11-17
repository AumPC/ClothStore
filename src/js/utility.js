const CONTAINER = document.getElementById('main-container');

function handleError(error) {
    console.log('navigator.getUserMedia error: ', error);
  }
  
  function clear () {
    var contains = document.getElementById('main-container');
    while (contains.firstChild) {
      contains.removeChild(contains.firstChild);
    }
  }
  
  function createTag (tagName, className = '', parent = undefined) {
    var tag = document.createElement(tagName);
  
    if (className) {
      tag.className = className;
    }
  
    if (parent) {
      parent.appendChild(tag);
    } else {
      CONTAINER.append(tag);
    }
  
    return tag;
  }
  