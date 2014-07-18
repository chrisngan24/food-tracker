/* TODO
- function for plural, add s for days or inventory name (since we are just doing carrots and apples
- make colour scheme for expired, about to expire and good (red, orange, yellow, white?)
 */
$(document).on('pageshow', function () {
  $.get("footer.html", function(data){
    $("[data-role='footer']").after(data).trigger("create");
  });
}); 