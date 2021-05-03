$(document).ready(function(){

  // $("#url").on("paste", function(){
  //     var req = {
  //         url: $("#url").val()
  //     };

  //     var response = $.ajax({
  //         url: "http://127.0.0.1:8800/get_feed/",
  //         type: "POST",
  //         data: JSON.stringify(req),
  //         contentType: "application/json",
  //         dataType: "json"
  //     });

  //     response.done(function(data){
  //         $("#taglink-model").addClass("show");
  //         $("#title").text(data.page.title);
  //         if(data.og.image){
  //             $("#img").attr("src", data.og.image);
  //         }else{
  //             $("#img").attr("src", "images/github.png");
  //         }
  //         $("#description").text(data.meta.description);
  //         console.log(data);
  //     });
  // });

  
  $("#btn").on("click", function(){
    var req = {
        url: $("#url").val()
    };

    var response = $.ajax({
        url: "http://127.0.0.1:8801/get_feed/",
        type: "POST",
        data: JSON.stringify(req),
        contentType: "application/json",
        dataType: "json"
    });

    response.done(function(data){
        if(data.entries){
            for(var i = 0; i < 5; i++){
                let head = $("<li></li>").html(
                    `
                    <h4> ${data.entries[i].title} </h4>
                    <p> ${data.entries[i].summary} </p>
                    <a href=${data.entries[i].link} target='_blank'>
                        Visit from here &nbsp;
                        <i class="fas fa-arrow-right"></i>
                    </a>
                    <span>${data.entries[i].published}</span>
                    `
                );
                $("#ol-list").append(head);
            }
        }
        console.log(data.entries[2]);
        });
    });
  
});