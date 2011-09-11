var searchterms = {"query": []};
var currentParamIndex = 0;

/**
	This function reads a json response item and returns html for the autocompletion
*/
function itemToHTML(data) {
	data.htmlValue = "<a>";
	$.each(data, function(key, val) {
		if(key >= 0 && val != undefined) { 
			data.htmlValue += "<span>"+val[0]+": "+val[1]+"</span>";
		}

	});
	data.htmlValue += "</a>";			
	return data;
}

function getSearchData(req) {
	
	searchterms.query[currentParamIndex] = [req.term, "New"];
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

				source:
				function(req, parseResult) {
					jQuery.ajax({
						   type: "GET",
						   url: "/ajax/autocomplete",
						   data: getSearchData(req),
						   processData: true,
						   dataType: "json",
						   traditional: true,
						   success: function(data) {parseResult(data);}
					   });
					   }
					   ,

				focus: function() {
					// prevent value inserted on focus
					return false;
				},
				select: function( event, ui ) {
					searchterms.query = [];
					$('#searchtags ul').empty();
					currentParamIndex = 0;
					$.each(ui.item, function(key, val) {
						if(key>=0 && val!== undefined) {
						 	$('#searchtags ul').append("<li>"+val[0]+"</li>");					
						 	searchterms.query.push([val[0], val[1]]);
						 	currentParamIndex++;
						}
					});				
					this.value = "";
					return false;
				}
			}).data( "autocomplete" )._renderItem = function( ul, item ) {
	
			parsedData = itemToHTML(item);
	
			return $( "<li></li>" )
				.data( "item.autocomplete", item )
				.append( parsedData.htmlValue )
				.appendTo( ul );
			};
	});
