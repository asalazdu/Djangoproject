const loaderOut = document.querySelector("#loader-out");
function fadeOut(element) {
  let opacity = 1;
  const timer = setInterval(function () {
    if (opacity <= 0.1) {
      clearInterval(timer);
      element.style.display = "none";
    }
    element.style.opacity = opacity;
    opacity -= opacity * 0.1;
  }, 50);
}
fadeOut(loaderOut);

function buscadorTable(tableId) {
  let input = document.getElementById('search');
  let filter = input.value.toLowerCase();
  let table = document.getElementById(tableId);
  let tr = table.getElementsByTagName('tr');

  for (let i = 1; i < tr.length; i++) {
      let td = tr[i].getElementsByTagName('td');
      let found = false;

      for (let j = 0; j < td.length; j++) {
          if (td[j]) {
              let txtValue = td[j].textContent || td[j].innerText;
              if (txtValue.toLowerCase().indexOf(filter) > -1) {
                  found = true;
                  break;
              }
          }
      }

      tr[i].style.display = found ? '' : 'none';
  }
}


setTimeout(function() {
  var messageContainer = document.getElementById('message-container');
  if (messageContainer) {
      messageContainer.style.display = 'none';
  }
}, 2000);