'use strict'

var videoElement;
var videoSelect;
var selectors;
var images = [];
var video, image;
var buttonTake, buttonRetake, buttonProceed;
var selectors = [];
const CONTAINER = document.getElementById('main-container');

function loadCamera() {
  video = document.getElementById('video');
  video.width = video.offsetWidth;
  video.setAttribute('playsinline', true);
  video.setAttribute('autoplay', true);

  row = document.getElementById('image1');
  // image.style.display = 'none';
  var row = createTag('div', 'row row-center');

  var v = createTag('div', 'select');
  var v1 = createTag('label', '', v);
  v1.setAttribute('for', 'videoSource');

  var se = createTag('select', '', v);
  se.id = 'videoSource';

  var row = createTag('div', 'row row-center');

  buttonTake = createTag('button', 'btn btn-raised btn-danger ', row);
  buttonTake.id = 'button-take';
  buttonTake.innerHTML = '<i class="material-icons" onclick="loadCamera">photo_camera</i>';


  buttonRetake = createTag('button', 'btn btn-outline-success btn-sm', row);
  buttonRetake.id = 'button-retake';
  buttonRetake.innerHTML = 'Next';
  buttonRetake.style.display = 'none';

  row = createTag('div', 'row row-center');
  buttonProceed = createTag('a', 'btn btn-outline-primary btn-sm', row);
  buttonProceed.id = 'button-proceed'
  buttonProceed.innerHTML = 'Proceed';
  buttonProceed.onclick = function () {
    clear();
    loadPictureSummary();
  };

  videoElement = document.querySelector('video');
  videoSelect = document.getElementById('videoSource');
  selectors = [videoSelect];
  navigator.mediaDevices.enumerateDevices().then(gotDevices).catch(handleError);
  videoSelect.onchange = start;
  start();
}

function gotDevices(deviceInfos) {
  // Handles being called several times to update labels. Preserve values.
  var values = selectors.map(function (select) {
    return select.value;
  });
  selectors.forEach(function (select) {
    while (select.firstChild) {
      select.removeChild(select.firstChild);
    }
  });
  for (var i = 0; i !== deviceInfos.length; ++i) {
    var deviceInfo = deviceInfos[i];
    var option = document.createElement('option');
    option.value = deviceInfo.deviceId;
    if (deviceInfo.kind === 'videoinput') {
      option.text = deviceInfo.label || 'camera ' + (videoSelect.length + 1);
      videoSelect.appendChild(option);
    } else {
      // console.log('Some other kind of source/device: ', deviceInfo);
    }
  }
  selectors.forEach(function (select, selectorIndex) {
    if (Array.prototype.slice.call(select.childNodes).some(function (n) {
        return n.value === values[selectorIndex];
      })) {
      select.value = values[selectorIndex];
    }
  });
}

function gotStream(stream) {
  window.stream = stream; // make stream available to console
  videoElement.srcObject = stream;
  // Refresh button list in case labels have become available
  return navigator.mediaDevices.enumerateDevices();
}

function start() {
  if (window.stream) {
    window.stream.getTracks().forEach(function (track) {
      track.stop();
    });
  }
  var videoSource = videoSelect.value;
  var constraints = {
    video: {
      deviceId: videoSource ? {
        exact: videoSource
      } : undefined
    }
  };
  navigator.mediaDevices.getUserMedia(constraints).
  then(gotStream).then(gotDevices).catch(handleError);

  video = document.getElementById("video")
  image = document.getElementById("image1")

  buttonTake = document.getElementById("button-take")
  buttonTake.onclick = function () {
    var canvas = document.createElement("canvas");
    canvas.width = video.offsetWidth;
    canvas.height = video.offsetHeight;
    canvas.getContext('2d')
      .drawImage(video, 0, 0, canvas.width, canvas.height);
    image.src = canvas.toDataURL();
    images.push(image.src)
    console.log(images)
    clear();
    // result();
  }
}

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


function uploadFile(){
  var x = document.getElementById("myFile");
  var txt = "";
  if ('files' in x) {
      if (x.files.length == 0) {
          txt = "Select one or more files.";
      } else {
          for (var i = 0; i < x.files.length; i++) {
              txt += "<br><strong>" + (i+1) + ". file</strong><br>";
              var file = x.files[i];
              if ('name' in file) {
                  txt += "name: " + file.name + "<br>";
              }
              if ('size' in file) {
                  txt += "size: " + file.size + " bytes <br>";
              }
          }
      }
  } 
  else {
      if (x.value == "") {
          txt += "Select one or more files.";
      } else {
          txt += "The files property is not supported by your browser!";
          txt  += "<br>The path of the selected file: " + x.value; // If the browser does not support the files property, it will return the path of the selected file instead. 
      }
  }
  document.getElementById("demo").innerHTML = txt;
}