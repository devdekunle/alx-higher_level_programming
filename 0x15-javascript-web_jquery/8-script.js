$(function() {

    $.ajax({

        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function(data) {

            films = data.results
            $.each(films, function(i, items) {

                $('UL#list_movies').append('<li>'+ items.title + '</li>');
            });

        }


    });

});
