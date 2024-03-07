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