$('.bd-example-modal-lg').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) 
    var recipient = button.attr("name");
  
    var modal = $(this)
    modal.find('.modal-title').text(recipient);
    recipient = recipient.replace(/\s/g, '');
    recipient=recipient.toLowerCase();
    $('.modal-content').css('background-image',"url('/static/images/"+recipient+".jpeg')");
    $('.modal-content').css('background-size',"cover");
   
    if (recipient=="eventx") {
      modal.find('.modal-body').text("Event X h ye");
    }
  })
  
  
    $('#nontech').click(function(){
  
     $('.tech').hide();
     $('.online').hide();
     $('.nontech').show();
      $('.mainevent').hide();
  });
     
     
    $('#tech').click(function(){
  
     $('.nontech').hide();
     $('.online').hide();
     $('.tech').show();
      $('.mainevent').hide();
  });  
    
      $('#online').click(function(){
  
     $('.nontech').hide();
     $('.online').show();
     $('.tech').hide();
      $('.mainevent').hide();
  }); 
  
    $('#mainevent').click(function(){
  
     $('.nontech').hide();
     $('.online').hide();
     $('.tech').hide();
     $('.mainevent').show();
  }); 