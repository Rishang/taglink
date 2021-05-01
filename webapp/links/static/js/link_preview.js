$(document).ready(function(){
  
  var preview = false
  
  $("#url").keyup( function(){
      var req = {
          url: $("#url").val()
      };


      if (req.url != "") {
        
        var response = $.ajax({
          url: "http://127.0.0.1:8800/get_metadata/",
          type: "POST",
          data: JSON.stringify(req),
          contentType: "application/json",
          dataType: "json"
        });
  
        response.done(function(data){
          var image = data.og.image || data.page.image;
          var title = data.og.title || data.page.title;
          var description = data.og.description || data.page.description  || data.meta.Description || data.meta.description;
          
          
          
          $("#taglink-model").addClass("show");
          $("#title").text(title);
          $("#img").attr("src", image);
          $("#description").text(description);
          
          $("#form_title").val(title);
          $("#form_description").val(description);
          $("#id_imageUrl").val(image);
          console.log(data, image);
        });
      }
      else {
        console.log("error", req)
        preview = false
      }
  });

})

// $(document).ready(function(){
//   $("#url").on("keyup", function(event){
//     if(event.keyCode == 86){
//       $("#url").keyup(function(){
//         var req = {
//           url: $("#url").val()
//         };

//         var response = $.ajax({
//           url: "http://127.0.0.1:8800/get_metadata/",
//           type: "POST",
//           data: JSON.stringify(req),
//           contentType: "application/json",
//           dataType: "json"
//         });

//         response.done(function(data){
//           $("#model").addClass("show");
//           $("#title").text(data.page.title);
//           $("#description").text(data.meta.description);

//           $("#link_title").val(data.page.title);
//           $("#link_description").val(data.meta.description);

//           console.log(data);
//         });
//       });
//     }else{
//       $("#model").removeClass("show");
//     }
//   });
// });
