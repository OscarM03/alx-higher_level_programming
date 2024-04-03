// JavaScript script that adds, removes and clears LI elements from a list
$(document).ready(function(){
  const newElem = '<li>Item</li>'
  $('#add_item').click(function(){
    $('UL.my_list').append(newElem);
  });

  $('#remove_item').click(function(){
    $('.my_list li:last-child').remove();
  });

  $('#clear_list').click(function() {
    $('.my_list').empty();
  });
});