//JavaScript script that fetches and lists the title for all
//movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function(data) {
    $(document).ready(function(){
      $.each(data.results, function(index, movie) {
        $('UL#list_movies').append('<li>' + movie.title + '<li>');
      });
    });
  },
  error: function(xhr, status, error){
    console.error('There was a problem with the AJAX request:', error)
  }
});