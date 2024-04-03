//JavaScript script that fetches 
//the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  success: function(data) {
    $(document).ready(function(){
      $('#character').text(data.name)
    });
  },
  error: function(xhr, status, error) {
    console.error('There was a problem with the AJAX request:', error);
  }
});