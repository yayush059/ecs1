function openPDF(pdfUrl) {
    var modal = document.getElementById("pdfModal");
    var iframe = document.getElementById("pdfFrame");
    var span = document.getElementsByClassName("close")[0];

    iframe.src = pdfUrl;
    modal.style.display = "block";

    span.onclick = function() {
        modal.style.display = "none";
        iframe.src = "";
    }

    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
            iframe.src = "";
        }
    }
}
