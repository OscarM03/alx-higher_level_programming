//JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays
//the value of hello from that fetch in the HTMLtag DIV#hello.
$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  method: 'GET',
  success: function(data){

    $(document).ready(function(){
      $('#hello').text(data.hello);
    });
  },
  error: function(xhr, status, error) {
    console.error('Error fetching translation:', error);
  }
});