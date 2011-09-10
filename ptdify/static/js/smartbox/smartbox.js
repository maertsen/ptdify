var searchterms = {"data":[{"new":""}]};

var testresponse = {"data": [[{"context":"kamer"}, {"project":"opruimen"}],[{"context":"kamer"}, {"unknown":"opruimen"}]]}

function parseSelection(searchterms, term) {
	term.each(function(i,val){
		searchterms.data[0][i] = val;
	});	
}

function getParams(searchterms, req) {
	
	searchterms.data[0].new = req.term;
	
	return searchterms;
}

$(function() {

		

		$( "#smartbox" )
			// don't navigate away from the field on tab when selecting an item
			.bind( "keydown", function( event ) {
				if ( event.keyCode === $.ui.keyCode.TAB &&
						$( this ).data( "autocomplete" ).menu.active ) {
						
					event.preventDefault();
				} else if(event.keyCode === $.ui.keyCode.ENTER) {
					console.info('enter key pressed');
				} else if(event.keyCode === $.ui.keyCode.BACKSPACE) {
					console.info('backspace key pressed');
				}
			})
			.autocomplete({
				minLength: 0,

				source: testresponse.data
				
				/*function(req){  
		
					//$("#smartbox").trigger("select", testresponse);			
					
					//pass request to server  
					$.getJSON("/searchtags/", getParams(searchterms, req) ,  function(response) {  
	  
						//create array for response objects  
						var suggestions = [];  
	  
	  					response = testresponse;
	  
						//process response  
						$.each(response.data, function(i, val){  
							console.info(val);
							
							suggestions.push(val);  
						});  
	  
						//pass array to callback  
						return suggestions; 
						
					});  
				}*/, 

				focus: function() {
					// prevent value inserted on focus
					return true;
				},
				select: function( event, ui ) {
					//$("#searchtags ul").append('<li>'+ui.item.value+'</li>');
					//parseSelection(ui.item.value);
					//console.info("terms: "+searchterms);
					console.info(event);
					console.info(ui);
					this.value = "";
					return false;
				}
			}).data( "autocomplete" )._renderItem = function( ul, item ) {
			appendToString = "";
			$.each(item, function(key,val){
			if(val != undefined) {
				if(val.context != undefined) appendToString += "context: " +val.context;
				if(val.project != undefined) appendToString += "project: " +val.project;
				if(val.unknown != undefined) appendToString += "unknown: " +val.unknown;
				}

			});
			
			return $( "<li></li>" )
				.data( "item.autocomplete", item )
				.append( appendToString )
				.appendTo( ul );
			};
	});
