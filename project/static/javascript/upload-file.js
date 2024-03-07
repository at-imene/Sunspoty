//selecting all required elements
const dropArea = document.querySelector(".drag-area"),
  dragText = dropArea.querySelector("header"),
  dragSpan = dropArea.querySelector("span"),
  button = dropArea.querySelector("button"),
  input = dropArea.querySelector("input");

let file; //this is a global variable and we'll use it inside multiple functions

button.onclick = ()=>{
  input.click(); //if user click on the button then the input also clicked
}

input.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  file = this.files[0];
  
  dropArea.classList.add("active");
  // input.value = this.files[0];
  showFile(); //calling function
});


//If user Drag File Over DropArea
dropArea.addEventListener("dragover", (event)=>{
  event.preventDefault(); //preventing from default behaviour
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File";
});

//If user leave dragged File from DropArea
dropArea.addEventListener("dragleave", ()=>{
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop to Upload File";
});

//If user drop File on DropArea
dropArea.addEventListener("drop", (event)=>{
  event.preventDefault(); //preventing from default behaviour
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  file = event.dataTransfer.files[0];
  input.value = file;
  showFile(); //calling function
});

function showFile() {
  console.log(dropArea);
  let fileType = file.type; //getting selected file type
  let validExtensions = ["image/jpeg", "image/jpg", "image/png"]; //adding some valid image extensions in array
  if(validExtensions.includes(fileType)){ //if user selected file is an image file
    let fileReader = new FileReader(); //creating new FileReader object
    fileReader.onload = (e)=>{
      let fileURL = fileReader.result; //passing user file source in fileURL variable
      let imgTag = `<img src="${fileURL}" alt="image">`; //creating an img tag and passing user selected file source inside src attribute
      const imgElement = document.createElement('img');
      imgElement.src = fileURL;
      imgElement.alt = 'image';
      dropArea.appendChild(imgElement); //adding that created img tag inside dropArea container
      dropArea.removeChild(dragText);
      dropArea.removeChild(dragSpan);
      dropArea.removeChild(button);  
      console.log(dropArea.innerHTML);
    }
    fileReader.readAsDataURL(file);
  }else{
    alert("This is not an Image File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
}

function openPopup() {
  document.querySelector('.popup-container-original').style.display = 'flex';
}

function closePopup() {
  document.querySelector('.popup-container-original').style.display = 'none';
}

function openPopupNew() {
  document.querySelector('.popup-container-new').style.display = 'flex';
}

function closePopupNew() {
  document.querySelector('.popup-container-new').style.display = 'none';
}




document.addEventListener("DOMContentLoaded", function() {
  var anchors = document.getElementsByClassName("anchor");
  var firstAnchor = anchors[0]; // Get the first anchor element

  // Add "active" class to the first anchor by default
  firstAnchor.classList.add("active-anchor");

  // Attach event listeners to each anchor
  for (var i = 0; i < anchors.length; i++) {
    anchors[i].addEventListener("mouseover", function() {
      // Add "active" class to the hovered anchor
      this.classList.add("active-anchor");
      // Remove "active" class from the other anchors
      for (var j = 0; j < anchors.length; j++) {
        if (anchors[j] !== this) {
          anchors[j].classList.remove("active-anchor");
        }
      }
    });

    anchors[i].addEventListener("mouseout", function() {
      // Remove "active" class when the mouse leaves the anchor
      this.classList.remove("active-anchor");
      // Add "active" class back to the first anchor
      firstAnchor.classList.add("active-anchor");
    });
  }
});