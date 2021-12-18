$("input").keypress(function(event) {
    if (event.keyCode == 13){
      event.preventDefault();
      $("button").click()
    }
});
var originalHtml = $('#tb').html();
    
    $("button").click(function(){ 
        $('#tb').html(originalHtml);
        var player_name = $("input").val(); 
        var url = "/player/?search={player_name}"
        var final = url.replace('{player_name}',player_name)
          $.ajax({
                   url : final,
                   dataType: "json",
                   type: 'GET',
                   success : function (data) {
                             console.log(data.results.length);
                             var tr ,pr,cr,str;
                              for(var j = 0; j < data.results.length; j++){
                                   tr = $('<tr>');
                                   tr.append('<td>' + j+ "</td>" )
                                   $("#we").append(tr);
                                   cr   = $("<tr>");
                                   str  =  "/chart/?varname="+ data.results[j].player_name;
                                   cr.append('<td> <a href= " '+ str + ' "> '+ data.results[j].player_name+ "</a> </td>" )
                                   $("#wq").append(cr);
              }
             }
          });
        });

document.getElementById("input").value = "";