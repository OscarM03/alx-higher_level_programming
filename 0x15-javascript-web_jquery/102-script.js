$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();

    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      method: 'GET',
      data: { lang: languageCode },
      success: function(data) {
        $('#hello').text(data.hello);
      },
      error: function(xhr, status, error) {
        console.error('Error fetching translation:', error);
      }
    });
  });
});
