'use strict'

const CONTAINER = document.getElementById('main-container');

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

function createProgressBar () {
  var container = createTag('div', 'text-center container');

  var div = createTag('div', 'step-container', container);
  var ul = createTag('ul', 'progressbar', div);

  var li = createTag('li', 'active', ul);
  li.innerHTML = 'Snap';

  var li = createTag('li', '', ul);
  li.innerHTML = 'Sign';

  var li = createTag('li', '', ul);
  li.innerHTML = 'Fix';

  var li = createTag('li', '', ul);
  li.innerHTML = 'Done';
}
